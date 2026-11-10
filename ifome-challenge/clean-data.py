import pandas as pd

# ---------- Settings (adjust these to your file) ----------
file_path = "pedidos.csv"
separator = ";"            # use "," if your CSV is comma-separated
encoding = "utf-8-sig"     # try "latin-1" if you see strange characters
order_column = "id_pedido"  # exact column name in your CSV

# ---------- Load the file ----------
df = pd.read_csv(file_path, sep=separator, encoding=encoding, dtype=str)

# Remove hidden spaces from the column names
df.columns = df.columns.str.strip()

# Helpful while debugging: shows the real column names
print("Columns found:", df.columns.tolist())

# Stop with a clear message if the column does not exist
if order_column not in df.columns:
    raise SystemExit(
        f"Column '{order_column}' not found. "
        f"Set order_column to one of: {df.columns.tolist()}"
    )

# ---------- Clean the data ----------
# Remove extra spaces around the order numbers
df[order_column] = df[order_column].str.strip()

# Ignore rows with an empty order number
df = df.dropna(subset=[order_column])

# ---------- Count duplicates ----------
total_rows = len(df)
unique_orders = df[order_column].nunique()
extra_rows = df.duplicated(subset=order_column, keep="first").sum()
orders_with_duplicates = (df[order_column].value_counts() > 1).sum()

print()
print(f"Total rows: {total_rows}")
print(f"Unique order numbers: {unique_orders}")
print(f"Order numbers that appear more than once: {orders_with_duplicates}")
print(f"Extra duplicated rows: {extra_rows}")

# ---------- Show and save the duplicated rows ----------
# keep=False marks ALL occurrences of a duplicated order number
duplicates = df[df.duplicated(subset=order_column, keep=False)]
duplicates = duplicates.sort_values(by=order_column)

if duplicates.empty:
    print("\nNo duplicate order numbers found.")
else:
    print("\nDuplicated rows:")
    print(duplicates)
    duplicates.to_csv("pedidos_duplicados.csv", index=False, sep=separator)

    # How many times each duplicated order appears
    counts = df[order_column].value_counts()
    print("\nTimes each duplicated order appears:")
    print(counts[counts > 1])

# ---------- Optional: save a version without duplicates ----------
df_clean = df.drop_duplicates(subset=order_column, keep="first")
df_clean.to_csv("pedidos_sem_duplicados.csv", index=False, sep=separator)
print(f"\nClean file saved with {len(df_clean)} rows.")
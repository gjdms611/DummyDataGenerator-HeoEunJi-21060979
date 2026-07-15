# DummyDataGenerator

Generates dummy `orders` rows into a local SQLite database (`dummy.db`) using
`faker`.

## Install

```
pip install -r requirements.txt
```

## Usage

```
python main.py --count N [--reset]
```

- `--count N` — number of orders to generate (default 10).
- `--reset` — drop and recreate the `orders` table before inserting. Without
  this flag, rows accumulate on every run.

Examples:

```
python main.py                # inserts 10 orders, appending
python main.py --count 5      # inserts 5 orders, appending
python main.py --count 5 --reset   # wipes the table, then inserts 5 orders
```

## Manual Verification

```
sqlite3 dummy.db
.tables
.schema orders
SELECT * FROM orders LIMIT 5;
```

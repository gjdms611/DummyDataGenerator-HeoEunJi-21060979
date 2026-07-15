# CLAUDE.md (DummyDataGenerator)

## Tech Stack

- Python 3 standard library `sqlite3` for storage.
- `faker` library for generating dummy data.
- No web framework, no ORM — a single `main.py` CLI script.

## Schema

Table `orders`:

| column        | type                    | notes                        |
|---------------|-------------------------|-------------------------------|
| id            | INTEGER PRIMARY KEY     | autoincrement                 |
| order_no      | TEXT                    | e.g. `ORD-000001`             |
| customer_name | TEXT                    | faker-generated                |
| product_name  | TEXT                    | faker-generated                |
| quantity      | INTEGER                 |                                |
| status        | TEXT                    | one of pending/shipped/completed |
| created_at    | TEXT                    | timestamp                     |

## Duplicate Policy: Accumulate by Default, `--reset` to Opt Out

Running `main.py` without `--reset` appends new rows to the existing `orders`
table on every run (duplicate order_no/customer_name/etc. are allowed — only
`id` is guaranteed unique). Passing `--reset` drops and recreates the table
first.

This is a deliberate default, not an oversight: the source requirements doc
leaves this behavior as TBD/free-design. Defaulting to accumulate better
demonstrates the "insert into existing storage, then query" completion
criterion (running the tool multiple times shows data piling up in the same
DB, which is closer to how a real dummy-data seeding tool is used) than
silently wiping data on every run.

## File Output Path Rule (inherited)

Per the parent project's CLAUDE.md, all generated files (code, docs, DB,
artifacts) must stay under:

`D:\user\education\2026_CRA_AI\final_test`

Do not write files outside this tree.

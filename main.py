# ==============================================================
# Import libraries 
# ==============================================================
import sqlite3
from pathlib import Path


# ==============================================================
# Parameters
# ==============================================================
DB_PATH = Path("./flight_management.db")
SCHEMA_SQL_PATH = Path("./schema.sql")

# ==============================================================
# Initialise database
# ==============================================================
def connect_db() -> sqlite3.Connection:
    """Open a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    # Enable foreign key suport in SQLite
    conn.execute("PRAGMA foreign_keys = ON;") 
    return conn

def initialise_db(conn: sqlite3.Connection) -> None:
    """Initilise the database by executing the database schema SQL scripts."""
    try:
        schema_sql = SCHEMA_SQL_PATH.read_text(encoding="utf-8")
        conn.executescript(schema_sql)
        conn.commit()
        print("Database initialised successfully.")
    except FileNotFoundError:
        print(f"Error. Database not initialised. File {SCHEMA_SQL_PATH} not found.")


# ==============================================================
# Main Logic of the program
# ==============================================================
def main() -> None:
    """Main function that initialises the Flight Management database and launches the CLI for user interaction."""
    with connect_db() as conn:
        initialise_db(conn)

if __name__ == "__main__":
    main()
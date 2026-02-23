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
# Populate database with mock data
# ==============================================================
def populate_db(conn: sqlite3.Connection) -> None:
    """"Populate the database with mock data."""

    # Generated mock data.
    flights = [
        ("BA1001", 5, 1, 2,  "2026-03-01 10:30:00.000", "2026-03-01 18:05:00.000", "SCHEDULED"),  # LHR->JFK
        ("BA1002", 1, 1, 3,  "2026-03-02 07:15:00.000", "2026-03-02 09:35:00.000", "SCHEDULED"),  # LHR->CDG
        ("BA1003", 2, 1, 4,  "2026-03-02 12:20:00.000", "2026-03-02 14:40:00.000", "DELAYED"),    # LHR->AMS
        ("BA1004", 2, 1, 5,  "2026-03-03 09:00:00.000", "2026-03-03 11:10:00.000", "SCHEDULED"),  # LHR->FRA
        ("BA1005", 4, 1, 6,  "2026-03-03 15:45:00.000", "2026-03-03 18:55:00.000", "SCHEDULED"),  # LHR->MAD
        ("BA1006", 1, 1, 7,  "2026-03-04 08:10:00.000", "2026-03-04 11:25:00.000", "SCHEDULED"),  # LHR->BCN
        ("BA1007", 9, 3, 8,  "2026-03-04 17:00:00.000", "2026-03-04 18:20:00.000", "CANCELLED"),  # CDG->DUB
        ("BA1008", 7, 1, 9,  "2026-03-05 21:30:00.000", "2026-03-06 07:15:00.000", "SCHEDULED"),  # LHR->DXB
        ("BA1009", 6, 1, 10, "2026-03-06 13:00:00.000", "2026-03-07 10:20:00.000", "SCHEDULED"),  # LHR->HND
        ("BA1010", 10, 1, 11, "2026-03-07 20:10:00.000", "2026-03-08 12:30:00.000", "SCHEDULED"), # LHR->SIN
        ("BA1011", 8, 4, 5,  "2026-03-08 06:40:00.000", "2026-03-08 08:50:00.000", "DEPARTED"),   # AMS->FRA (arrival after departure)
        ("BA1012", 3, 4, 1,  "2026-03-09 09:30:00.000", "2026-03-09 10:35:00.000", "ARRIVED"),    # AMS->LHR (arrival after departure)
        ("BA1013", 12, 8, 1, "2026-03-10 14:05:00.000", "2026-03-10 15:30:00.000", "SCHEDULED"),  # DUB->LHR
        ("BA1014", 14, 13, 12, "2026-03-11 16:20:00.000", "2026-03-11 18:05:00.000", "SCHEDULED"),# SFO->LAX
        ("BA1015", 15, 15, 14, "2026-03-12 22:10:00.000", "2026-03-13 06:25:00.000", "SCHEDULED"),# SYD->YYZ
    ]

    pilots = [
        ("LIC-UK-7Q2A91", "Amelia", None, "Carter", "+44 7700 900101", "amelia.carter@example.com", "2012-02-01 09:00:00.000", None, 1),
        ("LIC-UK-5M8K44", "Noah", "J", "Hughes", "+44 7700 900102", "noah.hughes@example.com", "2019-06-10 09:00:00.000", None, 1),
        ("LIC-UK-3P1R77", "Maya", None, "Patel", "+44 7700 900103", "maya.patel@example.com", "2014-01-20 09:00:00.000", None, 1),
        ("LIC-UK-8D6T20", "Oliver", None, "Reed", "+44 7700 900104", "oliver.reed@example.com", "2021-04-12 09:00:00.000", None, 1),
        ("LIC-UK-1V9S38", "Sophia", None, "Brown", "+44 7700 900105", "sophia.brown@example.com", "2009-09-01 09:00:00.000", None, 1),
        ("LIC-UK-4H0N62", "Ethan", None, "Ward", "+44 7700 900106", "ethan.ward@example.com", "2018-11-05 09:00:00.000", None, 1),
        ("LIC-UK-6B3X15", "Lily", "A", "Evans", "+44 7700 900107", "lily.evans@example.com", "2016-07-07 09:00:00.000", None, 1),
        ("LIC-UK-2C7F89", "James", None, "Murphy", "+44 7700 900108", "james.murphy@example.com", "2022-02-14 09:00:00.000", None, 1),
        ("LIC-UK-9Z5L11", "Ava", None, "Khan", "+44 7700 900109", "ava.khan@example.com", "2013-10-03 09:00:00.000", None, 1),
        ("LIC-UK-0Q6Y53", "Lucas", None, "Shaw", "+44 7700 900110", "lucas.shaw@example.com", "2020-05-22 09:00:00.000", None, 1),
        ("LIC-UK-7R4W66", "Isabella", None, "Diaz", "+44 7700 900111", "isabella.diaz@example.com", "2011-12-01 09:00:00.000", None, 1),
        ("LIC-UK-5A2G09", "Daniel", None, "Green", "+44 7700 900112", "daniel.green@example.com", "2017-08-18 09:00:00.000", None, 1),
        ("LIC-UK-8N1U24", "Harper", None, "Foster", "+44 7700 900113", "harper.foster@example.com", "2015-03-09 09:00:00.000", None, 1),
        ("LIC-UK-3K9E70", "Logan", "M", "Brooks", "+44 7700 900114", "logan.brooks@example.com", "2010-10-14 09:00:00.000", "2024-06-30 17:00:00.000", 0),
        ("LIC-UK-6J8P32", "Zoe", None, "Bennett", "+44 7700 900115", "zoe.bennett@example.com", "2018-09-03 09:00:00.000", "2025-11-15 17:00:00.000", 0),
    ]

    # Exactly 15 rows total; two flights have 2 pilots each; two flights have no assignments.
    # Avoid sequential symmetry like (1,1), (2,2), etc.
    flight_pilots = [
        (1, 5),
        (2, 1),
        (3, 9),
        (4, 3),
        (5, 11),
        (6, 2),
        (7, 7),
        (8, 12),
        (9, 4),
        (10, 6),
        (11, 10),  # Flight 11 has 2 pilots
        (11, 2),
        (12, 8),   # Flight 12 has 2 pilots
        (12, 13),
        (13, 1),
    ]

    aircraft = [
        ("Airbus A320-200", 180, "2016-03-12 00:00:00.000", "2026-01-18 08:15:00.000"),
        ("Airbus A321neo", 220, "2019-07-04 00:00:00.000", "2026-02-05 10:30:00.000"),
        ("Airbus A319-100", 144, "2014-11-21 00:00:00.000", "2026-01-09 06:45:00.000"),
        ("Boeing 737-800", 189, "2015-05-16 00:00:00.000", "2026-02-12 14:20:00.000"),
        ("Boeing 777-300ER", 396, "2013-09-02 00:00:00.000", "2026-01-27 09:10:00.000"),
        ("Boeing 787-9", 290, "2018-02-14 00:00:00.000", "2026-02-08 12:00:00.000"),
        ("Airbus A350-900", 325, "2020-10-30 00:00:00.000", "2026-02-16 07:55:00.000"),
        ("Embraer E190", 100, "2017-06-08 00:00:00.000", "2026-01-22 16:35:00.000"),
        ("ATR 72-600", 72, "2012-04-19 00:00:00.000", "2026-01-04 11:05:00.000"),
        ("Airbus A330-300", 300, "2011-12-03 00:00:00.000", "2026-01-29 05:40:00.000"),
        ("Boeing 737 MAX 8", 178, "2021-08-26 00:00:00.000", "2026-02-10 13:25:00.000"),
        ("Airbus A220-300", 145, "2022-01-15 00:00:00.000", "2026-02-18 09:05:00.000"),
        ("Boeing 757-200", 200, "2009-03-28 00:00:00.000", "2026-01-13 17:50:00.000"),
        ("Airbus A320neo", 186, "2023-05-09 00:00:00.000", "2026-02-20 08:30:00.000"),
        ("Boeing 767-300ER", 261, "2010-07-17 00:00:00.000", "2026-01-25 15:15:00.000"),
    ]

    destinations = [
        ("LHR", "London Heathrow Airport", "London", "United Kingdom", "T5"),
        ("JFK", "John F. Kennedy International Airport", "New York", "United States", "T4"),
        ("CDG", "Charles de Gaulle Airport", "Paris", "France", "2E"),
        ("AMS", "Amsterdam Airport Schiphol", "Amsterdam", "Netherlands", "1"),
        ("FRA", "Frankfurt Airport", "Frankfurt", "Germany", "1"),
        ("MAD", "Adolfo Suárez Madrid-Barajas Airport", "Madrid", "Spain", "T4"),
        ("BCN", "Barcelona-El Prat Airport", "Barcelona", "Spain", "T1"),
        ("DUB", "Dublin Airport", "Dublin", "Ireland", "T2"),
        ("DXB", "Dubai International Airport", "Dubai", "United Arab Emirates", "T3"),
        ("HND", "Tokyo Haneda Airport", "Tokyo", "Japan", "I"),
        ("SIN", "Singapore Changi Airport", "Singapore", "Singapore", "T3"),
        ("LAX", "Los Angeles International Airport", "Los Angeles", "United States", "B"),
        ("SFO", "San Francisco International Airport", "San Francisco", "United States", "2"),
        ("YYZ", "Toronto Pearson International Airport", "Toronto", "Canada", "1"),
        ("SYD", "Sydney Kingsford Smith Airport", "Sydney", "Australia", "T1"),
    ]

    # Inject the mock data into the database.
    with conn:
        conn.executemany("INSERT INTO Flight(FlightNumber, AircraftId, DepartureAirportId, DestinationAirportId, DepartureTime, DestinationArrivalTime, FlightStatus) VALUES (?, ?, ?, ?, ?, ?, ?);", flights)

# ==============================================================
# Main Logic of the program
# ==============================================================
def main() -> None:
    """Main function that initialises the Flight Management database and launches the CLI for user interaction."""
    with connect_db() as conn:
        initialise_db(conn)

if __name__ == "__main__":
    main()
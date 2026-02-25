# ==============================================================
# Import libraries 
# ==============================================================
import sqlite3
from pathlib import Path
from datetime import datetime

# ==============================================================
# Parameters
# ==============================================================
DB_PATH = Path("./flight_management.db")
SCHEMA_SQL_PATH = Path("./schema.sql")

# ==============================================================
# Global variables
# ==============================================================
valid_flight_statuses = ('SCHEDULED', 'DELAYED', 'CANCELLED', 'DEPARTED', 'ARRIVED')

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
        print("\nDatabase initialised successfully.\n")
    except FileNotFoundError:
        print(f"\nError. Database not initialised. File {SCHEMA_SQL_PATH} not found.\n")

# ==============================================================
# Populate database with mock data
# ==============================================================
def populate_db(conn: sqlite3.Connection) -> None:
    """"Populate the database with mock data."""

    # Generated mock data.
    aircraft = [
        ("Airbus A320-200", 180, "2016-03-12 00:00", "2026-01-18 08:15"),
        ("Airbus A321neo", 220, "2019-07-04 00:00", "2026-02-05 10:30"),
        ("Airbus A319-100", 144, "2014-11-21 00:00", "2026-01-09 06:45"),
        ("Boeing 737-800", 189, "2015-05-16 00:00", "2026-02-12 14:20"),
        ("Boeing 777-300ER", 396, "2013-09-02 00:00", "2026-01-27 09:10"),
        ("Boeing 787-9", 290, "2018-02-14 00:00", "2026-02-08 12:00"),
        ("Airbus A350-900", 325, "2020-10-30 00:00", "2026-02-16 07:55"),
        ("Embraer E190", 100, "2017-06-08 00:00", "2026-01-22 16:35"),
        ("ATR 72-600", 72, "2012-04-19 00:00", "2026-01-04 11:05"),
        ("Airbus A330-300", 300, "2011-12-03 00:00", "2026-01-29 05:40"),
        ("Boeing 737 MAX 8", 178, "2021-08-26 00:00", "2026-02-10 13:25"),
        ("Airbus A220-300", 145, "2022-01-15 00:00", "2026-02-18 09:05"),
        ("Boeing 757-200", 200, "2009-03-28 00:00", "2026-01-13 17:50"),
        ("Airbus A320neo", 186, "2023-05-09 00:00", "2026-02-20 08:30"),
        ("Boeing 767-300ER", 261, "2010-07-17 00:00", "2026-01-25 15:15"),
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

    pilots = [
        ("LIC-UK-7Q2A91", "Amelia", None, "Carter", "+44 7700 900101", "amelia.carter@example.com", "2012-02-01 09:00", None, 1),
        ("LIC-UK-5M8K44", "Noah", "J", "Hughes", "+44 7700 900102", "noah.hughes@example.com", "2019-06-10 09:00", None, 1),
        ("LIC-UK-3P1R77", "Maya", None, "Patel", "+44 7700 900103", "maya.patel@example.com", "2014-01-20 09:00", None, 1),
        ("LIC-UK-8D6T20", "Oliver", None, "Reed", "+44 7700 900104", "oliver.reed@example.com", "2021-04-12 09:00", None, 1),
        ("LIC-UK-1V9S38", "Sophia", None, "Brown", "+44 7700 900105", "sophia.brown@example.com", "2009-09-01 09:00", None, 1),
        ("LIC-UK-4H0N62", "Ethan", None, "Ward", "+44 7700 900106", "ethan.ward@example.com", "2018-11-05 09:00", None, 1),
        ("LIC-UK-6B3X15", "Lily", "A", "Evans", "+44 7700 900107", "lily.evans@example.com", "2016-07-07 09:00", None, 1),
        ("LIC-UK-2C7F89", "James", None, "Murphy", "+44 7700 900108", "james.murphy@example.com", "2022-02-14 09:00", None, 1),
        ("LIC-UK-9Z5L11", "Ava", None, "Khan", "+44 7700 900109", "ava.khan@example.com", "2013-10-03 09:00", None, 1),
        ("LIC-UK-0Q6Y53", "Lucas", None, "Shaw", "+44 7700 900110", "lucas.shaw@example.com", "2020-05-22 09:00", None, 1),
        ("LIC-UK-7R4W66", "Isabella", None, "Diaz", "+44 7700 900111", "isabella.diaz@example.com", "2011-12-01 09:00", None, 1),
        ("LIC-UK-5A2G09", "Daniel", None, "Green", "+44 7700 900112", "daniel.green@example.com", "2017-08-18 09:00", None, 1),
        ("LIC-UK-8N1U24", "Harper", None, "Foster", "+44 7700 900113", "harper.foster@example.com", "2015-03-09 09:00", None, 1),
        ("LIC-UK-3K9E70", "Logan", "M", "Brooks", "+44 7700 900114", "logan.brooks@example.com", "2010-10-14 09:00", "2024-06-30 17:00", 0),
        ("LIC-UK-6J8P32", "Zoe", None, "Bennett", "+44 7700 900115", "zoe.bennett@example.com", "2018-09-03 09:00", "2025-11-15 17:00", 0),
    ]

    flights = [
        ("BA1001", 5, 1, 2,  "2026-03-01 10:30", "2026-03-01 18:05", "SCHEDULED"),  # LHR->JFK
        ("BA1002", 1, 1, 3,  "2026-03-02 07:15", "2026-03-02 09:35", "SCHEDULED"),  # LHR->CDG
        ("BA1003", 2, 1, 4,  "2026-03-02 12:20", "2026-03-02 14:40", "DELAYED"),    # LHR->AMS
        ("BA1004", 2, 1, 5,  "2026-03-03 09:00", "2026-03-03 11:10", "SCHEDULED"),  # LHR->FRA
        ("BA1005", 4, 1, 6,  "2026-03-03 15:45", "2026-03-03 18:55", "SCHEDULED"),  # LHR->MAD
        ("BA1006", 1, 1, 7,  "2026-03-04 08:10", "2026-03-04 11:25", "SCHEDULED"),  # LHR->BCN
        ("BA1007", 9, 3, 8,  "2026-03-04 17:00", "2026-03-04 18:20", "CANCELLED"),  # CDG->DUB
        ("BA1008", 7, 1, 9,  "2026-03-05 21:30", "2026-03-06 07:15", "SCHEDULED"),  # LHR->DXB
        ("BA1009", 6, 1, 10, "2026-03-06 13:00", "2026-03-07 10:20", "SCHEDULED"),  # LHR->HND
        ("BA1010", 10, 1, 11, "2026-03-07 20:10", "2026-03-08 12:30", "SCHEDULED"), # LHR->SIN
        ("BA1011", 8, 4, 5,  "2026-03-08 06:40", "2026-03-08 08:50", "DEPARTED"),   # AMS->FRA (arrival after departure)
        ("BA1012", 3, 4, 1,  "2026-03-09 09:30", "2026-03-09 10:35", "ARRIVED"),    # AMS->LHR (arrival after departure)
        ("BA1013", 12, 8, 1, "2026-03-10 14:05", "2026-03-10 15:30", "SCHEDULED"),  # DUB->LHR
        ("BA1014", 14, 13, 12, "2026-03-11 16:20", "2026-03-11 18:05", "SCHEDULED"),# SFO->LAX
        ("BA1015", 15, 15, 14, "2026-03-12 22:10", "2026-03-13 06:25", "SCHEDULED"),# SYD->YYZ
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

    # Inject the mock data into the database.
    with conn:
        # Aircraft table
        conn.executemany("INSERT INTO Aircraft(Model, PassengerCapacity, BuiltDate, LastCheckDate) VALUES (?, ?, ?, ?);",
            aircraft)
        print("Inserted data into Aircraft table successfully.")

        # Destination table
        conn.executemany("INSERT INTO Destination(AirportCode, AirportName, City, Country, Terminal) VALUES (?, ?, ?, ?, ?);",
                         destinations)
        print("Inserted data into Destination table successfully.")

        # Pilot table
        conn.executemany("""
                        INSERT INTO Pilot(LicenseNumber, FirstName, MiddleName, LastName, MobilePhone, Email, EmploymentStartDate, EmploymentEndDate, IsActive)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
                         """,
                        pilots)
        print("Inserted data into Pilot table successfully.")

        # Flight table
        conn.executemany("INSERT INTO Flight(FlightNumber, AircraftId, DepartureAirportId, DestinationAirportId, DepartureTime, DestinationArrivalTime, FlightStatus) VALUES (?, ?, ?, ?, ?, ?, ?);", 
                        flights)
        print("Inserted data into Flight table successfully.")

        # Flight_Pilot table
        conn.executemany("INSERT INTO Flight_Pilot(FlightId, PilotId) VALUES (?, ?);",
                        flight_pilots)
        print("Inserted data into Flight_Pilot table successfully.")

# ==============================================================
# Define helper functions 
# ==============================================================
def get_non_empty_input(value: str) -> str:
    """Helper function that ensures user input is a not empty string."""
    while True:
        s = input(value).strip()
        if s:
            return s
        print("\t\tInput cannot be empty. Please, try again.")

def get_non_empty_integer_input(value: str) -> int:
    """Helper function that ensures user input is a non-empty integer."""
    while True:
        s = input(value).strip()
        if s:
            try:
                return int(s)
            except ValueError:
                print("\t\tInput must be an integer, e.g., 123. Please, try again.")
        else:
            print("\t\tInput cannot be empty. Please, try again.")

def get_valid_datetime_input(value: str) -> datetime:
    """Helper function that ensures user input is a non-empty and valid datetime string."""
    while True:
        s = input(value).strip()
        if not s:
            print("\t\tInput cannot be empty. Please, try again.")
            continue

        try:
            dt = datetime.strptime(s, "%Y-%m-%d %H:%M")
            return dt
        except ValueError:
            print("\t\tInvalid datetime format. Correct format: YYYY-MM-DD HH:MM, e.g., 2026-03-01 10:30. Please, try again.")

def pretty_printing_flight_information(flight_info_list: list) -> None:
    """Helper function that prints the obtained flight information in a more user-friendly format."""""
    if not flight_info_list:
        print("\t\tNo flight information to display. Please, check your criteria and try again.")
        return

    print("\nFlight Information:")
    print("-" * 80)
    for flight_idx, flight in enumerate(flight_info_list):
        print("Flight", flight_idx + 1, ":")
        print(f"\tFlight Number: {flight[0]}")
        print(f"\tDeparture Time: {flight[1]}")
        print(f"\tDestination Arrival Time: {flight[2]}")
        print(f"\tFlight Status: {flight[3]}")
        print(f"\tDestination Airport Code: {flight[4]}")
        print(f"\tDestination Airport Name: {flight[5]}")
        print(f"\tDestination City: {flight[6]}")
        print(f"\tDestination Country: {flight[7]}")
        print(f"\tTerminal: {flight[8]}")
        print("-" * 80)

def print_table(rows, headers):
    """Helper function to display a pilot's schedule in a user-friendly, tabular format."""
    # Combine table headers and underlying data to calculate column widths
    data = [headers] + rows
    widths = [max(len(str(row[i])) for row in data) for i in range(len(headers))]

    # Print table headers
    print()
    print(" | ".join(str(headers[i]).ljust(widths[i]) for i in range(len(headers))))
    print("-" * (sum(widths) + 3 * (len(headers) - 1)))

    # Print table content
    for row in rows:
        print(" | ".join(str(row[i]).ljust(widths[i]) for i in range(len(row))))
    print()

# ==============================================================
# Define functions for menu options
# ==============================================================
# ==============================================================
# add_new_flight() - Function allows the user to add a new flight to the database by collecting necessary information from the user.
# ==============================================================
def add_new_flight(conn: sqlite3.Connection) -> None:
    """Function allows the user to add a new flight to the database by collecting necessary information from the user."""
    print("\nTo add a new flight, please provide the following information:")

    # FlightNumber - TEXT NOT NULL UNIQUE
    # TODO: Write a test check the uniqueness of the Flight number provided by the user.
    flight_number = get_non_empty_input("\tFlight Number (e.g., AA123): ")

    # AircraftId - INTEGER NOT NULL
    # TODO: Encapsulate the below lodgic into a more generic, reusable helper function.
    while True:
        aircraft_model = get_non_empty_input("\tAircraft Model (e.g., Airbus A320-200): ")
        search_for_aircraft_id = conn.execute("SELECT AircraftId FROM Aircraft WHERE Model = ? COLLATE NOCASE;", (aircraft_model,)).fetchone()
        
        if search_for_aircraft_id:
            aircraft_id = search_for_aircraft_id[0]
            break
        else:
            print("\t\tError. Aircraft model not found in the database. Please, try again.")
    
    # DepartureAirportId - INTEGER NOT NULL
    # TODO: Encapsulate the below lodgic into a more generic, reusable helper function.
    while True:
        departure_airport_code = get_non_empty_input("\tDeparture Airport Code (e.g., LHR): ")
        search_for_departure_aiport_id = conn.execute("SELECT DestinationId FROM Destination WHERE AirportCode = ? COLLATE NOCASE;", (departure_airport_code,)).fetchone()
        
        if search_for_departure_aiport_id:
            departure_airport_id = search_for_departure_aiport_id[0]
            break
        else:
            print("\t\tError. Departure airport code not found in the database. Please, try again.")

    # DestinationAirportId - INTEGER NOT NULL
    # TODO: Encapsulate the below lodgic into a more generic, reusable helper function.
    while True:
        destination_airport_code = get_non_empty_input("\tDestination Airport Code (e.g., JFK): ")
        search_for_destination_airport_id = conn.execute("SELECT DestinationId FROM Destination WHERE AirportCode = ? COLLATE NOCASE;", (destination_airport_code,)).fetchone()

        if search_for_destination_airport_id:
            destination_airport_id = search_for_destination_airport_id[0]
            break
        else:
            print("\t\tError. Destination airport code not found in the database. Please, try again.")

    # DepartureTime - TEXT NOT NULL
    departure_datetime = get_valid_datetime_input("\tDeparture Time (e.g., 2026-02-01 10:30): ")
    # Covert time from datetime object to string in the correct format for SQLite
    departure_time = departure_datetime.strftime("%Y-%m-%d %H:%M")

    # DestinationArrivalTime - TEXT NOT NULL
    while True:
        destination_arrival_datetime = get_valid_datetime_input("\tDestination Arrival Time (e.g., 2026-02-01 13:30): ")
        # Check that the destination arrival time is after the departure time.
        if destination_arrival_datetime > departure_datetime:
            # Covert time from datetime object to string in the correct format for SQLite
            destination_arrival_time = destination_arrival_datetime.strftime("%Y-%m-%d %H:%M")
            break
        else:
            print("\t\tError. Destination arrival time must be after the departure time. Please, try again.")
    
    # FlightStatus - TEXT NOT NULL CHECK (FlightStatus IN ('SCHEDULED', 'DELAYED', 'CANCELLED', 'DEPARTED', 'ARRIVED'))
    while True:
        flight_status = get_non_empty_input(f"\tFlight Status {valid_flight_statuses}: ").upper()
        if flight_status in valid_flight_statuses:
            break
        else:
            print(f"\t\tError. Invalid flight status. Please, select one of the following: {valid_flight_statuses}.")

    # Add the new flight to the database.
    with conn:
            conn.execute(
                """
                INSERT INTO Flight(FlightNumber, AircraftId, DepartureAirportId, DestinationAirportId, DepartureTime, DestinationArrivalTime, FlightStatus)
                VALUES (?, ?, ?, ?, ?, ?, ?);
                """,
                (flight_number, aircraft_id, departure_airport_id, destination_airport_id, departure_time, destination_arrival_time, flight_status),
            )
    print("\nNew flight added successfully.\n")

# ==============================================================
# add_new_flight() - Function allows the user to filter the flights based on several criteria.
# ==============================================================
def view_flights_by_criteria(conn: sqlite3.Connection) -> None:
    """
    Function allows the user to filter the flights based on several criteria:
    - Destination Airport Code
    - Departure Date
    - Flight Status.

    User can press Enter to skip any of the above criteria. If all criteria are skipped, no flights will be returned.
    """
    print("\nProvide the below details to view the respective flights. Press Enter to skip any criteria.")

    criteria_list = []
    
    # Get Destination Aiport Code from the user
    while True:
        destination_airport_code = input("\tDestination Airport Code (e.g., JFK): ").strip().upper()
        if destination_airport_code == "":
            break
        else:
            search_for_destination_airport_code = conn.execute("SELECT AirportCode FROM Destination WHERE AirportCode = ? COLLATE NOCASE;", (destination_airport_code,)).fetchone()
            if search_for_destination_airport_code:
                criteria_list.append(destination_airport_code)
                break
            else:
                print("\t\tError. Destination Airport Code not found in the database. Please, try again.")

    # Get Departure Date from the user
    while True:
        departure_datetime = input("\tDeparture Time (e.g., 2026-02-01 10:30): ").strip()
        if departure_datetime == "":
            break
        else:
            try:
                departure_datetime = datetime.strptime(departure_datetime, "%Y-%m-%d %H:%M")
                # Convert time from datetime object to string in the correct format for SQLite
                departure_time = departure_datetime.strftime("%Y-%m-%d %H:%M")
                criteria_list.append(departure_time)
                break
            except ValueError:
                print("\t\tInvalid datetime format. Correct format: YYYY-MM-DD HH:MM, e.g., 2026-03-01 10:30. Please, try again.")
        
    # Get Flight Status from the user
    while True:
        flight_status = input(f"\tFlight Status {valid_flight_statuses}: ").strip()
        if flight_status == "":
            break
        else:
            flight_status = flight_status.upper()
            if flight_status in valid_flight_statuses:
                criteria_list.append(flight_status)
                break
            else:
                print(f"\t\tError. Invalid flight status. Please, select one of the following: {valid_flight_statuses}.")

    print(criteria_list)

    # Specify template SQL query that will be amended depending on the chosen criteria.
    template_sql_query_for_viewing_flights = """
        SELECT 
            f.FlightNumber AS "Flight Number",
            f.DepartureTime AS "Departure Time",
            f.DestinationArrivalTime AS "Destination Arrival Time",
            f.FlightStatus AS "Flight Status",
            d.AirportCode AS "Destination Airport Code",
            d.AirportName AS "Destination Airport Name",
            d.City AS "Destination City",
            d.Country AS "Destination Country",
            d.Terminal AS "Destination Terminal"
        FROM Flight AS f
        LEFT JOIN Destination AS d
            ON f.DestinationAirportId = d.DestinationId
        WHERE 1=1
    """

    # Augment the template SQL query based on the specified criteria.
    if destination_airport_code:
        template_sql_query_for_viewing_flights += " AND d.AirportCode = ? COLLATE NOCASE"
    if departure_datetime:
        template_sql_query_for_viewing_flights += " AND f.DepartureTime = ?"
    if flight_status:
        template_sql_query_for_viewing_flights += " AND f.FlightStatus = ?"
    
    filtered_table_rows = conn.execute(template_sql_query_for_viewing_flights, criteria_list).fetchall()
    pretty_printing_flight_information(filtered_table_rows)

# ==============================================================
# update_flight_information() - Function allows the user to update flight information (e.g., departure date and/or status) in the database.
# ==============================================================
def update_flight_information(conn: sqlite3.Connection) -> None:
    """
    Function allows the user to update flight information (e.g., departure date and/or status) in the database.
    """
    flight_number = get_non_empty_input("\nEnter the flight number to update(e.g., AA123): ")

    available_flight_information = conn.execute(
        "SELECT FlightNumber, DepartureTime, FlightStatus, FlightId FROM Flight WHERE FlightNumber = ? COLLATE NOCASE;",
        (flight_number,)
    ).fetchone()

    # Check if the Flight Number provided by the users exists in the database.
    if not available_flight_information:
        print("\tFlight not found. Please, try again.")
        return
    
    # Display information about the flight.
    print("\n\tFlight information:")
    print(f"\t\tFlight number: {available_flight_information[0]}")
    print(f"\t\tDeparture Time: {available_flight_information[1]}")
    print(f"\t\tFlight Status: {available_flight_information[2]}")

    # Get new Departure Time and/or Flight Status.
    # TODO: Introduce validity check for the new Departure Time.
    new_departure_time = input("\n\tEnter new Departure Time (e.g., 2026-02-01 10:30) or press Enter to skip: ").strip()

    # TODO: Introduce validity check for the new Flight Status.
    new_flight_status = input(f"\tEnter new Flight Status (e.g., (SCHEDULED, DELAYED, CANCELLED, DEPARTED, ARRIVED)) or press Enter to skip: ").strip().upper()

    updates = []
    params_for_updates = []

    if new_departure_time:
        updates.append("DepartureTime = ?")
        params_for_updates.append(new_departure_time)
    if new_flight_status:
        updates.append("FlightStatus = ?")
        params_for_updates.append(new_flight_status)
    
    if not updates:
        print("\t\tNo new information provided. Flight information remains unchanged.")    
        return
    else:
        params_for_updates.append(available_flight_information[3]) # FlightId for the WHERE-clause
    
    # Update the Flight Information.
    try:
        with conn:
            conn.execute(
                f"UPDATE Flight SET {', '.join(updates)} WHERE FlightId = ?;",
                params_for_updates,
            )
    except sqlite3.IntegrityError as e:
        print(f"Error. Update failed: {e}")
    
    # Display the updated flight information.
    updated_flight_information = conn.execute(
        "SELECT FlightNumber, DepartureTime, FlightStatus, FlightId FROM Flight WHERE FlightNumber = ? COLLATE NOCASE;",
        (flight_number,)
    ).fetchone()
    
    # Display information about the flight.
    print("\n\tUpdated Flight information:")
    print(f"\t\tFlight number: {updated_flight_information[0]}")
    print(f"\t\tDeparture Time: {updated_flight_information[1]}")
    print(f"\t\tFlight Status: {updated_flight_information[2]}")

# ==============================================================
# assign_pilot_to_flight() - Function allows the user to assign a pilot to a flight.
# ==============================================================
def assign_pilot_to_flight(conn: sqlite3.Connection) -> None:
    """Function allows the user to assign a pilot to a flight."""
    print("\nTo assign a pilot to a flight, please provide the below information.")
    
    # Take the pilot's license number and check that it exists in the database.
    license_number = get_non_empty_input("\tPilot License Number (e.g., LIC-UK-7Q2A91): ").upper()
    pilot_information = conn.execute("SELECT LicenseNumber, FirstName, LastName, IsActive, PilotId FROM Pilot WHERE LicenseNumber = ? COLLATE NOCASE;", 
                                     (license_number,)
                                     ).fetchone()
    if not pilot_information:
        print("\t\tLicense Number not found. Please, try again.")
        return  

    # Check if the pilot has an active employment status.
    if not pilot_information[3]: # IsActive column
        print("\t\tPilot does not have an active employment status. Please, try again.")
        return
    
    # Take the flight number and check that it exists in the database.
    flight_number = get_non_empty_input("\nEnter the flight number to update(e.g., AA123): ")
    available_flight_information = conn.execute(
        "SELECT FlightNumber, DepartureTime, FlightStatus, FlightId FROM Flight WHERE FlightNumber = ? COLLATE NOCASE;",
        (flight_number,)
    ).fetchone()
    if not available_flight_information:
        print("\tFlight not found. Please, try again.")
        return

    # Assign the pilot to the flight.
    try:
        with conn:
            conn.execute(
                "INSERT INTO Flight_Pilot(FlightId, PilotId) VALUES (?, ?);",
                (available_flight_information[3], pilot_information[4]),
            )
        print(f"\t\tPilot {pilot_information[0]} assigned to flight {available_flight_information[0]} successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Assignment failed (maybe duplicate assignment): {e}")

# ==============================================================
# view_pilot_schedule() - Function allows the user to view a selected pilot's schedule.
# ==============================================================
def view_pilot_schedule(conn: sqlite3.Connection) -> None:
    """Function allows the user to view a selected pilot's schedule."""
    print("\nTo view a pilot's schedule, please provide the below information.")

    license_number = get_non_empty_input("\tPilot License Number (e.g., LIC-UK-7Q2A91): ").upper()

    # Check if the License Number exists in the database.
    pilot_information = conn.execute("SELECT LicenseNumber, FirstName, LastName FROM Pilot WHERE LicenseNumber = ? COLLATE NOCASE;", 
                                     (license_number,)
                                     ).fetchone()

    # Check if the Flight Number provided by the users exists in the database.
    if not pilot_information:
        print("\t\tLicense Number not found. Please, try again.")
        return   

    # Get the pilot's schedule.
    pilot_schedule = conn.execute(
        """
        SELECT
          p.LicenseNumber as "License Number",
          p.FirstName || ' ' || COALESCE(p.MiddleName || ' ', '') || p.LastName AS "Pilot Name",
          f.FlightNumber,
          da.AirportCode AS DepartureAirport,
          aa.AirportCode AS DestinationAirport,
          f.DepartureTime,
          f.DestinationArrivalTime,
          f.FlightStatus
        FROM Pilot AS p
        LEFT JOIN Flight_Pilot AS fp 
            ON fp.PilotId = p.PilotId
        LEFT JOIN Flight AS f 
            ON f.FlightId = fp.FlightId
        LEFT JOIN Destination AS da 
            ON da.DestinationId = f.DepartureAirportId
        LEFT JOIN Destination AS aa 
            ON aa.DestinationId = f.DestinationAirportId
        WHERE p.LicenseNumber = ?
        ORDER BY f.DepartureTime ASC;
        """,
        (license_number,),
    ).fetchall()                                 

    # Display the pilot's schedule.
    headers = ["License Number", "Pilot Name", "Flight Number", "Departure Airport", "Destination Airport", "Departure Time", "Destination Arrival Time", "Flight Status"]
    print_table(pilot_schedule, headers)

# ==============================================================
# additional_summary_queries() - Function produces additional summary queries on the created data.
# ==============================================================
def additional_summary_queries(conn: sqlite3.Connection) -> None:
    """Function produces additional summary queries on the created data."""
    print("\nSummary Information.")

    # Number of flight to each destination
    print("\n1) Number of flights to each destination")
    n_flights_to_each_destination = conn.execute(
        """
        SELECT
          d.AirportCode,
          d.City,
          d.Country,
          COUNT(*) AS FlightsToDestination
        FROM Flight AS f
        LEFT JOIN Destination AS d 
            ON d.DestinationId = f.DestinationAirportId
        GROUP BY d.DestinationId
        ORDER BY FlightsToDestination DESC, d.AirportCode ASC;
        """
    ).fetchall()
    print_table(n_flights_to_each_destination, ["Airport Code", "City", "Country", "Flights To Destination"])

    # Number of flights assigned to each pilot
    print("2) Number of flights assigned to each pilot")
    n_flights_assigned_to_pilot = conn.execute(
        """
        SELECT
          p.LicenseNumber,
          p.FirstName || ' ' || COALESCE(p.MiddleName || ' ', '') || p.LastName AS PilotName,
          COUNT(fp.FlightId) AS AssignedFlights
        FROM Pilot AS p
        LEFT JOIN Flight_Pilot AS fp 
            ON fp.PilotId = p.PilotId
        GROUP BY p.PilotId
        ORDER BY AssignedFlights DESC, p.LicenseNumber ASC;
        """
    ).fetchall()
    print_table(n_flights_assigned_to_pilot, ["License Number", "Pilot Name", "Assigned Flights"])

# ==============================================================
# Main Logic of the program
# ==============================================================
def main() -> None:
    """Main function that initialises the Flight Management database and launches the CLI for user interaction."""
    with connect_db() as conn:
        initialise_db(conn)
        populate_db(conn)

    # Menu interface options
    menu = {
        "0": ("Exit", None),
        "1": ("Add a New Flight", add_new_flight),
        "2": ("View Flights by Criteria", view_flights_by_criteria),
        "3": ("Update Flight Information", update_flight_information),
        "4": ("Assign Pilot to Flight", assign_pilot_to_flight),
        "5": ("View Pilot Schedule", view_pilot_schedule),
        "6": ("Additional Summary Queries", additional_summary_queries),
    }

    # Display menu options
    while True:
        print("="*50)
        print("Flight Management System Menu:")
        print("="*50)

        # Print the sorted menu options
        for k in sorted(menu.keys()):
            print(f"\t{k}. {menu[k][0]}")
        
        print("="*50)

        # Get user input
        choice = input("\nPlease, select one of the above options (0-7): ").strip()

        # Specify user interaction logic for each menu option
        if choice == "0":
            print("\nTerminating the session. Goodbye!\n")
            break
        
        command = menu.get(choice)
        if not command:
            print(f"\nInvalid menu option selected: {choice}. Please, try again.\n")
            continue

        # Execute user-selected command
        command[1](conn)

if __name__ == "__main__":
    main()
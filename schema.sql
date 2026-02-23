PRAGMA foreign_keys = ON;

-- ========================================================================
-- Flight table
-- ========================================================================
CREATE TABLE IF NOT EXISTS Flight (
    FlightId                    INTEGER PRIMARY KEY AUTOINCREMENT,
    FlightNumber                TEXT NOT NULL UNIQUE,
    AircraftId                  INTEGER NOT NULL, 
    DepartureAirportId          INTEGER NOT NULL, 
    DestinationAirportId        INTEGER NOT NULL, 
    DepartureTime               TEXT NOT NULL, 
    DestinationArrivalTime      TEXT NOT NULL, 
    FlightStatus                TEXT NOT NULL CHECK (FlightStatus IN ('SCHEDULED', 'DELAYED', 'CANCELLED', 'DEPARTED', 'ARRIVED')
    ),

    FOREIGN KEY (AircraftId) REFERENCES Aircraft(AifcraftId) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (DepartureAirportId) REFERENCES Destination(DestinationId) ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (DestinationAirportId) REFERENCES Destination(DestinationId) ON UPDATE CASCADE ON DELETE RESTRICT
);

-- ========================================================================
-- Pilot table
-- ========================================================================
CREATE TABLE IF NOT EXISTS Pilot (
    PilotId                     INTEGER PRIMARY KEY AUTOINCREMENT, 
    LicenseNumber               TEXT NOT NULL UNIQUE, 
    FirstName                   TEXT NOT NULL,
    MiddleName                  TEXT,
    LastName                    TEXT NOT NULL,
    MobilePhone                 TEXT,
    Email                       TEXT,
    EmploymentStartDate         TEXT NOT NULL,
    EmploymentEndDate           TEXT NOT NULL,
    IsActive                    INTEGER NOT NULL DEFAULT 1 CHECK (IsActive IN (0, 1))
);

-- ========================================================================
-- Flight_Pilot table
-- ========================================================================
CREATE TABLE IF NOT EXISTS Flight_Pilot (
    FlightId        INTEGER NOT NULL,
    PilotId         INTEGER NOT NULL,

    PRIMARY KEY (FlightId, PilotId),

    FOREIGN KEY (FlightId) REFERENCES Flight(FlightId) ON DELETE CASCADE,
    FOREIGN KEY (PilotId) REFERENCES Pilot(PilotId) ON DELETE RESTRICT
);

-- ========================================================================
-- Aircraft table
-- ========================================================================
CREATE TABLE IF NOT EXISTS Aircraft (
    AircraftId          INTEGER PRIMARY KEY AUTOINCREMENT,
    Model               TEXT NOT NULL,
    PassengerCapacity   INTEGER NOT NULL,
    BuiltDate           TEXT NOT NULL,
    LastCheckDate       TEXT NOT NULL
);

-- ========================================================================
-- Destination table
-- ========================================================================
CREATE TABLE IF NOT EXISTS Destination (
    DestinationId       INTEGER PRIMARY KEY AUTOINCREMENT,
    AirportCode         TEXT NOT NULL UNIQUE,
    AirportName         TEXT NOT NULL,
    City                TEXT NOT NULL,
    Country             TEXT NOT NULL,
    Terminal
);

-- ========================================================================
-- Possible further improvements
-- ========================================================================
/*
1. Add indices on the frequently queried columns for more efficient queries
*/
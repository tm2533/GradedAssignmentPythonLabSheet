-- ========================================================================
-- Description
-- ========================================================================
/*
SQL queries below are used to verify that it is possible to query the created database.
*/

-- ========================================================================
-- Queries
-- ========================================================================
. schema

-- Verify that the tables were created successfully.
SELECT * FROM Flight LIMIT 5;
SELECT * FROM Pilot LIMIT 5;
SELECT * FROM Flight_Pilot LIMIT 5;
SELECT * FROM Aircraft LIMIT 5;
SELECT * FROM Destination LIMIT 5;

-- If the user added a new flight, use the query below to verify that the new flight was added successfully.
SELECT * FROM Flight WHERE FlightId > 15 ORDER BY FlightId;
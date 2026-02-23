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

SELECT * FROM Flight LIMIT 5;
SELECT * FROM Pilot LIMIT 5;
SELECT * FROM Flight_Pilot LIMIT 5;
SELECT * FROM Aircraft LIMIT 5;
SELECT * FROM Destination LIMIT 5;
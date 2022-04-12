-- This script drops all tables in the database (but not the database itself)
-- To run it:
-- 1. cd into this dir
-- 2. mysql -u root -p 
-- 3. Enter password
-- 4. SOURCE dropAllTables.sql

SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS Visitors;
DROP TABLE IF EXISTS Places;
DROP TABLE IF EXISTS PlaceOwners;
DROP TABLE IF EXISTS Agents;
DROP TABLE IF EXISTS Hospitals;
DROP TABLE IF EXISTS PlacesVisited;
SET FOREIGN_KEY_CHECKS = 1;
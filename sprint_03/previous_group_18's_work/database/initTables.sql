-- !! REPLACE WITH MySQL DATABASE IF ALTERNATE NAME IS WANTED !!
CREATE DATABASE IF NOT EXISTS Group18;
USE Group18;

-- Citizens or visitors will use the web service to indicate whether they have
-- entered a particular place and when they have done so.
CREATE TABLE IF NOT EXISTS Visitors
(
    VisitorID INT NOT NULL AUTO_INCREMENT, -- primary key column
    VisitorName VARCHAR(64) NOT NULL,
    VisitorAddress VARCHAR(128) NOT NULL,
    VisitorPhoneNumber VARCHAR(20),
    VisitorEmail VARCHAR(128),
    VisitorDeviceID VARCHAR(128) NOT NULL,

    -- Marks whether the person is infected (1) or not infected (0)
    infected BOOLEAN DEFAULT 0,

    -- login details
    VisitorUsername VARCHAR(64) NOT NULL,
    VisitorPassword VARCHAR(256) NOT NULL,

    PRIMARY KEY (VisitorID),

    -- Ensure either phone number or email is given
    CONSTRAINT ensure_contact
        CHECK(NOT(VisitorEmail IS NULL AND VisitorPhoneNumber IS NULL))
);

-- No login functionality
CREATE TABLE IF NOT EXISTS PlaceOwners
(
    PlaceOwnerID INT NOT NULL AUTO_INCREMENT, -- primary key column
    PlaceOwnerName VARCHAR(128) NOT NULL,
    PlaceOwnerPhoneNumber VARCHAR(20),
    PlaceOwnerEmail VARCHAR(64),
    
    PRIMARY KEY (PlaceOwnerID),

    -- Ensure either phone number or email is given
    CONSTRAINT ensure_contact
        CHECK(NOT(PlaceOwnerEmail IS NULL AND PlaceOwnerPhoneNumber IS NULL))
);

-- Places which are frequently visited by people, such as clubs, pubs, 
-- restaurants, cinemas etc. Owners will use the web service to get access 
-- to a QR code, which uniquely identifies their place. Citizens will scan 
-- this QR code to record their presence at that place.
CREATE TABLE IF NOT EXISTS Places
(
    PlaceID INT NOT NULL AUTO_INCREMENT, -- primary key column
    PlaceName VARCHAR(64) NOT NULL,
    PlaceAddress VARCHAR(128) NOT NULL,
    QRcode VARCHAR(128),
    -- QR Codes will be created based off of the Place ID.
    -- When a visitor scans the QR code they will be redirected
    -- to the site with the place field filled out. If they 
    -- have an account, they can simply log in

    -- Places have their Owner referenced by a foreign key
    PlacesPlaceOwnerID INT NOT NULL,
    FOREIGN KEY (PlacesPlaceOwnerID) REFERENCES PlaceOwners(PlaceOwnerID),

    PRIMARY KEY (PlaceID)
);

-- The agency or the evaluation client will use the web service to generate 
-- coronarelated reports by collecting data from the database.
CREATE TABLE IF NOT EXISTS Agents
(
    AgentID INT NOT NULL AUTO_INCREMENT, -- primary key column

    -- login details
    AgentUsername VARCHAR(64) NOT NULL,
    AgentPassword VARCHAR(256) NOT NULL,

    PRIMARY KEY (AgentID)
);

-- Hospitals will use the web service to mark people as infected and track 
-- anyone else that has been in contact with an infected person.
CREATE TABLE IF NOT EXISTS Hospitals
(
    HospitalID INT NOT NULL AUTO_INCREMENT, -- primary key column

    -- login details
    HospitalUsername VARCHAR(64) NOT NULL,
    HospitalPassword VARCHAR(256) NOT NULL,

    PRIMARY KEY (HospitalID)
);

-- Places where Visitors visited
CREATE TABLE IF NOT EXISTS PlacesVisited
(
    OccurrenceID INT NOT NULL AUTO_INCREMENT, -- primary key column
    PlaceVisitorID INT NOT NULL,
    PlaceVisitedID INT NOT NULL,

    DeviceID VARCHAR(128),    -- device used to check in

    PRIMARY KEY (OccurrenceID),

    -- TimeExited is allowed to be NULL because it will be edited later
    TimeEntered CHAR(14) NOT NULL,  -- DD/MM/YY,HH:MM
    TimeExited CHAR(14),            -- DD/MM/YY,HH:MM

    FOREIGN KEY (PlaceVisitorID) REFERENCES Visitors(VisitorID),
    FOREIGN KEY (PlaceVisitedID) REFERENCES Places(PlaceID)
);
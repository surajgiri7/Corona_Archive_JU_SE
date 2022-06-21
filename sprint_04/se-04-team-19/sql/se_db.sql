-- !! REPLACE WITH MySQL DATABASE IF ALTERNATE NAME IS WANTED !!
CREATE DATABASE
IF NOT EXISTS se_db;
USE se_db;

-- Citizens or visitors will use the web service to indicate whether they have
-- entered a particular place and when they have done so.
DROP TABLE IF EXISTS User;
CREATE TABLE User
(
  UserID INT NOT NULL
  AUTO_INCREMENT, -- primary key column
  Name VARCHAR
  (64) NOT NULL,
  Address VARCHAR
  (128) NOT NULL,
  PhoneNumber VARCHAR
  (20),
  Email VARCHAR
  (128),
  DeviceID VARCHAR
  (128),

    -- Marks whether the person is infected (1) or not infected (0)
    infected BOOLEAN DEFAULT 0,

    -- login details
    Username VARCHAR
  (64) NOT NULL,
    Password VARCHAR
  (256) NOT NULL,
    UserType VARCHAR
  (50) NOT NULL,
    PRIMARY KEY
  (UserID),
    -- Ensure either phone number or email is given
    CONSTRAINT ensure_contact
        CHECK
  (NOT
  (Email IS NULL AND PhoneNumber IS NULL))
);

  DROP TABLE IF EXISTS Places;
  -- This table has all the places which are registered by place owners
  CREATE TABLE Places
  (
    PlaceID INT NOT NULL
    AUTO_INCREMENT, -- primary key column
    PlaceName VARCHAR
    (64) NOT NULL,
    PlaceAddress VARCHAR
    (128) NOT NULL,
    QRcode VARCHAR
    (128),
    PRIMARY KEY
    (PlaceID)
);

    DROP TABLE IF EXISTS VisitorToPlaces;
    -- This table saves all the visitors at specific places and their entry/exit times
    CREATE TABLE VisitorToPlaces
    (
      -- VisitedPlacesID INT NOT NULL AUTO_INCREMENT,
      Visitor VARCHAR(64),
      Place VARCHAR(128),
      -- UserID INT FOREIGN KEY REFERENCES User(UserID),
      -- PlaceID INT FOREIGN KEY REFERENCES Places(PlaceID),
      EntryDateTime DATETIME,
      ExitDateTime DATETIME,
      infected BOOLEAN
    );


    -- TEST INPUTS
    INSERT INTO User
      (Name,Address,PhoneNumber,Email,Username,Password,infected,Usertype,DeviceID)
    VALUES
      ("Visitor1", "Bremen", "1111", "visitor1@gmail.com", "vv", "vv", 0, "visitor", "01");
    INSERT INTO User
      (Name,Address,PhoneNumber,Email,Username,Password,infected,Usertype,DeviceID)
    VALUES
      ("Visitor1", "Bremen", "1111", "visitor1@gmail.com", "visitor1", "$2b$12$dSK2fQbA9YzBMCo/.gBKLuZyYjm0aoYmQ5UPUm30CgCW.LetR95kC", 0, "visitor", "01");

    INSERT INTO User
      (Name,Address,PhoneNumber,Email,Username,Password,infected,Usertype,DeviceID)
    VALUES
      ("Placeowner1", "Bremen", "2222", "placeowner1@gmail.com", "pp", "pp", 0, "owner", "02");
    INSERT INTO User
      (Name,Address,PhoneNumber,Email,Username,Password,infected,Usertype,DeviceID)
    VALUES
      ("Placeowner1", "Bremen", "2222", "placeowner1@gmail.com", "place1", "$2b$12$bG8LjQH06jIJ9h5bA1FiS.hOhtkL6HAKM5sAYtXNYKyx.MOwfpZmK", 0, "owner", "02");

    INSERT INTO User
      (Name,Address,PhoneNumber,Email,Username,Password,infected,Usertype,DeviceID)
    VALUES
      ("Agent1", "College Ring 7", "1234", "agent1@gmail.com", "agent", "$2b$12$bG8LjQH06jIJ9h5bA1FiS.hOhtkL6HAKM5sAYtXNYKyx.MOwfpZmK", 0, "agent", "000");

    INSERT INTO User
      (Name,Address,PhoneNumber,Email,Username,Password,Usertype,DeviceID)
    VALUES
      ("Hospital1", "College Ring 1", "4321", "hospital1@gmail.com", "hh", "hh", "hospital", "000");
    INSERT INTO User
      (Name,Address,PhoneNumber,Email,Username,Password,Usertype,DeviceID)
    VALUES
      ("Hospital1", "College Ring 1", "4321", "hospital1@gmail.com", "hospital1", "$2b$12$O5hgvJkNPMZ3DMlGp9CG8u8C/2kv2bMs1yfXR0v5lWK0Qm4XAl5Wq", "hospital", "000");


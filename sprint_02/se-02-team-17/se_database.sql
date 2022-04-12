CREATE TABLE Visitor (
    visitor_id INT PRIMARY KEY AUTO_INCREMENT,
    visitor_name CHAR(30) NOT NULL,
    visitor_address CHAR(100) NOT NULL,
    visitor_phone CHAR(30) NOT NULL,
    visitor_email CHAR(30) UNIQUE NOT NULL,
    visitor_password CHAR(30) NOT NULL,
    device_ID CHAR(100) UNIQUE,
    infected TINYINT
);

CREATE TABLE Places (
    place_id INT PRIMARY KEY AUTO_INCREMENT,
    place_name CHAR(50) UNIQUE NOT NULL,
    place_address CHAR(100) NOT NULL,
    place_email CHAR(100) UNIQUE NOT NULL,
    place_password CHAR(30) NOT NULL,
    QRcode CHAR(100) UNIQUE
);

CREATE TABLE Agent (
    agent_id INT PRIMARY KEY AUTO_INCREMENT,
    agent_username CHAR(50) UNIQUE NOT NULL,
    agent_password CHAR(30) NOT NULL
);

CREATE TABLE Hospital (
    hospital_id INT PRIMARY KEY AUTO_INCREMENT,
    hospital_username CHAR(50) UNIQUE NOT NULL,
    hospital_address CHAR(100) NOT NULL,
    hospital_password CHAR(30) NOT NULL
);

CREATE TABLE VisitorToPlaces (
    visit_id INT PRIMARY KEY AUTO_INCREMENT,
    QRcode CHAR(30) NOT NULL,
    device_ID CHAR(30) NOT NULL,
    entry_date DATE,
    entry_time TIME,
    exit_date DATE,
    exit_time TIME,
    FOREIGN KEY(QRcode) REFERENCES Places(QRcode) ON DELETE CASCADE,
    FOREIGN KEY(device_ID) REFERENCES Visitor(device_ID) ON DELETE CASCADE
);

INSERT INTO Visitor (visitor_id, visitor_name, visitor_address, visitor_phone, visitor_email, visitor_password, infected)
VALUES (1, 'First Visitor', 'visitor1 address', '1234567890', 'visitor1@gmail.com', 'password', 0),
       (2, 'Second Visitor', 'visitor2 address', '1234567890', 'visitor2@gmail.com', 'password', 0),
       (3, 'Third Visitor', 'visitor2 address', '1234567890', 'visitor3@gmail.com', 'password', 0);


INSERT INTO Places (place_id, place_name, place_address, place_email, place_password)
VALUES (1, 'First Place', 'place1 address', 'place1@gmail.com', 'password'),
       (2, 'Second Place', 'place2 address', 'place2@gmail.com', 'password'),
       (3, 'Third Place', 'place2 address', 'place3@gmail.com', 'password');

INSERT INTO Agent (agent_id, agent_username, agent_password)
VALUES (1, 'agent1', 'agent_password');

INSERT INTO Hospital (hospital_id, hospital_username, hospital_address, hospital_password)
VALUES (1, 'hospital1', 'hospital1_address', 'password'),
       (2, 'hospital2', 'hospital1_address', 'password'),
       (3, 'hospital3', 'hospital2_address', 'password');


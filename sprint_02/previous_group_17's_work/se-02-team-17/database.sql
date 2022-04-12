CREATE TABLE Visitor (
    visitor_id INT PRIMARY KEY AUTO_INCREMENT,
    visitor_name CHAR(30) NOT NULL,
    v_address CHAR(100) NOT NULL,
    v_phone_number CHAR(30) NOT NULL,
    v_email CHAR(30) UNIQUE,
    device_ID CHAR(100) UNIQUE,
    infected TINYINT
);

CREATE TABLE Places (
    place_id INT PRIMARY KEY AUTO_INCREMENT,
    place_name CHAR(50) UNIQUE NOT NULL,
    place_address CHAR(100) NOT NULL,
    QRcode CHAR(30) UNIQUE
);

CREATE TABLE Agent (
    agent_id INT PRIMARY KEY AUTO_INCREMENT,
    agent_username CHAR(50) UNIQUE,
    agent_password CHAR(30) NOT NULL
);

CREATE TABLE Hospital (
    hospital_id INT PRIMARY KEY AUTO_INCREMENT,
    hospital_username CHAR(50) UNIQUE,
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

INSERT INTO Visitor (visitor_id, visitor_name, v_address, v_phone_number, v_email, device_ID, infected)
VALUES (1, 'Jack Smith', 'Ansgarstr 4, Wallenhorst, 49134', '4917656785634', 'jack.smith@gmail.com', '4352cef119', 0),
       (2, 'Megi Dervishi', 'Ochsenweg 54, Melle, 49324', '3558912367', 'devishimegi@gmail.com', '7056dgh333', 0),
       (3, 'Roberto Garcia', 'Antwerpener Str. 47, Berlin, 13353', '4917658591234', 'garcia.roberto1@gmail.com', '1026jep454', 0),
       (4, 'Aadil Bakir', 'Am Papelor 17, Cobbenrode, 59889', '4056728593', 'aadil_bakir@gmail.com', '3782bcf845', 0),
       (5, 'William Jackson', 'Sudweg 3, Glandorf, 49219', '3556891234', 'williamjackson@gmail.com', '0711afg833', 0),
       (6, 'Alex Silva', 'Iburger Str. 4, Bad Laer, 49196', '38690546723', 'alex.silva@gmail.com', '7626olt139', 0),
       (7, 'Kimberly Ramos', 'Burgunderstr. 8, Singen, 75196', '21290764893', 'kimberly.ramos@gmail.com', '5788yfr331', 0),
       (8, 'Hiroto Nakamura', 'Sudring 25, Emsdetten, 48282', '4987501235', 'nakamura_hiroto@gmail.com', '4209zzn710', 0),
       (9, 'Sofia Weber', 'Schafers Garten 14, Frankfurt Am Main, 60431', '9176593025', 'sofiaweber10@gmail.com', '6928hxi002', 0),
       (10, 'Noah Neverson', 'Dammkuhlenweg 1, Glandorf, 49219', '2015783924', 'n_neverson333@gmail.com', '8356wqs501', 0),
       (11, 'John Ferguson', 'Fasanenstrasse 6, Hamburg, 21033', '0401316133', 'john.ferguson@gmail.com', '5341hrk777', 0),
       (12, 'Paula Reyes', 'Guentzelstrasse 9, Baden-Wurttemberg, 74632', '0662118314', 'p.reyes@gmail.com', '0932gpa671', 0),
       (13, 'Elijah Fisher', 'Charlottenstrasse 19, Brandenburg, 03048', '0355389096', 'fisher.elijah@gmail.com', '7238sxy114', 0),
       (14, 'Patricia Hamilton', 'Jahnstrasse 40, Birnbach, 84419', '08082362365', 'patricia_ham@gmail.com', '5407yfs101', 0),
       (15, 'Jennifer Johnson', 'Gotthardstrasse 41, Kirchheim, 97268', '0361685362', 'jenniferjohnson@gmail.com', '3751wog740', 0),
       (16, 'Bruna Pereira', 'Gruenauer Strasse 73, Lauenburg, 21473', '04153306010', 'bruno.pereiraaa@gmail.com', '9640ffd519', 0),
       (17, 'Daniela Pires', 'Mohrenstrasse 37, Berlin, 10117', '493045185800', 'piresdaniela@gmail.com', '7391tcd883', 0),
       (18, 'Maria Santos', 'Zweibruckenstrasse 12, Munich, 80331', '498921950175', 'maria_santos@gmail.com', '6329bhrhzq', 0),
       (19, 'Steven Loos', 'Grimnitzer Str 11, Joachimsthal, 16247', '35569414054', 'steven3loos@gmail.com', '5742zyp633', 0),
       (20, 'Franco Seifert', 'Bergstrasse 10, Hamburg, 21033', '2268745113', 'f_seifert@gmail.com', '6904tqs617', 0);

INSERT INTO Agent (agent_id, agent_username, agent_password)
VALUES (1, 'agent1234', 'corona_statistics1');

INSERT INTO Hospital (hospital_id, hospital_username, hospital_password)
VALUES (1, 'Johns_Hopkins_Hospital', 'hospital_hopkins1'),
       (2, 'Alpha_Health_Hospital', 'alphahealth777'),
       (3, '24hr_Service_Clinic', 'service_clinic!');


USE Group18

INSERT INTO Visitors SET
    VisitorName = 'John Doe',
    VisitorAddress = 'College Ring 1, 28759 Bremen',
    VisitorPhoneNumber = '+49 123 4567 8910',
    VisitorDeviceID = 103549754023,
    VisitorUsername = 'jdoetheguy',
    VisitorPassword = 'plaintextpassword';

INSERT INTO Visitors SET
    VisitorName = 'Testing Testing',
    VisitorAddress = 'College Ring 1, 28759 Bremen',
    -- leave VisitorPhoneNumber blank for testing
    VisitorEmail = "test@test.com",
    VisitorDeviceID = 123,
    VisitorUsername = 'test',
    VisitorPassword = 'test';

INSERT INTO PlaceOwners SET
    PlaceOwnerName = 'abde ez',
    PlaceOwnerPhoneNumber = '+49 123 4222 8910';

INSERT INTO Places SET
    PlaceName = 'Espace Hassan',
    PlaceAddress = 'College Ring 2, 28759 Bremen',
    PlacesPlaceOwnerID = 1;

INSERT INTO Agents SET
    AgentUsername = 'admin',
    AgentPassword = 'password';

INSERT INTO Hospitals SET
    HospitalUsername = 'beauzart',
    HospitalPassword = 'abcdzz';

INSERT INTO PlacesVisited SET
    PlaceVisitorID = 1,
    PlaceVisitedID = 1,
    DeviceID = 212,
    TimeEntered = '05/12/22,15:22',
    TimeExited = '05/12/22,15:45';
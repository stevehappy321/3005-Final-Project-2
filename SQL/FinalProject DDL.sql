CREATE TABLE IF NOT EXISTS Members (
    MemberID SERIAL Primary Key,
    FirstName   varchar(150) NOT NULL,
    LastName    varchar(150)  NOT NULL,
    Address     TEXT NOT NULL,
    City        varchar(50) NOT NULL,
    PhoneNumber varchar(150) NOT NULL,
    Email       TEXT UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS FitnessStuffs (
    MemberID INT PRIMARY KEY,
    DistanceRunningGoal  varchar(50),
    FastestLapGoal       varchar(50),
    BenchPressGoal       INT,
	SquatGoal            INT,
	SwimmingDistanceGoal INT,
	CurrentRunDistance	 varchar(50),
	CurrentFastestLap	 varchar(50),
    CurrentBenchPress	 INT,
	CurrentSquat		 INT,
	CurrentSwimDistance	 INT,
    FOREIGN KEY (MemberID) 
    REFERENCES Members (MemberID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS HealthStuffs (
    MemberID INT PRIMARY KEY,
    MeasurementDate     DATE,
    Weight              DECIMAL(5, 2),
    BloodPressure       varchar(50),
    HeartRate           INT,
	WeightGoal          DECIMAL(5, 2),
	HeartRateGoal       INT,
    FOREIGN KEY (MemberID) 
    REFERENCES Members (MemberID) ON DELETE CASCADE
);
-- 1 to 1 with member
CREATE TABLE IF NOT EXISTS Payment (
    MemberID INT PRIMARY KEY,
    PaymentDate     DATE,
    AmountPayed     DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
	AmountOwed      DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    PaymentMethod   varchar(20),
    FOREIGN KEY (MemberID) 
    REFERENCES Members (MemberID) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS FitnessRoutine (
    MemberID INT PRIMARY KEY,
    LastUpdated     DATE NOT NULL,
    Routine         Text,
    FOREIGN KEY (MemberID) 
    REFERENCES Members (MemberID) ON DELETE CASCADE
);

--Maybe remove address
CREATE TABLE IF NOT EXISTS Trainers (
    TrainerID SERIAL Primary Key,
    FirstName   varchar(150) NOT NULL,
    LastName    varchar(150) NOT NULL,
    Address     TEXT NOT NULL,
    City        varchar(50) NOT NULL,
    PhoneNumber varchar(150) NOT NULL,
    Email       Text UNIQUE  NOT NULL,
    StartTime   TIME,
    EndTime     TIME
);

CREATE TABLE IF NOT EXISTS Rooms (
    RoomID      SERIAL PRIMARY KEY,
    Name        Text NOT NULL,
    Capacity    INT NOT NULL,
    Type        varchar(150)
);
-- many to many with room
CREATE TABLE IF NOT EXISTS Equipment (
    EquipmentID SERIAL PRIMARY KEY,
    Name varchar        (255) NOT NULL,
    Type varchar        (100) NOT NULL,
    PurchaseDate        DATE NOT NULL,
    Condition           varchar(100) NOT NULL,
    RoomID              INT,
    FOREIGN KEY (RoomID) 
    REFERENCES Rooms(RoomID) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS FitnessClass (
    ClassID         SERIAL PRIMARY KEY,
    ClassName       varchar(150) NOT NULL,
    TrainerID       INT NOT NULL,
    RoomID          INT,
    ClassDate       DATE NOT NULL,
	SessionTime     TIME NOT NULL,
    EndTime         TIME NOT NULL,
	Cost            varchar(10),
    Capacity        INT NOT NULL,
    FOREIGN KEY (TrainerID) 
    REFERENCES Trainers (TrainerID) ON DELETE CASCADE,
    FOREIGN KEY (RoomID) 
    REFERENCES Rooms (RoomID) ON DELETE SET NULL
);
-- needed for one to many 
CREATE TABLE IF NOT EXISTS ClassMembers (
    ClassID     INT NOT NULL,
    MemberID    INT NOT NULL,
    FOREIGN KEY (ClassID) 
    REFERENCES FitnessClass (ClassID) ON DELETE CASCADE,
    FOREIGN KEY (MemberID) 
    REFERENCES Members (MemberID) ON DELETE CASCADE,
    PRIMARY KEY (ClassID, MemberID)
);
-- 1 to 1 relation with member trainer
CREATE TABLE IF NOT EXISTS PrivateSession (
    SessionID   SERIAL PRIMARY KEY,
    TrainerID   INT NOT NULL,
    MemberID    INT NOT NULL,
    RoomID      INT,
    SessionDate DATE NOT NULL,
	SessionTime TIME NOT NULL,
    EndTime     TIME NOT NULL,
	Cost        varchar(10),
    FOREIGN KEY (TrainerID) 
    REFERENCES Trainers (TrainerID),
    FOREIGN KEY (MemberID) 
    REFERENCES Members (MemberID),
    FOREIGN KEY (RoomID) 
    REFERENCES Rooms (RoomID) ON DELETE SET NULL
);
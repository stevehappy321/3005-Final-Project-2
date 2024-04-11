--Inserts
INSERT INTO Members (FirstName, LastName, Address, City, PhoneNumber, Email) VALUES 
('Jane', 'Doe', '123 Tree Court', 'Springfield', '111-555-6789', 'jdoe@hotmail.com'),
('Ryan', 'Mastin', '323 Mallard Avenue', 'Burlington', '905-555-6789', 'rmastin@gmail.com'),
('Steven', 'Wu', '124 Blue Avenue', 'Markham', '222-333-4444', 'SteveWu@gmail.com');

--addr is the gym address
INSERT INTO Trainers (FirstName, LastName, Address, City, PhoneNumber, Email, StartTime, EndTime) VALUES 
('Alice', 'Smith', '456 Boat Road', 'Ottawa','111-565-1234', 'a.smith@gym.com', '09:00:00', '16:00:00'),
('Trainer2', 'Two', '456 Boat Road', 'Ottawa','111-655-1235', 'TrainerTwo@gym.com', '08:00:00', '18:00:00'),
('Snorp', 'Swind', '456 Boat Road', 'Ottawa','111-556-1234', 's.swind@gym.com', '09:00:00', '17:00:00');

--Empty room will be empty, others occupied
INSERT INTO Rooms (Name, Capacity, Type) VALUES 
('Yoga Studio', 11, 'Yoga'),
('Weight Room', 13, 'Weight Training'),
('Private Session Studio', 20, 'Sectioned Room for PrivateSessions'),
('Main Hall', 100, 'Event Hall For Grand Occasions'),
('Empty Room', 12, 'Room thats empty');

--Conditions dont nessecarily align with purchase date - fyi
INSERT INTO Equipment (Name, Type, PurchaseDate, Condition, RoomNumber, LastMaintenance) VALUES 
('Yoga Mats', 'Yoga Equipment', '2023-02-12', 'New', 1, '2022-02-12'),
('Weight set 1', 'Weights', '2023-01-15', 'Old', 2, '2022-02-12'),
('Weight set 2', 'Weights', '2023-01-20', 'New', 3, '2022-02-12'),
('StairClimber', 'Cario', '2023-02-03', 'Under Maintenance', 3, CURRENT_DATE),
('Shake Weight', 'Arms', '2023-09-11', 'Under Maintenance', 3, CURRENT_DATE),
('Swimming Pool', 'Utilities', '2023-01-01', 'Old', 4, '2022-02-12');

--random assortment of classes, 0 person class has no capacity, full class will have 1 person registered (Member 2)
INSERT INTO FitnessClass (ClassName, TrainerID, RoomNumber, ClassDate, SessionTime, EndTime, Cost, Capacity) VALUES 
('Morning Meditation', 1, 1, '2024-04-18', '10:00:00', '10:30:00', '10$', 10),
('Full Class', 3, 3, '2024-04-15', '10:00:00', '10:30:00', '10$', 1),
('Afternoon Yoga', 1, 1, '2024-04-20', '13:00:00', '14:30:00', '15$', 8),
('Swim Lessions', 3, 4, '2024-04-12', '8:00:00', '10:00:00', '20$', 6),
('Lifting Class', 2, 2, '2024-04-11', '12:00:00', '12:24:00', '12$', 15),
('0 person Class', 3, 3, '2024-04-28', '10:00:00', '10:30:00', '10$', 0);

--random private session times.
INSERT INTO PrivateSession (TrainerID, MemberID, RoomNumber, SessionDate, SessionTime, EndTime, Cost) VALUES 
(1, 1, 1, '2024-04-16', '10:00:00', '10:30:00', '100$'),
(2, 2, 2, '2024-04-10', '15:00:00', '16:00:00', '100$'),
(3, 3, 3, '2024-04-15', '08:00:00', '10:24:00', '100$');

INSERT INTO ClassMembers (ClassID, MemberID) VALUES 
(1, 1),
(2, 1),
(3, 2),
(4, 3),
(5, 2);

--random values for this, if unrealistic dont blame me :P
INSERT INTO FitnessStuffs (MemberID, MeasurementDate, DistanceRunningGoal, FastestLapGoal, BenchPressGoal, SquatGoal, SwimmingDistanceGoal, CurrentRunDistance, CurrentFastestLap, CurrentBenchPress, CurrentSquat, CurrentSwimDistance) VALUES 
(1, '2024-03-09', '7.5km', '3:00 min/km', 100, 150, 100, '2km', '4:24 min/km', 70, 110, 300),
(2, '2024-03-09', '10km', '5:00 min/km', 120, 200, 150, '7km', '5:30 min/km', 90, 160, 700),
(3, '2024-03-09', '15km', '2:00 min/km', 90, 90, 88, '8km', '3:30 min/km', 85, 111, 200);


INSERT INTO HealthStuffs (MemberID, MeasurementDate, Weight, BloodPressure, HeartRate, WeightGoal, HeartRateGoal, BloodPressureGoal) VALUES 
(1, '2024-03-09', 224.00, '130/83', 71, 172.00, 65, '129/82'),
(2, '2024-03-09', 150.00, '115/75', 75, 140.00, 72, '100/74'),
(3, '2024-03-09', 250.00, '155/94', 80, 200.00, 79, '154/93');

--Each user generally starts with a debit
INSERT INTO Payment (MemberID, PaymentDate, AmountPayed, AmountOwed, PaymentMethod) VALUES
(1, '2023-03-25', 80.00, 100.00, 'Credit Card'),
(2, '2024-03-10', 1.00, 300.00, 'Debit'),
(3, '2024-03-10', 0.00, 2, 'Trading Fur');

INSERT INTO FitnessRoutine (MemberID, LastUpdated, Routine) VALUES
(1, '2024-04-09', '10x Jumping Jack, 30 Squats, 10km run, 40 cruntches'),
(2, '2024-04-09', '11x Jumping Jack, 10 Squats, 10km run, 30 min swim, 10 mins monkey bars'),
(3, '2024-04-09', '50x Supermans, 5 minute plank, 5km run, 1 min sprint, 5 toe touches');
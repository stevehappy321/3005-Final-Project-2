
Functions to Implement:
Member Functions:
1. ~~User Registration~~
2. ~~Profile Management ~~(Updating personal information)~~, (fitness goals), ~~(health metrics)~~
3. ~~Dashboard Display~~ (Displaying exercise routines),  ~~(fitness achievements, health statistics)~~
4. Schedule Management (Scheduling personal training sessions or group fitness classes. The system
must ensure that the trainer is available)

~~Trainer Functions:~~
1. Schedule Management (Trainer can set the time for which they are available.)
    -changes the working hours
2. Member Profile Viewing (Search by Member’s name)
    -search all members that match a given name and display their personal data


~~Administrative Staff Functions:~~
1. Room Booking Management
2. Equipment Maintenance Monitoring
3. Class Schedule Updating
4. Billing and Payment Processing 

~~Login Screen~~

SQL Functions
1. personExists() - Splits the input and checks if the firstname and lastname are in the database
2. getAllSomething() - Selects * From (passed in)
3. addSomething() - Inserts into (passed in)
4. deleteSomething() - Delete From (passed in)
5. UpdateSomething() - Update (passed in)
6. StrictSelect() - (Passed in) *For cases where we have 1-1 search*


**BUGS**
2. QUERIES MUST BE REVIEWED REGARDING TRAINERS FITNESS SESH AND PRIVATE SESH
3. WHEN SOMEONE UPDATES NAME IN PERSONAL INFO IT BREAKS


**Bug Graveyard**
1. ~~In Admin you can keep adding, add buttons~~
2. ~~In Update you can continuously add fields, implement fix from BG#1~~

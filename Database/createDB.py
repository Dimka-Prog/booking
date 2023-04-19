import sqlite3

database = sqlite3.connect("booking.db.sqlite")

database.executescript('''
                    DROP TABLE IF EXISTS Places;
                    CREATE TABLE Places (
                        PlaceID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Floor,
                        PlaceWindow VARCHAR (20)
                    );
                    
                    DROP TABLE IF EXISTS Guests;
                    CREATE TABLE Guests (
                        GuestID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Login VARCHAR(50) NOT NULL,
                        Password VARCHAR(50) NOT NULL,
                        FIO VARCHAR (50) NULL,
                        PhoneNumber VARCHAR (20) NULL
                    );
                    
                    DROP TABLE IF EXISTS Staff;
                    CREATE TABLE Staff (
                        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Login VARCHAR(100) NOT NULL,
                        Password VARCHAR(100) NOT NULL
                    );
                    
                    DROP TABLE IF EXISTS Tables;
                    CREATE TABLE Tables (
                        TableID INTEGER PRIMARY KEY AUTOINCREMENT,
                        TableNumber INT,
                        CountPlaces INT,
                        PlaceID INT,
                        FOREIGN KEY (PlaceID) REFERENCES Places (PlaceID) ON DELETE CASCADE
                    );
                    
                    DROP TABLE IF EXISTS WorkSchedule;
                    CREATE TABLE WorkSchedule(
                        ScheduleID INTEGER PRIMARY KEY AUTOINCREMENT,
                        TimeBegin DATETIME,
                        TimeEnd DATETIME,
                        WorkDate DATE
                    );
                    
                    DROP TABLE IF EXISTS Booking;
                    CREATE TABLE Booking (
                        BookingID INTEGER PRIMARY KEY AUTOINCREMENT,
                        TableID INT,
                        GuestID INT,
                        ScheduleID INT,
                        BookingDate DATETIME,
                        BeginTime VARCHAR (10),
                        EndTime VARCHAR (10),
                        CountPlaces INT, 
                        FOREIGN KEY (TableID) REFERENCES Tables (TableID) ON DELETE CASCADE,
                        FOREIGN KEY (ScheduleID) REFERENCES WorkSchedule (ScheduleID) ON DELETE CASCADE, 
                        FOREIGN KEY (GuestID) REFERENCES Guests (GuestID) ON DELETE CASCADE
                    );
                                        
                    DROP TABLE IF EXISTS BookingHours;
                    CREATE TABLE BookingHours (
                        HourNumber INT
                    );
                    
                    
                    INSERT INTO Places (Floor, PlaceWindow)  VALUES 
                    (1, 'yes'),
                    (1, 'no'),
                    (2, 'yes'),
                    (2, 'no');
                    
                    INSERT INTO Staff (Login, Password) VALUES 
                    ('ivanov.mv@mail.ru', '123456789'),
                    ('anastasya.vs@mail.ru', '987654321');
                    
                    INSERT INTO Tables (TableNumber, CountPlaces, PlaceID)  VALUES
                    (1, 1, 1),
                    (2, 1, 3),
                    (3, 1, 2),
                    (4, 1, 4),
                    (5, 1, 1),
                    (6, 1, 4), 
                    (7, 2, 1),
                    (8, 2, 2),
                    (9, 2, 2),
                    (10, 2, 4),
                    (11, 2, 3),
                    (12, 3, 1),
                    (13, 3, 2),
                    (14, 3, 3),
                    (15, 3, 4),
                    (16, 3, 1),
                    (17, 4, 4),
                    (18, 4, 4),
                    (19, 4, 1),
                    (20, 4, 3),
                    (21, 4, 2),
                    (22, 6, 1),
                    (23, 6, 2),
                    (24, 6, 4),
                    (25, 6, 3),
                    (26, 6, 2),
                    (27, 8, 1),
                    (28, 8, 4),
                    (29, 8, 2),
                    (30, 8, 3);
                    
                    INSERT INTO WorkSchedule (WorkDate, TimeBegin, TimeEnd) VALUES
                    ('2022-10-1', '12:00', '24:00'),
                    ('2022-10-2', '10:00', '23:00'),
                    ('2022-10-3', '10:00', '23:00'),
                    ('2022-10-4', '10:00', '23:00');
                    
                    INSERT INTO BookingHours(HourNumber) VALUES 
                    (1),
                    (2),
                    (3),
                    (4),
                    (5),
                    (6),
                    (7),
                    (8),
                    (9),
                    (10),
                    (11),
                    (12); 
                       ''')

database.commit()
database.close()

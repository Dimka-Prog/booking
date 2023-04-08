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
                        FIO VARCHAR (50),
                        PhoneNumber VARCHAR (20)
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
                        BookingTime VARCHAR (10),
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
                    
                    INSERT INTO Guests (FIO, PhoneNumber) VALUES
                    ('Попов А.А.', '89147594501'),
                    ('Сидоров А.А.', '89147594502'),
                    ('Агапова А.А.', '89147594503'),
                    ('Сазонтова А.А.', '89147594504'),
                    ('Дудко А.А.', '89147594505'),
                    ('Сорокина А.А.', '89147594506'),
                    ('Петров А.А.', '89147594507'),
                    ('Петрова А.А.', '89147594508'),
                    ('Сорокин А.А.', '89147594509'),
                    ('Агапов А.А.', '89147594510'),
                    ('Сидорова А.А.', '89147594511'),
                    ('Якимова А.А.', '89147594512'),
                    ('Круглов А.А.', '89147594513'),
                    ('Иванов А.А.', '89147594514'),
                    ('Калашникова А.А.', '89147594515'),
                    ('Иванова А.А.', '89147594516'),
                    ('Хмелев А.А.', '89147594517'),
                    ('Копийко А.А.', '89147594518'),
                    ('Крючкова А.А.', '89147594519'),
                    ('Калиниченко А.А.', '89147594520'),
                    ('Шастун А.А.', '89147594521'),
                    ('Кузнецов А.А.', '89147594522'),
                    ('Васильева А.А.', '89147594523'),
                    ('Соколова А.А.', '89147594524'),
                    ('Михайлова А.А.', '89147594525'),
                    ('Адеева А.А.', '89147594526'),
                    ('Аксенова А.А.', '89147594527'),
                    ('Горина А.А.', '89147594528'),
                    ('Казанцев А.А.', '89147594529'),
                    ('Емельянов А.А.', '89147594530');
                    
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
                    
                    INSERT INTO Booking (TableID, BookingDate, ScheduleID, BookingTime) 
                    SELECT TableID, WorkDate, ScheduleID, strftime('%H:%M', time(TimeBegin, '+' || 
                           HourNumber || ' hour')) as time
                    FROM Tables, WorkSchedule, BookingHours
                    WHERE WorkDate = '2022-10-1' and TableNumber = 1;
                    
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

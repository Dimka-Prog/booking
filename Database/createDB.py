import sqlite3

database = sqlite3.connect("booking.db.sqlite")

database.executescript('''
                    DROP TABLE IF EXISTS Place;
                    CREATE TABLE Place (
                        place_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        place_floor INT,
                        place_window VARCHAR (20)
                    );
                    
                    DROP TABLE IF EXISTS Guest;
                    CREATE TABLE Guest (
                        guest_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        guest_name VARCHAR (20),
                        guest_phone VARCHAR (20)
                    );
                    
                    DROP TABLE IF EXISTS Desk;
                    CREATE TABLE Desk (
                        desk_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        desk_numb INT,
                        desk_amount INT,
                        place_id INT,
                        FOREIGN KEY (place_id) REFERENCES Place (place_id) ON DELETE CASCADE
                    );
                    
                    DROP TABLE IF EXISTS Schedule;
                    CREATE TABLE Schedule(
                        schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        schedule_time_begin DATETIME,
                        schedule_time_end DATETIME,
                        schedule_date DATE
                    );
                    
                    DROP TABLE IF EXISTS Booking;
                    CREATE TABLE Booking (
                        booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        desk_id INT,
                        guest_id INT,
                        schedule_id INT,
                        booking_date DATETIME,
                        booking_time VARCHAR (10),
                        booking_amount INT, 
                        FOREIGN KEY (desk_id) REFERENCES Desk (desk_id) ON DELETE CASCADE,
                        FOREIGN KEY (schedule_id) REFERENCES Schedule (schedule_id) ON DELETE CASCADE, 
                        FOREIGN KEY (guest_id ) REFERENCES Guest (guest_id) ON DELETE CASCADE
                    );
                                        
                    DROP TABLE IF EXISTS BookingHours;
                    CREATE TABLE BookingHours (
                        numb_numb INT
                    );
                    
                    
                    INSERT INTO Place (place_floor, place_window)  VALUES 
                    (1, 'yes'),
                    (1, 'no'),
                    (2, 'yes'),
                    (2, 'no');
                    
                    INSERT INTO Guest (guest_name, guest_phone) VALUES
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
                    
                    INSERT INTO Desk (desk_numb, desk_amount, place_id)  VALUES 
                    (1, 2, 1),
                    (2, 2, 2),
                    (3, 2, 2),
                    (4, 2, 4),
                    (5, 2, 3),
                    (6, 3, 1),
                    (7, 3, 2),
                    (8, 3, 3),
                    (9, 3, 4),
                    (10, 3, 1),
                    (11, 4, 4),
                    (12, 4, 4),
                    (13, 4, 1),
                    (14, 4, 3),
                    (15, 4, 2),
                    (16, 6, 1),
                    (17, 6, 2),
                    (18, 6, 4),
                    (19, 6, 3),
                    (20, 6, 2),
                    (21, 8, 1),
                    (22, 8, 4),
                    (23, 8, 2),
                    (24, 8, 3),
                    (25, 1, 1),
                    (26, 1, 3),
                    (27, 1, 2),
                    (28, 1, 4),
                    (29, 1, 1),
                    (30, 1, 4);
                    
                    INSERT INTO Schedule (schedule_date, schedule_time_begin, schedule_time_end) VALUES
                    ('2022-10-1', '12:00', '24:00'),
                    ('2022-10-2', '10:00', '23:00'),
                    ('2022-10-3', '10:00', '23:00'),
                    ('2022-10-4', '10:00', '23:00');
                    
                    INSERT INTO Booking (desk_id, booking_date, schedule_id, booking_time) 
                    SELECT desk_id, schedule_date, schedule_id, strftime('%H:%M', time(schedule_time_begin, '+' || 
                           numb_numb || ' hour')) as time
                    FROM Desk, Schedule, BookingHours
                    WHERE schedule_date = '2022-10-1' and desk_numb = 1;
                    
                    INSERT INTO BookingHours(numb_numb) VALUES 
                    (0),
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
                    (11); 
                       ''')

database.commit()
database.close()

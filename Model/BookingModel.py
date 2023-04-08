import Database.connectDB as db


def delete():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute("DELETE FROM Booking")
    connectDB.commit()
    connectDB.close()


def get_date_time_booking():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    date = cursor.execute('''
                            SELECT 
                                BookingDate, 
                                BookingTime 
                            FROM Booking
                           ''').fetchall()
    connectDB.close()
    return date


def get_all_booking():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    all_booking = cursor.execute('''
                            SELECT 
                                BookingDate, 
                                BookingTime, 
                                G.FIO, 
                                D.CountPlaces, 
                                D.TableNumber 
                            FROM Booking B 
                                JOIN Guests G ON B.GuestID = G.GuestID 
                                JOIN Tables D ON B.TableID = D.TableID
                           ''').fetchall()
    connectDB.close()
    return all_booking


def insert_booking(desc_id, quest_id, date, time, amount):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute(f'''
                    INSERT INTO Booking (TableID, GuestID, ScheduleID, BookingDate, BookingTime, CountPlaces) 
                    VALUES ({desc_id}, {quest_id}, 1, '{date}', '{time}', {amount})
                    ''')
    connectDB.commit()
    connectDB.close()


def get_block_time(var_date):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    data = cursor.execute(f'''
                            SELECT BookingTime 
                            FROM Booking 
                            WHERE BookingDate = '{var_date}'
                            ''').fetchall()
    connectDB.close()
    return data

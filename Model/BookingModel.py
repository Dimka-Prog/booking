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


def addBooking(tableID, questID, bookingDate, bookingTime, countPlaces):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute(f'''
                    INSERT INTO Booking (TableID, GuestID, ScheduleID, BookingDate, BookingTime, CountPlaces) 
                    VALUES ({tableID}, {questID}, 1, '{bookingDate}', '{bookingTime}', {countPlaces})
                    ''')
    connectDB.commit()
    connectDB.close()


def get_block_time(bookingDate):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    data = cursor.execute(f'''
                            SELECT BookingTime 
                            FROM Booking 
                            WHERE BookingDate = '{bookingDate}'
                            ''').fetchall()
    connectDB.close()
    return data

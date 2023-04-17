import Database.connectDB as db


def delete():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute("DELETE FROM Booking")
    connectDB.commit()
    connectDB.close()


def getDateTime():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    date = cursor.execute('''
                            SELECT 
                                BookingDate, 
                                BeginTime,
                                EndTime
                            FROM Booking
                           ''').fetchall()
    connectDB.close()
    return date


def getAllBooking():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    allBooking = cursor.execute('''
                            SELECT 
                                BookingDate, 
                                BeginTime,
                                EndTime, 
                                G.FIO, 
                                B.CountPlaces, 
                                T.TableNumber 
                            FROM Booking B
                                JOIN Guests G USING (GuestID)
                                JOIN Tables T USING (TableID)
                            ORDER BY BookingDate, BeginTime
                           ''').fetchall()
    connectDB.close()
    return allBooking


def addBooking(tableID, guestID, bookingDate, beginTime, endTime, countPlaces):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute(f'''
                    INSERT INTO Booking (TableID, GuestID, ScheduleID, BookingDate, BeginTime, EndTime, CountPlaces) 
                    VALUES ({tableID}, {guestID}, 2, '{bookingDate}', '{beginTime}', '{endTime}', {countPlaces})
                    ''')
    connectDB.commit()
    connectDB.close()


def getTime(bookingDate):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    time = cursor.execute(f'''
                            SELECT 
                                BeginTime,
                                EndTime, 
                            FROM Booking 
                            WHERE BookingDate = '{bookingDate}'
                            ''').fetchall()
    connectDB.close()
    return time

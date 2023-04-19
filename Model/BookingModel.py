import Database.connectDB as db


def removeBooking(bookingDate, beginTime, tableNumber):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute(f'''
                    DELETE FROM Booking
                    WHERE TableID = (
                        SELECT TableID 
                        FROM Booking
                            JOIN Tables T USING(TableID)
                        WHERE T.TableNumber = {tableNumber}
                    ) AND 
                          BookingDate = '{bookingDate}' AND
                          BeginTime = '{beginTime}'
                    ''')
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


def getBookingTable(tableID):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    bookingTable = cursor.execute(f'''
                                SELECT  
                                    T.TableNumber 
                                FROM Booking B
                                    JOIN Tables T USING (TableID)
                                WHERE B.TableID = {tableID}
                               ''').fetchone()
    connectDB.close()
    return bookingTable[0]


def getDates():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    dates = cursor.execute(f'''
                            SELECT BookingDate 
                            FROM Booking
                            GROUP BY BookingDate
                            ORDER BY BookingDate
                            ''').fetchall()
    connectDB.close()
    return dates


def getBeginTimes():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    beginTimes = cursor.execute(f'''
                                SELECT BeginTime 
                                FROM Booking
                                GROUP BY BeginTime
                                ORDER BY BeginTime
                                ''').fetchall()
    connectDB.close()
    return beginTimes


def getTableNumbers():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    allTables = cursor.execute(f'''
                                SELECT  
                                    TableNumber 
                                FROM Booking 
                                    JOIN Tables USING (TableID)
                                GROUP BY TableNumber
                                ORDER BY TableNumber
                               ''').fetchall()
    connectDB.close()
    return allTables

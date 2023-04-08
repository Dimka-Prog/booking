import Database.connectDB as db


def getTableLocation(floor, placeWindow):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    placeID = cursor.execute(f'''
                                SELECT PlaceID 
                                FROM Places 
                                WHERE Floor = {floor} AND PlaceWindow = '{placeWindow}'
                                ''').fetchone()
    connectDB.close()
    return placeID[0]


def getCountPlaces():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    countPlaces = cursor.execute('''
                            SELECT CountPlaces
                            FROM Tables
                            GROUP BY CountPlaces
                           ''').fetchall()
    connectDB.close()
    return countPlaces


def getFreeTable(countPlaces, placeID):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    tableID = cursor.execute(f'''
                                SELECT TableID
                                FROM Booking 
                                WHERE TableID = {countPlaces}
                               ''').fetchone()

    if tableID is None:
        tableID = cursor.execute(f'''
                                    SELECT TableID 
                                    FROM Tables 
                                    WHERE CountPlaces = {countPlaces} AND PlaceID = {placeID}
                                   ''').fetchone()

    connectDB.close()
    return tableID[0]

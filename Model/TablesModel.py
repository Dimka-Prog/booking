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
                                FROM Tables T
                                WHERE NOT EXISTS(
                                   SELECT TableID
                                   FROM Booking B
                                   WHERE B.TableID = T.TableID
                                ) AND CountPlaces = {countPlaces} AND PlaceID = {placeID}
                             ''').fetchone()

    connectDB.close()

    if tableID is None:
        return None
    else:
        return tableID[0]

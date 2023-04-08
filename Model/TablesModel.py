import Database.connectDB as db


def get_place(place_floor, place_window):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    place_id = cursor.execute(f'''
                                SELECT PlaceID 
                                FROM Places 
                                WHERE Floor = {place_floor} AND PlaceWindow = '{place_window}'
                                ''').fetchone()
    connectDB.close()
    return place_id[0]


def getDeskAmount():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    deskAmount = cursor.execute('''
                            SELECT CountPlaces
                            FROM Tables
                            GROUP BY CountPlaces
                           ''').fetchall()
    connectDB.close()
    return deskAmount


def select_desk(desk_amount, place_id):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    desc_id = cursor.execute(f'''
                                SELECT TableID
                                FROM Booking 
                                WHERE TableID = {desk_amount}
                               ''').fetchone()

    if desc_id is None:
        desc_id = cursor.execute(f'''
                                    SELECT TableID 
                                    FROM Tables 
                                    WHERE CountPlaces = {desk_amount} AND PlaceID = {place_id}
                                   ''').fetchone()

    connectDB.close()
    return desc_id[0]

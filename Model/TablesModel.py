import Database.connectDB as db


def get_place(place_floor, place_window):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    place_id = cursor.execute(f'''
                                SELECT PLACE_ID 
                                FROM Place 
                                WHERE PLACE_FLOOR = {place_floor} AND PLACE_WINDOW = '{place_window}'
                                ''').fetchone()
    connectDB.close()
    return place_id[0]


def select_desk(desk_amount, place_id):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    desc_id = cursor.execute(f'''
                                SELECT desk_id 
                                FROM Booking 
                                WHERE desk_id = {desk_amount}
                               ''').fetchone()

    if desc_id is None:
        desk_amount += 1
        desc_id = cursor.execute(f'''
                                    SELECT desk_id 
                                    FROM Desk 
                                    WHERE desk_amount = {desk_amount} AND place_id = {place_id}
                                   ''').fetchone()

    connectDB.close()
    return desc_id[0]

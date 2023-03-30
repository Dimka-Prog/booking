def get_place(connectDB, place_floor, place_window):
    cursor = connectDB.cursor()
    place_id = cursor.execute(f'''
                                SELECT PLACE_ID 
                                FROM Place 
                                WHERE PLACE_FLOOR = {place_floor} AND PLACE_WINDOW = '{place_window}'
                                ''').fetchone()
    return place_id[0]


def select_desk(connectDB, desk_amount, place_id):
    cursor = connectDB.cursor()

    desc_id = cursor.execute(f'''
                                SELECT DESk_ID 
                                FROM Booking 
                                WHERE DESk_ID = {desk_amount}
                               ''').fetchone()

    if desc_id is None:
        desk_amount += 1
        desc_id = cursor.execute(f'''
                                    SELECT DESk_ID 
                                    FROM Desk 
                                    WHERE DESk_AMOUNT = {desk_amount} AND PLACE_ID = {place_id}
                                   ''').fetchone()
    return desc_id[0]

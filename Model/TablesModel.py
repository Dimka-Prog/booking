import pandas


def get_place(connectDB, place_floor, place_window):
    place_id = pandas.read_sql(f'''
                                SELECT PLACE_ID 
                                FROM Place 
                                WHERE PLACE_FLOOR = {place_floor} AND PLACE_WINDOW = {place_window}
                                ''', connectDB)
    return place_id[0]


def select_desk(connectDB, desk_amount, place_id):
    desc_id = pandas.read_sql(f'''
                                SELECT DESk_ID 
                                FROM Booking 
                                WHERE DESk_ID = {desk_amount}
                               ''', connectDB)

    if desc_id is None:
        desk_amount += 1
        desc_id = pandas.read_sql(f'''
                                    SELECT DESk_ID 
                                    FROM Desk 
                                    WHERE DESk_AMOUNT = {desk_amount} AND PLACE_ID = {place_id}
                                   ''', connectDB)
    return desc_id[0]
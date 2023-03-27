import pandas


def delete(connectDB):
    cursor = connectDB.cursor()
    cursor.execute("DELETE FROM Booking")
    connectDB.commit()


def get_date_time_booking(connectDB):
    return pandas.read_sql('''
                            SELECT 
                                BOOKING_DATE, 
                                BOOKING_TIME 
                            FROM Booking
                           ''', connectDB)


def get_all_booking(connectDB):
    return pandas.read_sql('''
                            SELECT 
                                BOOKING_DATE, 
                                BOOKING_TIME, 
                                G.GUEST_NAME, 
                                D.DESK_AMOUNT, 
                                D.DESK_NUMB 
                            FROM Booking B 
                                JOIN Guest G ON B.GUEST_ID = G.GUEST_ID 
                                JOIN Desk D ON B.DESK_ID = D.DESK_ID
                           ''', connectDB)


def insert_guest(connectDB, fio, number_phone):
    cursor = connectDB.cursor()
    cursor.execute(f'''
                    INSERT INTO Guest (guest_name, guest_phone) 
                    VALUES ('{fio}', {number_phone})
                    ''')
    connectDB.commit()

    guest_id = pandas.read_sql(f'''
                                SELECT GUEST_ID 
                                FROM Guest 
                                WHERE GUEST_NAME = '{fio}' AND GUEST_PHONE = {number_phone}
                                ''', connectDB)
    return guest_id[0]


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


def insert_booking(connectDB, desc_id, quest_id, date, time, amount):
    cursor = connectDB.cursor()
    cursor.execute(f'''
                    INSERT INTO Booking (DESK_ID, GUEST_ID, schedule_id, BOOKING_DATE, BOOKING_TIME, BOOKING_AMOUNT) 
                    VALUES ({desc_id}, {quest_id}, 1, {date}, {time}, {amount})
                    ''')
    connectDB.commit()


def get_block_time(connectDB, var_date):
    return pandas.read_sql(f'''
                            SELECT booking_time 
                            FROM Booking 
                            WHERE booking_date = {var_date}
                            ''', connectDB)

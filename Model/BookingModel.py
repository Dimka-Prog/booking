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


def insert_booking(connectDB, desc_id, quest_id, date, time, amount):
    cursor = connectDB.cursor()
    cursor.execute(f'''
                    INSERT INTO Booking (DESK_ID, GUEST_ID, schedule_id, BOOKING_DATE, BOOKING_TIME, BOOKING_AMOUNT) 
                    VALUES ({desc_id}, {quest_id}, 1, '{date}', '{time}', {amount})
                    ''')
    connectDB.commit()


def get_block_time(connectDB, var_date):
    return pandas.read_sql(f'''
                            SELECT booking_time 
                            FROM Booking 
                            WHERE booking_date = {var_date}
                            ''', connectDB)

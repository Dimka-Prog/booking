import Database.connectDB as db


def delete():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute("DELETE FROM Booking")
    connectDB.commit()
    connectDB.close()


def get_date_time_booking():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    date = cursor.execute('''
                            SELECT 
                                booking_date, 
                                booking_time 
                            FROM Booking
                           ''').fetchall()
    connectDB.close()
    return date


def get_all_booking():
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    all_booking = cursor.execute('''
                            SELECT 
                                BOOKING_DATE, 
                                BOOKING_TIME, 
                                G.GUEST_NAME, 
                                D.DESK_AMOUNT, 
                                D.DESK_NUMB 
                            FROM Booking B 
                                JOIN Guest G ON B.GUEST_ID = G.GUEST_ID 
                                JOIN Desk D ON B.DESK_ID = D.DESK_ID
                           ''').fetchall()
    connectDB.close()
    return all_booking


def insert_booking(desc_id, quest_id, date, time, amount):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute(f'''
                    INSERT INTO Booking (DESK_ID, GUEST_ID, schedule_id, BOOKING_DATE, BOOKING_TIME, BOOKING_AMOUNT) 
                    VALUES ({desc_id}, {quest_id}, 1, '{date}', '{time}', {amount})
                    ''')
    connectDB.commit()
    connectDB.close()


def get_block_time(var_date):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    data = cursor.execute(f'''
                            SELECT booking_time 
                            FROM Booking 
                            WHERE booking_date = '{var_date}'
                            ''').fetchall()
    connectDB.close()
    return data

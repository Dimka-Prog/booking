import Database.connectDB as db


def insert_guest(fio, number_phone):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute(f'''
                    INSERT INTO Guests (FIO, PhoneNumber) 
                    VALUES ('{fio}', '{number_phone}')
                    ''')
    connectDB.commit()

    guest_id = cursor.execute(f'''
                                SELECT GuestID 
                                FROM Guests 
                                WHERE FIO = '{fio}' AND PhoneNumber = '{number_phone}'
                                ''').fetchone()
    connectDB.close()
    return guest_id[0]

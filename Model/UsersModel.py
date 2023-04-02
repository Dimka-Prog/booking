import Database.connectDB as db


def insert_guest(fio, number_phone):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute(f'''
                    INSERT INTO Guest (guest_name, guest_phone) 
                    VALUES ('{fio}', '{number_phone}')
                    ''')
    connectDB.commit()

    guest_id = cursor.execute(f'''
                                SELECT GUEST_ID 
                                FROM Guest 
                                WHERE GUEST_NAME = '{fio}' AND GUEST_PHONE = '{number_phone}'
                                ''').fetchone()
    connectDB.close()
    return guest_id[0]

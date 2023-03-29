def insert_guest(connectDB, fio, number_phone):
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
    return guest_id[0]

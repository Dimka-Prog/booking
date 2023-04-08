import Database.connectDB as db


def addGuest(fio, phoneNumber):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute(f'''
                    INSERT INTO Guests (FIO, PhoneNumber) 
                    VALUES ('{fio}', '{phoneNumber}')
                    ''')
    connectDB.commit()


def getGuest(fio, phoneNumber):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    guestID = cursor.execute(f'''
                              SELECT GuestID 
                              FROM Guests 
                              WHERE FIO = '{fio}' AND PhoneNumber = '{phoneNumber}'
                             ''').fetchone()
    connectDB.close()
    return guestID[0]

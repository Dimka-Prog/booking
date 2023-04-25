import Database.connectDB as db


def updateGuest(guestID, fio, phoneNumber):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute(f'''
                    UPDATE Guests
                    SET FIO = '{fio}', PhoneNumber = '{phoneNumber}'
                    WHERE GuestID = {guestID}
                    ''')
    connectDB.commit()


def addGuest(login, password):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    cursor.execute(f'''
                    INSERT INTO Guests (Login, Password) VALUES 
                    ('{login}', '{password}')
                    ''')
    connectDB.commit()


def getAuthGuest(login, password):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    authGuest = cursor.execute(f'''
                              SELECT
                                    GuestID,
                                    Login,
                                    Password 
                              FROM Guests 
                              WHERE Login = '{login}' AND Password = '{password}'
                             ''').fetchone()
    connectDB.close()
    return authGuest


def getAuthStaff(login, password):
    connectDB = db.getConnection()
    cursor = connectDB.cursor()

    authStaff = cursor.execute(f'''
                              SELECT
                                    Login,
                                    Password 
                              FROM Staff 
                              WHERE Login = '{login}' AND Password = '{password}'
                             ''').fetchone()
    connectDB.close()
    return authStaff

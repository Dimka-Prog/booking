import os
import sqlite3


def getConnection():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    pathDB = os.path.join(SITE_ROOT, "booking.db.sqlite")

    return sqlite3.connect(pathDB)

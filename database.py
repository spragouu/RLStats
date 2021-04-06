import sqlite3

def dbselect(db, sql, variables):
    """Grab data from DB"""
    db = sqlite3.connect(db)
    cursor = db.execute(sql, variables)
    row = cursor.fetchone()
    cursor.close()
    db.close()

    if row is None:
        pass

    elif len(row) == 1:
        try:
            row = int(row[0])
        except TypeError:
            row = str(row[0])
        except ValueError:
            row = str(row[0])

    else:
        row = list(row)

    return row

def dbupdate(db, sql, variables):
    """Update the existing records or add new records to DB"""
    db = sqlite3.connect(db)
    cursor = db.execute(sql, variables)
    db.commit()
    cursor.close()
    db.close()
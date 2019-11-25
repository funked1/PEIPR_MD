import pymysql

def clear_table(cursor, table):
    sql = "DROP TABLE IF EXISTS {}".format(table)
    cursor.execute(sql)

def make_table(cursor, table, type):
    columns = {
        "channels": """(ch_num INT AUTO_INCREMENT PRIMARY KEY,
                        ch_lbl VARCHAR(255))""",
        "data"    : """(indx INT AUTO_INCREMENT PRIMARY KEY,
                        samples FLOAT,
                        ch_num INT,
                        FOREIGN KEY (ch_num) REFERENCES channels(ch_num)
                        ON DELETE CASCADE)"""
    }

    sql = "CREATE TABLE IF NOT EXISTS {} {}".format(table, columns[type])
    cursor.execute(sql)

def insert_channel(db, cursor, ch_lbl):
    sql = "INSERT INTO channels (ch_lbl) VALUES('{}')".format(ch_lbl)
    cursor.execute(sql)
    db.commit()

def insert_sample(db, cursor, table, sample, key):
    sql = "INSERT INTO {} (samples, ch_num) VALUES({}, {})"
    sql = sql.format(table, sample, key)
    cursor.execute(sql)
    #db.commit()

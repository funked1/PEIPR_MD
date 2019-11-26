import pymysql

def clear_table(cursor, table):
    # function to drop a table within a given database
    sql = "DROP TABLE IF EXISTS {}".format(table)
    cursor.execute(sql)

def make_table(cursor, table, type):
    # function to create a table of type within a given database
    columns = {
        "data": """(indx INT AUTO_INCREMENT PRIMARY KEY,
                    samples FLOAT,
                    ch_num INT,
                    FOREIGN KEY (ch_num) REFERENCES channels(ch_num)
                    ON DELETE CASCADE)""",
        "channels": """(ch_num INT AUTO_INCREMENT PRIMARY KEY,
                        ch_lbl VARCHAR(255))"""
        }
    sql = "CREATE TABLE IF NOT EXISTS {} {}".format(table, columns[type])
    cursor.execute(sql)

def reset_tables(cursor, num_tables):
    # function to old data and creates new empty tables
    data_tables = []
    for i in range(num_tables):
        data_tables.append("data_{}".format(i))
    for table in data_tables:
        clear_table(cursor, table)
    clear_table(cursor, "channels")
    make_table(cursor, "channels", "channels")
    for table in data_tables:
        make_table(cursor, table, "data")


def insert_channel(db, cursor, ch_lbl):
    # function to insert a channel with label ch_lbl into the channels table
    sql = "INSERT INTO channels (ch_lbl) VALUES('{}')".format(ch_lbl)
    cursor.execute(sql)
    db.commit()

def insert_sample(db, cursor, table, sample, key):
    sql = "INSERT INTO {} (samples, ch_num) VALUES({}, {})"
    sql = sql.format(table, sample, key)
    cursor.execute(sql)
    #db.commit()

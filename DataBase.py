import sqlite3 # importing sqlite3 library


with sqlite3.connect('database') as connect: #connect = sqlite3.connect('DataBase/database.db3') # Connecting to the database, if the database does not exist, create a database
        cursor = connect.cursor() # Creating cursor
        cursor.execute('''
                            CREATE TABLE database(
                                ID INTEGER primary key,
                                configuration TEXT,
                                TITLE Text
                            )
                      ''')


connect.close() # break connection with database
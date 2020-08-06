import pymysql

class DBConnect():

    def __init__(self):
        pass

    def __connect(self, db):
        host = '127.0.0.1'
        port = 3306
        conn = pymysql.connect(host=host, port=port, user='root', passwd='mysql', db=db)

        return conn

    def select(self, db, query):
        conn = self.__connect(db)
        cursor = conn.cursor()
        # Execute the query
        cursor.execute(query)
        # Fetch Data
        result = cursor.fetchall()

        all_rows = []
        for line in result:
            row = []
            for col in line:
                row.append(str(col)) #convert each value to string
            all_rows.append(row)

        conn.close() # close the db connection
        cursor.close() # clean the cursor

        return all_rows

    def update(self, db, query):
        conn = self.__connect(db)
        cursor = conn.cursor()

        # Execute the query and commit
        result = cursor.execute(query)
        conn.commit()

        conn.close()
        cursor.close()

        return result





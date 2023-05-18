import pymysql
import pymysql.cursors


# Use this to access database
class Dbconnect:
    def __init__(self) -> None:
        self.connection = pymysql.connect(host='sql9.freemysqlhosting.net',
                                          db='sql9607918', port=3306, user='sql9607918', password='GFQC75Bg2g')
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)

    def select(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)

        result = self.cursor.fetchall()
        return result

    def execute(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        self.connection.commit()

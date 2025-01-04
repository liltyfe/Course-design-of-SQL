import mysql.connector


class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123abc',
            database='studentdb'
        )
        self.cursor = self.conn.cursor()

    def login_check(self, username, password):
        sql = "SELECT * FROM users WHERE username = %s AND passwords = %s"
        val = (username, password)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False

    def insert_data(self, name, ID, mathsc, chinesesc, englishsc):
        sql = "INSERT INTO students (stname, stID, mathsc, chinesessc, englishse) VALUES (%s, %s, %s, %s, %s)"
        val = (name, ID, mathsc, chinesesc, englishsc)
        try:
            self.cursor.execute(sql, val)
            self.conn.commit()
            return True
        except:
            return False

    def show_data(self):
        sql = "SELECT * FROM students"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def select_data_id(self, ID):
        sql = "SELECT * FROM students WHERE stID = %s"
        val = (ID,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        return result

    def select_data_name(self, name):
        sql = "SELECT * FROM students WHERE stname = %s"
        val = (name,)
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        return result

    def delete_data(self, name):
        sql = "DELETE FROM students WHERE stname = %s"
        val = (name,)
        try:
            self.cursor.execute(sql, val)
            self.conn.commit()
            return True
        except:
            return False


if __name__ == '__main__':
    db = Database()
    db.insert_data('Mary', '1234576', 85, 90, 80)
    print(db.show_data())
    db.insert_data('John', '1234577', 90, 85, 80)
    print(db.show_data())
    db.conn.close()

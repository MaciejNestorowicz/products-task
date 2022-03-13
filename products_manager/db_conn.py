from flask_mysqldb import MySQL

class DBConn:


    def __init__(self, app):
        self.app = app


    def make_conn(self):
        self.app.config['MYSQL_HOST'] = 'mysql-db'
        self.app.config['MYSQL_USER'] = 'root'
        self.app.config['MYSQL_PASSWORD'] = 'root'
        self.app.config['MYSQL_DB'] = 'products_db'
        mysql = MySQL(self.app)
        return mysql
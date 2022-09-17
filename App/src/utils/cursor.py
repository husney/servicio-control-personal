
from config import info
import mysql.connector

config = {
    'user' : info["MYSQL_USER"],
    'password' :  info["MYSQL_ROOT_PASSWORD"],
    'host' : info["MYSQL_HOST"],
    'port' : info["PORT_DB_LOCAL"],
    'database' : info["MYSQL_DATABASE"]
}

class Cursor:
    
    def __init__(self):
        self.__db = mysql.connector.connect(**config)
        self.__cursor = None
        
    def __enter__(self):
        try:
            self.__cursor = self.__db.cursor()
            self.__cursor.execute("SET GLOBAL time_zone = '-5:00';")
            return self.__cursor
        except:
            return None
        
    def __exit__(self, exc_type, exc_val, exc_trace):
        try:
            if exc_type:
                pass
                self.__db.rollback()
            else:
                self.__cursor.nextset()
                self.__db.commit()
        except:
            pass
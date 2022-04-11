import psycopg2
from utils.config import pg_config


class UserDAO:
    '''
    Help on the User Data Access Object (DAO)
    TODO: Document
    '''

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (
            pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2.connect(connection_url)


    def get(self):
        cursor = self.conn.cursor()
        query = 'select * from users;'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close
        return result


    def get_by_id(self, id):
        cursor = self.conn.cursor()
        query = 'select * from users where id = %s;'
        cursor.execute(query, ([id]))
        result = cursor.fetchone()
        self.conn.commit()
        return result


    def get_by_uname(self, uname):
        cursor = self.conn.cursor()
        query = 'select * from users where uname = %s;'
        cursor.execute(query, ([uname]))
        result = cursor.fetchone()
        self.conn.commit()
        return result


    def get_by_email(self, email):
        cursor = self.conn.cursor()
        query = 'select * from users where email = %s;'
        cursor.execute(query, ([email]))
        result = cursor.fetchone()
        self.conn.commit()
        return result
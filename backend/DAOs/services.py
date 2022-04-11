import psycopg2
from utils.config import pg_config


class ServiceDAO:
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
        query = 'select * from services;'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close
        return result


    def get_by_id(self, id):
        cursor = self.conn.cursor()
        query = 'select * from services where id = %s;'
        cursor.execute(query, ([id]))
        result = cursor.fetchone()
        self.conn.commit()
        return result


    def get_by_cname(self, cname):
        cursor = self.conn.cursor()
        query = 'select * from services natural inner join utility_companies where company_name = %s;'
        cursor.execute(query, ([cname]))
        result = cursor.fetchone()
        self.conn.commit()
        return result


    def get_by_category(self, uname):
        cursor = self.conn.cursor()
        query = 'select * from services where category = %s;'
        cursor.execute(query, ([uname]))
        result = cursor.fetchone()
        self.conn.commit()
        return result
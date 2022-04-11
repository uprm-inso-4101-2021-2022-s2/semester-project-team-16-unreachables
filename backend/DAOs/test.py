import psycopg2
from utils.config import pg_config


class TestDao:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (
            pg_config['dbname'], pg_config['user'], pg_config['password'], pg_config['host'], pg_config['port'])
        self.conn = psycopg2.connect(connection_url)

    def getTest(self):
        cursor = self.conn.cursor()
        query = 'select * from test;'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.conn.close()
        return result
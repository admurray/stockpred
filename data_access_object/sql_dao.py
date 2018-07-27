import pymysql

from data_access_object.db_config import SQL_DATABASE

class SQLConnector:
    def __init__(self):
        self.hostname = SQL_DATABASE['hostname']
        self.port = SQL_DATABASE['port']
        self.user = SQL_DATABASE['user']
        self.password = SQL_DATABASE['password']
        self.database = SQL_DATABASE['database']

        self.connection = pymysql.connect(host=self.hostname,
                                          port=self.port,
                                          user=self.user,
                                          passwd=self.password,
                                            db=self.database)
        self.cursor = self.connection.cursor()

    def get_all_data(self, table):
        query = 'select * from {};'.format(table)
        result = self.cursor.execute(query)
        return result

    def insert_single_into_table(self, **data):
        tablekeys = tuple(data.keys())
        tablevalues = tuple(data.values())
        insert_statement = 'insert into table({}) values({})'.format(tablekeys, tablevalues)
        print("Executing command : ".format(insert_statement))

import pymysql
import re

class HandleMysql():
    def __init__(self):
        self.conn, self.cursor = self.setup()
        self.runner()
        self.teardown()

    def setup(self):
        conn = pymysql.connect(host='192.168.200.58', port=3306, user='root', 
                        passwd='123456', database='test', charset='utf8')
        cursor = conn.cursor()
        return conn, cursor
    def teardown(self):
        self.cursor.close()
        self.conn.close()
    def table_exists(self, table):
        result = self.cursor.execute('show tables')
        rows = self.cursor.fetchall()
        print(rows)
        table_list = re.findall('(\'.*?\')', str(rows))
        table_list = [re.sub("'", '', i) for i in table_list]
        if table in table_list:
            return 1
        else:
            return 0


    def create_table(self, table):
        self.cursor.execute('create table {table}()')

    def select_data(self):
        pass
    def update_data(self):
        pass
    def insert_data(self):
        pass
    def delect_data(self):
        pass

    def runner(self):
        res = self.table_exists('test')
        if res:
            print(self.cursor.fetchall())
        else:
            print('表不存在')
        # self.conn.commit()

if __name__ == '__main__':
    my = HandleMysql()

import psycopg2
import csv

# sqlalchemy로 url 지정해서 넣어보려했으나 실패
# from sqlalchemy import create_engine
conn = psycopg2.connect(host='arjuna.db.elephantsql.com', 
dbname='*', user='*', password='*', port=5432)
cur = conn.cursor()

# f = open('used_mobile_phone.csv','r')
# csvReader = csv.reader(f)

# postgreSQL에 테이블 생성해서 직접 insert 방법 선택
# 중고나라 데이터 insert
# cur.execute("CREATE TABLE used_retail (price float, text varchar, phone_model varchar, factory_price integer, maker varchar, price_index float);")
# 번개장터 데이터 insert
cur.execute("CREATE TABLE bangae (locate varchar);")
#conn.commit()

# 변수 지정해서 copy문 사용해서 시도했으나 실패

# cur.execute(sql2)
conn.commit()
# f.close()
conn.close()

## 클래스문 지정해서 데이터베이스 insert 시도했으나 실패
"""
class Database():
    def __init__(self):
        self.db = psycopg2.connect(host='arjuna.db.elephantsql.com', 
        dbname='*', user='*', password='*', port=5432)
        self.cur = db.cursor()

    def __del__(self):
        self.db.close()
        self.cur.close()

    def execute(self,query,args={}):
        self.cur.execute(query,args)
        row = self.cur.fetchall()
        return row

    def commit(self):
        self.cursor.commit()

    def insertDB(self, schema, table, colum, data):
        sql = " INSERT INTO {schema}.{table}({colum}) VALUES ('{data}');".format(schema=schema,table=table,colum=colum,data=data)
        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception as e:
            print(" insert DB ",e)
"""

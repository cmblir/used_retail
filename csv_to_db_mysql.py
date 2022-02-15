from traceback import print_exception
import scipy.io
import csv
import pymysql

conn = pymysql.connect(host='localhost', user='root',password='tlsdud12!!', db='DBtest1', charset='utf8')
cur = conn.cursor()
conn.commit()

f = open('used_mobile_phone.csv','r')
csvReader = csv.reader(f)

for row in csvReader:
    create_date = (row[0])
    price = (row[1])
    phone_model = (row[3])
    factory_price = (row[4])
    maker = (row[5])
    price_index = (row[6])
    


    sql ="""insert into used_retail (create_date, price, phone_model, factory_price, maker, price_index) values (%s,  %s,  %s,  %s,  %s,  %s)"""
    cur.execute(sql, (create_date, price, phone_model, factory_price, maker, price_index))

conn.commit()

f.close()
conn.close()
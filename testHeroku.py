# -*- coding  = utf-8 -*-
# @Time : 10/6/21 2:56 PM
# @Author : Malumolo
# @ File: testHeroku.py
# @Software: PyCharm


import requests
import psycopg2


# Name: email: phone: city: state: country:  
# conn = psycopg2.connect(host = 'ec2-54-161-189-150.compute-1.amazonaws.com', port = 5432, user = 'rxxmjyumuyvrqg', dbname = 'd10h6jfmgo6dgj',password = '4909dea8d4520c01eb1bceb3872a488bf59ab9c2639c5bec6b9c5dd7edf862e0')

conn = psycopg2.connect(host = "ec2-34-233-105-94.compute-1.amazonaws.com",
                        port = 5432,
                        user = "kumyeqamxdmurk",
                        dbname ="d84gvhbmduou75",
                        password = "d60e885fb5d86b21ae28997fbb9105afddd823895e67e9946c16d6c3742e53dd",
                        )
cur = conn.cursor()
# sql_insert_statment = "INSERT into pyclass.plos (id, journel) values ('{}', '{}')"
# r = requests.get('http://api.plos.org/search?q=title:DNA')
# [cur.execute(sql_insert_statment.format(item.get('id'), item.get('journal'))) for item in r.json()['response']['docs']]

# cur.execute("create table evantest( name varchar(255), email varchar(255), phone varchar(255),city varchar(255),state varchar(255),country varchar(255))")
# print(cur.execute(" select * from evan"))

sql_insert_statement = "insert into evan (name,email,phone,city,state,country) values ('evan', 'test@gamil.com','2134211112','Los Angeles','CA','US')"
cur.execute(sql_insert_statement)
# print(cur.execute(sql_insert_statement))
# cur.execute("select * from evan")
# print(cur.execute("select * from evan"))


print(cur.fetchall())
conn.commit()

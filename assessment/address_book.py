"""
Write a program to store the information in the database and CRUD operation.

CRUD - > create, read, update and delete


Address


Name:
email:
phone:
city:
state:
country:

1) You need ask user to enter above information.
2) User can search data
3) Update address book
4) Delete address record.

"""

import psycopg2

db_operate_key=['add','search','update','delete']
Info_key = ["name","email","phone","city","state","country"]

conn = psycopg2.connect(
    host='ec2-18-214-214-252.compute-1.amazonaws.com',
    port='5432',
    user='jeyxxlqqumdqxq',
    dbname='d2dol75vnd2q92',
    password='4f0b9e147e4a99864e37d22b98349ad7c421a2499d81819ebd9f85a93b8276d2'
)

cur = conn.cursor()

Input_oper_key=input("whay do you want to do? {}".format(db_operate_key).upper()).upper()

if Input_oper_key == "ADD":
    print("enter above information for add ")
    name = input("enter name: ")
    email = input("enter email: ")
    phone = input("enter phone: ")
    city = input("enter city: ")
    state = input("enter state: ")
    country = input("country: ")
    cur.execute("insert into pyclass.address_book(name,email,phone,city,state,country) values('{}','{}','{}','{}','{}','{}')".format(name,email,phone,city,state,country))
    conn.commit()
    print("Add info success! ")

elif Input_oper_key == "SEARCH":
    print("search data by enter name")
    name = input("enter name: ")
    cur.execute("select * from pyclass.address_book where name='{}'".format(name))
    print(cur.fetchall())

elif Input_oper_key == "UPDATE":
    #update_key = input("Which info do you want to update?{}".format(Info_key))
    update_key = input("Which name information needs to be modified?")
    Loop_true = 1
    while Loop_true:
        update_item = input("Which info do you want to update? [email, phone, city, state, country]")
        update_info = input("Enter new info:")
        if update_item.upper() == "EMAIL":
            cur.execute("update pyclass.address_book set email='{}' where name='{}'".format(update_info,update_key))
        elif update_item.upper() == "PHONE":
            cur.execute("update pyclass.address_book set phone='{}' where name='{}'".format(update_info, update_key))
        elif update_item.upper() == "CITY":
            cur.execute("update pyclass.address_book set city='{}' where name='{}'".format(update_info, update_key))
        elif update_item.upper() == "STATE":
            cur.execute("update pyclass.address_book set state='{}' where name='{}'".format(update_info, update_key))
        elif update_item.upper() == "COUNTRY":
            cur.execute("update pyclass.address_book set country='{}' where name='{}'".format(update_info, update_key))
        else:
            print('Err! Input operation is not in [email, phone, city, state, country]')

        conn.commit()
        exitFun = input("Update success! Do you want to exit ?(Y/N): ")
        if exitFun.upper() == "Y":
            Loop_true = 0
            print("Exit!")

elif Input_oper_key == "DELETE":
    print("Delete data by enter name")
    name = input("enter name: ")
    cur.execute("delete from pyclass.address_book where name='{}'".format(name))
    conn.commit()
    print("Delete success! ")

else:
    print("Enter err! exit!")






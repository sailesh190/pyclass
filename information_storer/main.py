# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import psycopg2

conn = psycopg2.connect(host='ec2-52-2-118-38.compute-1.amazonaws.com', port=5432, user='gfyadjusuelqhu',
                        dbname='d6rtkk82v8kghs',
                        password='521791264ca305c822febfecf2f45194bea092cfbf51388f84ddd5dc5030c09a')
conn.autocommit = True
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS address_book ('
            'name VARCHAR (50)  PRIMARY KEY,'
            'email VARCHAR (50),'
            'phone VARCHAR (50),'
            'city VARCHAR (50),'
            'state VARCHAR (50),'
            'country VARCHAR (50)'
            ');')
book_choices = {'add', 'update', 'read', 'delete'}
sql_find_statement = "SELECT * FROM address_book WHERE name= '{}' "
sql_insert_statement = "UPDATE address_book " \
                       "SET" \
                       "    {} = '{}' " \
                       "WHERE" \
                       "    name = '{}' "
sql_delete_statement = "DELETE FROM address_book WHERE name = '{}' "


def add():
    name = input('Please enter your name: ')
    email = input('Please enter your email: ')
    phone = input('Please enter your phone: ')
    city = input('Please enter your city: ')
    state = input('Please enter your state:')
    country = input('Please enter your country: ')

    cur.execute('INSERT INTO address_book (name, email, phone, city, state, country)'
                'VALUES(%s, %s, %s, %s, %s, %s)', (name, email, phone, city, state, country))

    cur.execute('SELECT * FROM address_book;')
    print("Here is the information you just inputted: ")
    print(cur.fetchall())


def update():
    name: str = input('Please enter the name of the data ')
    try:
        cur.execute(sql_find_statement.format(name))
    except:
        print("Can not find data, please try again")
        pass
    category = input('Please enter the category you want to change: ')
    new_data = input('Please enter the new data you want to store: ')
    try:
        cur.execute(sql_insert_statement.format(category, new_data, name))
    except:
        print("An error had occurred, please try again.")
        pass
    print('Here is the data now:')
    cur.execute(sql_find_statement.format(name))
    print(cur.fetchone())


def read():
    name = input("Please enter the name of the recipient: ")
    cur.execute(sql_find_statement.format(name))
    print(cur.fetchone())


def delete():
    name = input("Please enter the recipient's name: ")
    cur.execute(sql_find_statement.format(name))
    print("The current address is below:")
    print(cur.fetchone())
    deletion = input("Do you want to delete it? yes or no:")
    if deletion == 'yes':
        cur.execute(sql_delete_statement.format(name))
        print('Addresss Deleted.')


while True:
    choice = input(f'Please type the command you want to use {book_choices}')
    if choice == 'add':
        add()
        continue
    elif choice == 'update':
        update()
        continue
    elif choice == 'read':
        read()
        continue
    elif choice == 'delete':
        delete()
        continue
    else:
        print("Invalid command, program exiting...")
        break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

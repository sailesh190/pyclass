import psycopg2

conn = psycopg2.connect(
    host='ec2-54-161-189-150.compute-1.amazonaws.com', port=5432, user='rxxmjyumuyvrqg', dbname='d10h6jfmgo6dgj',
    password='4909dea8d4520c01eb1bceb3872a488bf59ab9c2639c5bec6b9c5dd7edf862e0')

cur = conn.cursor()

entries = ["name", "email", "phone", "city", "state", "country"]

# fetch all table names

sql_statment = "select * from information_schema.tables where table_schema = 'pyclass';"

cur.execute(sql_statment)

conn.commit()

table_name_index = [item.name for item in cur.description].index('table_name')

table_names = [item[table_name_index] for item in cur.fetchall()]

# if there is not table called "address_book_di" then just create one

if 'address_book_di' not in table_names:
    
    # define id to allow duplicate entries
    
    temp_str = ", ".join([item + " varchar(255)" for item in entries])
    
    sql_statment = f"create table pyclass.address_book_di (id SERIAL primary key, {temp_str});"
    
    cur.execute(sql_statment)
    
    conn.commit()


def search_fun(entries):
    
    temp_str = " ".join(entries).upper()

    search_entry = input(f"Which entry would you like to search with? {temp_str}:")

    while search_entry.lower() not in entries:

        search_entry = input(f"You entered wrong entry, please enter {temp_str}:")

    search_value = input("Please enter the value of this entry:")

    sql_statment = f"select * from pyclass.address_book_di where {search_entry}='{search_value}';"

    cur.execute(sql_statment)

    conn.commit()

    search_result = [dict(zip([item.name for item in cur.description], value)) for value in cur.fetchall()]
    
    return(search_result)


def find_contact_id(entries):
    
    search_result = search_fun(entries)

    if len(search_result):

        print("Below is the search result:")

        for i in range(len(search_result)):

            print("\n")

            print(f"({i + 1})")

            for entry in entries:

                print(entry + ": " + search_result[i][entry])

        print("\n")

        if len(search_result) == 1:

            search_result_index = 0

        else:

            contact_index_str = input("Please select a contact by entering the index number:")

            while not contact_index_str.isdigit():
                
                contact_index_str = input("You entered wrong number. Please enter again:")

            search_result_index = int(contact_index_str) - 1

            while search_result_index > len(search_result) - 1:

                contact_index_str = input("The number you entered is too large. Please enter again:")
                
                while not contact_index_str.isdigit():

                    contact_index_str = input("You entered wrong number. Please enter again:")

                search_result_index = int(contact_index_str) - 1
                
        contact_id = search_result[search_result_index]["id"]
        
        print("OK. This is the contact you selected.\n")

        for entry in entries:

            print(entry + ": " + search_result[search_result_index][entry])

        print("\n")

    else:
        
        print("No results.")

        contact_id = None
        
    return(contact_id)


operations = ["ADD", "SEARCH", "EDIT", "DELETE"]

if_continue = "Y"

while if_continue.upper() == "Y":
    
    temp_str = " ".join(operations)
    
    operation_type = input(f"What are you going to do with the address book? {temp_str}:")
    
    while operation_type.upper() not in operations:
                
        operation_type = input(f"You entered wrong keyword, please enter {temp_str}:")
        
    if operation_type.upper() == "ADD":
                
        add_info = []

        for item in entries:

            add_info.append(input("Please enter " + item + ":"))
            
        temp_str_1 = ", ".join(entries)
        
        temp_str_2 = ", ".join(["'" + item + "'" for item in add_info])

        sql_statment = f"insert into pyclass.address_book_di ({temp_str_1}) values ({temp_str_2});"
        
        cur.execute(sql_statment)

        conn.commit()
        
        print("New contact added.")

    elif operation_type.upper() == "SEARCH":
        
        search_result = search_fun(entries)

        if len(search_result):

            print("Below is the search result:")

            for record in search_result:

                print("\n")

                for entry in entries:

                    print(entry + ": " + record[entry])

        else:

            print("No results.")
        
    elif operation_type.upper() == "EDIT":
        
        print("Please locate the contact you would like to edit first.")
        
        edit_id = find_contact_id(entries)
        
        if edit_id is not None:
            
            temp_str = " ".join(entries).upper()
        
            edit_entry = input(f"Which entry you would like to update for this contact? {temp_str}:")

            while edit_entry.lower() not in entries:
                
                temp_str = " ".join(entries).upper()

                edit_entry = input(f"You entered wrong entry, please enter {temp_str}:")

            edit_value = input("Please enter the new value for this entry: ")

            sql_statment = f"update pyclass.address_book_di set {edit_entry}='{edit_value}' where id={edit_id};"

            cur.execute(sql_statment)

            conn.commit()
            
            print("Contact updated.")
        
    elif operation_type.upper() == "DELETE":
        
        print("Please locate the contact you would like to delete first.")
        
        delete_id = find_contact_id(entries)
        
        if delete_id is not None:

            sql_statment = f"delete from pyclass.address_book_di where id={delete_id};"

            cur.execute(sql_statment)

            conn.commit()
            
            print("Contact deleted.")
        
    if_continue = input("Would you like to continue? (Y or N):")
    
    while if_continue.upper() != "Y" and if_continue.upper() != "N":
        
        if_continue = input("You entered wrong response. Would you like to continue? (Y or N):")
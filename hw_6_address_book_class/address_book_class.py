import psycopg2

conn = psycopg2.connect(
    host='ec2-54-161-189-150.compute-1.amazonaws.com', port=5432, user='rxxmjyumuyvrqg', dbname='d10h6jfmgo6dgj',
    password='4909dea8d4520c01eb1bceb3872a488bf59ab9c2639c5bec6b9c5dd7edf862e0')

cur = conn.cursor()

entries = ["name", "email", "phone", "city", "state", "country"]

temp_str = ", ".join([item + " varchar(255)" for item in entries])

sql_statment = f"create table if not exists pyclass.address_book_di (id serial primary key, {temp_str});"

cur.execute(sql_statment)

conn.commit()

class contact:
    def __init__(self):
        self.name = input("Please enter name:")
        self.email = input("Please enter email:")
        self.validate_email()
        self.phone = input("Please enter phone:")
        self.validate_phone()
        self.city = input("Please enter city:")
        self.state = input("Please enter state:")
        self.country = input("Please enter country:")
        
    def validate_email(self):
        while not "@" in self.email:
            self.email = input("Your email is invalid, please enter again: ")
    
    def validate_phone(self):
        while not self.phone.isnumeric():
            self.phone = input("Your phone is invalid, please enter again: ")

if_continue = "Y"

while if_continue.upper() == "Y":
    
    new_contact = contact()

    temp_str_1 = ", ".join([item for item in vars(new_contact).keys()])

    temp_str_2 = ", ".join(["'" + item + "'" for item in vars(new_contact).values()])

    sql_statment = f"insert into pyclass.address_book_di ({temp_str_1}) values ({temp_str_2});"

    cur.execute(sql_statment)

    conn.commit()

    print("New contact added.")
    
    if_continue = input("Would you like to continue? (Y or N):")
    
    while if_continue.upper() != "Y" and if_continue.upper() != "N":
        
        if_continue = input("Your input is invlid. Would you like to continue? (Y or N):")
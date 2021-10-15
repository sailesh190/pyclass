import psycopg2

entries = ["name", "email", "phone", "city", "state", "country"]

class Contact:
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

class Dbconnect(Contact):
    
    def __init__(self, host, port, user, dbname, password):
        self.host = host
        self.port = port
        self.user = user
        self.dbname = dbname
        self.password = password
    
    def get_connect(self):
        self.conn = psycopg2.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            dbname = self.dbname,
            password = self.password
        )
        
        self.cur = self.conn.cursor()
        
    def query(self, statement):
        self.cur.execute(statement)
        self.conn.commit()
        
    def create_statement(self, entries):
        temp_str = ", ".join([item + " varchar(255)" for item in entries])
        return(f"create table if not exists pyclass.address_book_di (id serial primary key, {temp_str});")
        
    def insert_statement(self, entries):
        super().__init__()
        temp_str_1 = ", ".join([item for item in entries])
        temp_str_2 = ", ".join(["'" + vars(self)[item] + "'" for item in entries])
        return(f"insert into pyclass.address_book_di ({temp_str_1}) values ({temp_str_2});")
    

    
pyclass_connect = Dbconnect('ec2-54-161-189-150.compute-1.amazonaws.com',
                            5432,
                            'rxxmjyumuyvrqg',
                            'd10h6jfmgo6dgj',
                            '4909dea8d4520c01eb1bceb3872a488bf59ab9c2639c5bec6b9c5dd7edf862e0')

pyclass_connect.get_connect()
pyclass_connect.query(pyclass_connect.create_statement(entries))

if_continue = "Y"

while if_continue.upper() == "Y":
    
    pyclass_connect.query(pyclass_connect.insert_statement(entries))

    print("New contact added.")
    
    if_continue = input("Would you like to continue? (Y or N):")
    
    while if_continue.upper() != "Y" and if_continue.upper() != "N":
        
        if_continue = input("Your input is invlid. Would you like to continue? (Y or N):")
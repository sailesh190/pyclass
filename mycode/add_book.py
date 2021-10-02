address_book = []


for item in range(3):
    name = input("Enter your name:")
    email = input("Enter your email:")
    phone = input("Enter your phone number:")
    address_book.append(dict(name=name, email=email, phone=phone))


print(address_book)
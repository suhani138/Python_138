# create an empty list to store the database
database = []

# function to add a new record to the database
def add_record(name, age, city):
    record = {'Name': name, 'Age': age, 'City': city}
    database.append(record)
    print('Record added successfully')

# function to display all the records in the database
def display_records():
    for record in database:
        print(record)

# main program
while True:
    print('Enter your name, age, and city:')
    name = input('Name: ')
    age = int(input('Age: '))
    city = input('City: ')
    add_record(name, age, city)
    print('Do you want to add another record? (y/n)')
    choice = input()
    if choice == 'n':
        break
display_records()

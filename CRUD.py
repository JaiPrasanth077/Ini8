import mysql.connector

connection = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="jaiprasanth", #use your sql password
    database="Regs"
)

def create_registration(name, email, dob, num):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO Registration (Name, Email, dob, contactnum) VALUES (%s, %s, %s, %s)", (name, email, dob, num))
        connection.commit()
        registration_id = cursor.lastrowid
        print("Registration created successfully with ID:", registration_id)
    except mysql.connector.Error as err:
        print("Error creating registration:", err)
    finally:
        cursor.close()

def read_registration(registration_id):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM Registration WHERE ID = %s", (registration_id,))
        registration = cursor.fetchone()
        if registration:
            print("Registration details:")
            print("ID:", registration[0])
            print("Name:", registration[1])
            print("Email:", registration[2])
            print("DOB:", registration[3])
            print("Contact Number:", registration[4])
        else:
            print("Registration not found")
    except mysql.connector.Error as err:
        print("Error reading registration:", err)
    finally:
        cursor.close()

def update_registration(registration_id, email):
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE Registration SET Email = %s WHERE ID = %s", (email, registration_id))
        connection.commit()
        print("Registration updated successfully")
    except mysql.connector.Error as err:
        print("Error updating registration:", err)
    finally:
        cursor.close()

def delete_registration(registration_id):
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM Registration WHERE ID = %s", (registration_id,))
        connection.commit()
        print("Registration deleted successfully")
    except mysql.connector.Error as err:
        print("Error deleting registration:", err)
    finally:
        cursor.close()

def menu():
    print("Welcome to Ini8 Registration System")
    print("1. Create Registration")
    print("2. Read Registration")
    print("3. Update Registration")
    print("4. Delete Registration")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        num = input("Enter Contact Number: ")
        create_registration(name, email, dob, num)
    elif choice == '2':
        registration_id = input("Enter Registration ID: ")
        read_registration(registration_id)
    elif choice == '3':
        registration_id = input("Enter Registration ID: ")
        email = input("Enter new Email: ")
        update_registration(registration_id, email)
    elif choice == '4':
        registration_id = input("Enter Registration ID: ")
        delete_registration(registration_id)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")

connection.close()

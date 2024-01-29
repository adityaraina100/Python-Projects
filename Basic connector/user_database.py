import sqlite3


conn = sqlite3.connect('user_data.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')



def add_user(name, email):
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    print("User added successfully!")

def view_users():
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    for row in rows:
        print(row)


while True:
    print("\n1. Add User")
    print("2. View Users")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter user's name: ")
        email = input("Enter user's email: ")
        add_user(name, email)
    elif choice == '2':
        view_users()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

conn.close()

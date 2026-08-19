# login_system.py
users = {"renu": "1234", "admin": "admin"}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login Successful! ✅")
else:
    print("Invalid Username or Password ❌")
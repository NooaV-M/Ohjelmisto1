Username = input("Enter your username: ")
password = input("Enter your password: ")
login_attempts = 0

while password != "rules" or Username != "python":
    if login_attempts < 4:
        print("Invalid username or password!")
        Username = input("Enter your username: ")
        password = input("Enter your password: ")
        login_attempts += 1
    else:
        break

if login_attempts >= 4:
    print("Access denied")
else:
    print("Welcome")
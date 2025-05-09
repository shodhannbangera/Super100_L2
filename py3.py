import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users:
        print("Username already exists.")
    else:
        users[username] = hash_password(password)
        print("Created new user")

def login(username, password):
    hashed = hash_password(password)
    if username in users and users[username] == hashed:
        print("Login Successful")
    else:
        print("Login Failed")

def main():
    while True:
        action = input("Would you like to Register or Login? (type 'r' or 'l', 'exit' to quit): ").lower()
        
        if action == "exit":
            break
        
        if action not in ["r", "l"]:
            print("Invalid option. Please try again.")
            continue
        
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if action == "r":
            register(username, password)
        elif action == "l":
            login(username, password)

if __name__ == "__main__":
    main()

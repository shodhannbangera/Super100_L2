users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

#create
new_user={"id":3,"name":"cat","email":"cat@example.com"}
users.append(new_user)
print("create")
print(users)

#Read
print("Read")
for user in users:
    if user["name"]=="cat":
        print("cat info")
        print(user)

#update
print("update")
for user in users:
    if user["id"]==2:
        user["name"]="bobby"
        user["email"]="bobby@gmail.com"
print(users)

#delete
print("delete")
for user in users:
    if user["id"]==1:
        users.remove(user)
print(users)


def isValidEmail(email):
    n= len(email)
    if email[n-4:] == ".com" and '@' in email and email[0]!='@':
        return True
    return False

email=input("enter the email:")
print(isValidEmail(email))
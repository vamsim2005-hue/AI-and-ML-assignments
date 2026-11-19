# Username Validation System

username = input("Enter your username: ")

# Check username conditions
if len(username) < 5:
    print("Invalid Username")
    print("Reason: Username must contain at least 5 characters.")

elif username.strip() == "":
    print("Invalid Username")
    print("Reason: Username cannot contain only spaces.")

elif username.lower() == "admin":
    print("Invalid Username")
    print("Reason: Username cannot be 'admin'.")

else:
    print("Valid Username")
    print("Welcome,", username)
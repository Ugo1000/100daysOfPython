import re

def validate_password():
    while True:
        password = input('Enter password : ')
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        if re.match(pattern, password):
            return "Valid password"
        else:
            print("Invalid password. Password must have at least 8 characters including at least one uppercase letter, one lowercase letter, one digit, and one special character.")

# Test the password validator (uncomment and use if necessary)
# print(validate_password())

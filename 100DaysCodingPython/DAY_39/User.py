

'''This Module is for user input'''

def get_username():
    try:    
        name = input("Username: ")
        return name
    except Exception as e:
        print("An error occurred:", e)
        return None


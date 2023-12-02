from password import validate_password
from User import get_username


def main():
    user = get_username()
    passw = validate_password()

    if passw:
        print('Welcome To My App')
    else: 
        print('Not welcome')


if __name__ == "__main__":
    main()

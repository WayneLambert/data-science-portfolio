import random
from string import ascii_lowercase, ascii_uppercase, digits

special_chars = "!#$%&*@^"
available_chars = list(ascii_lowercase) + list(ascii_uppercase) + list(digits) + list(special_chars)


def get_length():
    user_l = ""
    while not user_l.isdigit() or int(user_l) < 6:
        user_l = input("Please input a password length.\n")
    return int(user_l)


def pwd_gen(length):
    return [random.choice(available_chars) for i in range(length)]


def pwd_chk(length):
    pwd = []
    while True:
        pwd = pwd_gen(length)
        if set(pwd) & set(ascii_lowercase) == set():
            continue
        elif set(pwd) & set(ascii_uppercase) == set():
            continue
        elif set(pwd) & set(digits) == set():
            continue
        elif set(pwd) & set(special_chars) == set():
            continue
        else:
            print("\nYour password is " + "".join(pwd))
            while True:
                accept = input("Would you like a different password? Y/N\n\n")
                if accept.lower() in ["n", "no"]:
                    print("\nYour password is:")
                    break
                elif accept.lower() in ["y", "yes"]:
                    pwd_chk(length)
                    break
                else:
                    print("\nInvalid input. Your password is " + "".join(pwd))
                    continue
            break

    pwd = "".join(pwd)
    print(pwd)

pwd_chk(get_length())

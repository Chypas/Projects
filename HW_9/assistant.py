import re


def decorator(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            print("Sorry, try again")
    return wrapper


def decorator_add(func):
    def wrapper(user_input):
        name = re.search("\D+", user_input[1]) is not None
        phone = re.search("\d+", user_input[2]) is not None
        if name and phone == True:
            return func(user_input)
        else:
            print("add 'name' 'number'")
    return wrapper


adress_book = {}
end_comand = ["end", "exit", "out", "close", "."]
a_b = {}
user_input = ""


@decorator_add
@decorator
def add_func(user_input):
    a_b = {user_input[1]: user_input[2]}
    adress_book.update(a_b)
    a_b = {}


@decorator
def change_func(user_input):
    adress_book[user_input[1]] = user_input[2]


@decorator
def phone_func(user_input):
    for k, v in adress_book.items():
        if user_input[1] in k:
            return v


@decorator
def show_func(user_input):
    i = ""
    for k, v in adress_book.items():
        i += str("{0}: {1}\n".format(k, v))
    return i


@decorator
def main():
    print("Hello!")
    global user_input
    user_input = input().lower().split(" ")
    while True:
        if user_input[0] == "hello":
            print("How can I help you?")
            user_input = input().lower().split(" ")

        elif user_input[0] == "add":
            add_func(user_input)
            user_input = input().lower().split(" ")

        elif user_input[0] == "change":
            change_func(user_input)
            user_input = input().lower().split(" ")

        elif user_input[0] == "phone":
            print(phone_func(user_input))
            user_input = input().lower().split(" ")

        elif user_input[0] == "show":
            print(show_func(user_input))
            user_input = input().lower().split(" ")

        elif user_input[0] in end_comand:
            print("Good bye!")
            break
        else:
            print("Wrong command, try again.")
            user_input = input().lower().split(" ")


main()

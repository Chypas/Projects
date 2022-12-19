adress_book = {}
end_comand = ["end", "exit", "out", "close", "."]
a_b = {}
user_input = ""


def add_func(user_input):
    a_b = {user_input[1]: user_input[2]}
    adress_book.update(a_b)
    a_b = {}


def change_func(user_input):
    adress_book[user_input[1]] = user_input[2]


def phone_func(user_input):
    for k, v in adress_book.items():
        if user_input[1] in k:
            print(v)


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
            phone_func(user_input)
            user_input = input().lower().split(" ")

        elif user_input[0] == "show":
            for key, value in adress_book.items():
                print("{0}: {1}".format(key, value))
            user_input = input().lower().split(" ")

        elif user_input[0] in end_comand:
            print("Good bye!")
            break
        else:
            user_input = input().lower().split(" ")


main()

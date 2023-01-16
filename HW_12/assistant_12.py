from collections import UserDict
from datetime import datetime
import re
import pickle


class AddressBook(UserDict):

    def add_record(self, rec):
        self.data[rec.name.value] = rec

    def iterator(self, n=2):
        self.n = n
        index = 1
        print_block = '-' * 50 + '\n'
        for name, record in self.data.items():
            print_block += str(name)+":" + " " + str(record) + '\n'
            if index < n:
                index += 1
            else:
                yield print_block
                index, print_block = 1, '-' * 50 + '\n'
        yield print_block

    def next(self, n=2):
        result = "List of all users:\n"
        print_list = self.iterator(n)
        for item in print_list:
            result += f"{item}"
        return result

    def search_of_user(self, text):
        list_of_users = []
        for n, r in self.data.items():
            search_name = re.search(text, str(r)) is not None
            search_data = re.search(text.lower(), str(n.lower())) is not None
            if search_data == True or search_name == True:
                list_of_users.append(str(f"{n}: {r}"))
        return f"Search result: \n{list_of_users}" 
                    
    def write_to_file(self):
        file_name = 'Adress book.txt'
        with open(file_name, "wb") as fh:
            pickle.dump(self.data, fh)

    def load_from_file(self):
        file_name = 'Adress book.txt'
        with open(file_name, "rb") as fh:
            unpacked = pickle.load(fh)
            self.data.update(unpacked)


class Field:

    def __init__(self, value):
        self.value = value

    @ property
    def value(self):
        return self.__value

    @ value.setter
    def value(self, new_value):
        self.__value = new_value

    def __repr__(self) -> str:
        return f"{self.value}"

    def __str__(self) -> str:
        return f"{self.value}"


class Name(Field):
    pass


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if value.isdigit():
            self.__value = value
        else:
            raise Exception("Wrong number.")


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        sb = re.search(r"\d{2} [a-zA-Z]+ \d{4}", str(value)) is not None
        if sb == True:
            self.__value = value
        else:
            raise Exception("Wrong type of birthday.")


class Record:
    def __init__(self, name, birthday=None, phone=None):
        self.name = name
        if birthday:
            self.birthday = birthday
        if phone:
            self.phones = [phone]
        else:
            self.phones = []

    def __repr__(self):
        return f"{self.birthday} {self.phones}"

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):
        for i in self.phones:
            if old_phone == i:
                self.phones.remove(i)
                self.phones.append(Phone(new_phone))

    def delete_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)

    def days_to_birthday(self):
        current_datetime = datetime.now()
        birth_day = datetime.strptime(self.birthday.value, "%d %B %Y")
        t_y_b = datetime(year=2023, month=birth_day.month, day=birth_day.day)
        day_to_birth = t_y_b - current_datetime
        return f'{day_to_birth.days} days to {self.name.value} Birthday'


if __name__ == '__main__':
    name = Name('Bill')
    birthday = Birthday('24 may 1990')
    phone = Phone('1234567890')
    bill = Record(name, birthday, phone)
    ab = AddressBook()
    ab.add_record(bill)

    name = Name("Roman")
    birthday = Birthday('24 june 2000')
    phone = Phone('0987654321')
    roman = Record(name, birthday, phone)
    ab.add_record(roman)
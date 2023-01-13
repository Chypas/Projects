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
        for record in self.data.values(): 
            print_block += str(record) + '\n'
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
    
    # def inf(self, text):
    #     for record in self.data.values(): 
    #         if text in record:
    #             return record  
    
    # def write_to_file(self):
    #     file_name = 'Adress book.txt'
    #     with open(file_name, "wb") as fh:
    #         pickle.dump(self.data, fh)

    # def load_from_file(self):
    #     file_name = 'Adress book.txt'
    #     with open(file_name, "rb") as fh:
    #         unpacked = pickle.load(fh)
    #         self.data.update(unpacked)
        
class Field:
    def __init__(self, name, birthday=None, phone=None):
        # self.value = value
        self.name = name
        self.__private_phone = None
        self.__private_birthday = None
        self.birthday = birthday
        self.phone = phone

    @property
    def birthday(self):
        return self.__private_birthday

    @birthday.setter
    def birthday(self, value: str):
        sb = re.search("\d{2} [a-zA-Z]+ \d{4}", str(value)) is not None
        if sb == True:
            self.__private_birthday = value
        else:
            raise Exception("Wrong type of birthday.")

    @property
    def phone(self):
        return self.__private_phone

    @phone.setter
    def phone(self, value: str):
        if value.isdigit():
            self.__private_phone = value
        else:
            raise Exception("Wrong number.")

    def __repr__(self) -> str:
        return f"{self.value}"

    def __str__(self) -> str:
        return f"{self.value}"


class Name(Field):
    pass


class Phone(Field):
    pass


class Birthday(Field):
    pass


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
    birthday = Birthday('24 august 1990')
    phone = Phone('1234567890')
    bill = Record(name, birthday, phone)
    ab = AddressBook()
    ab.add_record(bill)

    name = Name("Roman")
    birthday = Birthday('24 may 2000')
    phone = Phone('0987654321')
    roman = Record(name, birthday, phone)
    ab.add_record(roman)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].birthday, Birthday)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print("All Ok)")
    print(type(birthday))

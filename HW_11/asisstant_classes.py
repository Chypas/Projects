from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):

    def add_record(self, rec):
        self.data[rec.name.value] = rec

    # def __repr__(self):
    #     return f"repr AB {self.data}"

    # def __str__(self) -> str:
    #     return f"str AB {self.data}"

    def __iter__(self):
        return self

    def __next__(self):
        pass


class Field:
    def __init__(self, value):
        self.value = value

    def __repr__(self) -> str:
        return f"repr Field {self.value}"

    def __str__(self) -> str:
        return f"str Field {self.value}"


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
        return f"repr Record {self.birthday} {self.phones}"

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
    birthday = Birthday('24.08.2000')
    phone = Phone('0987654321')
    roman = Record(name, birthday, phone)
    ab.add_record(roman)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].birthday, Birthday)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')
    print(str(ab))
    print(bill.days_to_birthday())

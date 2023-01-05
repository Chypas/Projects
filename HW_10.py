from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, rec):
        self.data[rec.name.value] = rec


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        if phone:
            self.phones = [phone]
        else:
            self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)
        phone = self.phones

    def change_phone(self, old_phone, new_phone):
        for i in self.phones:
            if old_phone in self.phones:
                self.phones.remove(i)
                self.phones.append(new_phone)

    def delete_phone(self):
        for i in self.phones:
            self.phones.remove(i)

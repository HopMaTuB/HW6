from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value):
        if len(value)>=10:
            super().__init__(value)
        else:
            raise Exception("Phone number must be Longer than 10 numbers")
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    def del_phone(self,phone):
        for p in self.phones:
            if p.value != phone:
                self.phones.remove(p)
    
    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone   

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value                      

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]


    def delete(self, name):
        if name in self.data:
            del self.data[name]



book = AddressBook()



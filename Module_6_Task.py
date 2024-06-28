from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value:str):
        self.value=value.capitalize()

class Phone(Field):
    def __init__(self, value):
        self.value=validate(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = [] #Елементи всередині списку будуть об'єктами Phone

    def add_phone(self, phone:str):
        if phone not in [p.value for p in self.phones]:
            self.phones.append(Phone(phone))
        else:print(f'{phone} already exists')

    def remove_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones = [p for p in self.phones if p.value != phone_obj.value]

    def edit_phone(self, old_phone: str, new_phone: str):
        try:
            index = next(i for i, p in enumerate(self.phones) if p.value == old_phone)
        except StopIteration:
            return print(f'{old_phone} does not exist')
        self.phones[index] = Phone(new_phone)

    def find_phone(self, phone: str):
        phone_obj = Phone(phone)
        for p in self.phones:
            if p.value == phone_obj.value:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

def validate(phone: str):
    if phone.isdigit() and len(phone) == 10:return phone
    else:raise ValueError('Phone number must be 10 digits.')

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        try:return self.data[name]
        except KeyError: print(f'{name} does not exist')

    def delete(self, name):
        try: del self.data[name]
        except KeyError: print(f'{name} does not exist')

    def __str__(self) -> str:
        return '\n'.join(str(record) for record in self.data.values())

# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
print(book)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
book.delete("Jane")
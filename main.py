#task1
class AccessDescriptor:
    def __init__(self, name):
        self.name = name
        self._value = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if value not in ["read", "write", "execute"]:
            raise ValueError(f"Invalid access permission: {value}. "
                             f"Allowed values are 'read', 'write', 'execute'.")
        self._value = value

    def __delete__(self, instance):
        self._value = None


class FileManager:
    permission = AccessDescriptor("permission")

    def __init__(self, file_name, permission):
        self.file_name = file_name
        self.permission = permission

    def __repr__(self):
        return f"FileManager(file_name='{self.file_name}', permission='{self.permission}')"

try:
    file1 = FileManager("example.txt", "read")
    print(file1)

    file1.permission = "write"
    print(file1)

    file1.permission = "delete"
except ValueError as e:
    print(e)

#task2
class Car:
    def __init__(self, speed=0, fuel_type="бензин"):
        self._speed = 0
        self._fuel_type = None
        self.speed = speed
        self.fuel_type = fuel_type

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if not (0 <= value <= 240):
            raise ValueError("Швидкість має бути від 0 до 240 км/год")
        self._speed = value

    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        allowed_fuels = ["бензин", "дизель", "електро"]
        if value not in allowed_fuels:
            raise ValueError(f"Тип пального має бути одним із {allowed_fuels}")
        self._fuel_type = value

    def __repr__(self):
        return f"Car(speed={self.speed}, fuel_type='{self.fuel_type}')"

try:
    car = Car(120, "дизель")
    print(car)

    car.speed = 250
except ValueError as e:
    print(e)

try:
    car.fuel_type = "газ"
except ValueError as e:
    print(e)

car.speed = 80
car.fuel_type = "електро"
print(car)

#task3
class EmailValidator:
    def __get__(self, instance, owner):
        return instance._email

    def __set__(self, instance, value):
        if "@" not in value or "." not in value:
            raise ValueError("Некоректна електронна пошта. Вона повинна містити '@' і '.'")
        instance._email = value

class PhoneNumberValidator:
    def __get__(self, instance, owner):
        return instance._phone_number

    def __set__(self, instance, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Телефонний номер повинен містити рівно 10 цифр")
        instance._phone_number = value

class UserProfile:
    email = EmailValidator()
    phone_number = PhoneNumberValidator()

    def __init__(self, email, phone_number):
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return f"UserProfile(email='{self.email}', phone_number='{self.phone_number}')"

user = UserProfile("example@gmail.com", "1234567890")
print(user)

user.email = "new_email@example.com"
user.phone_number = "0987654321"
print(user)

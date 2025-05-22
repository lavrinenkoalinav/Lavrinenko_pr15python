def create_person_class():
    class Person:
        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.city = city

        def short_info(self):
            return f"{self.name}, {self.age} років, м. {self.city}"

    return Person

def create_car_class():
    class Car:
        def __init__(self, brand, model, year, color):
            self.brand = brand
            self.model = model
            self.year = year
            self.color = color

        def full_info(self):
            return f"{self.year} {self.brand} {self.model}, колір: {self.color}"

        def change_color(self, new_color):
            self.color = new_color
            return f"Колір змінено на {self.color}"

    return Car

def create_bank_account_class():
    class BankAccount:
        def __init__(self, owner, account_number, balance=0):
            self.owner = owner
            self.account_number = account_number
            self.balance = balance

        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"Поповнення на {amount} грн. Новий баланс: {self.balance} грн.")
            else:
                print("Сума повинна бути більшою за нуль.")

        def withdraw(self, amount):
            if amount > self.balance:
                print("Недостатньо коштів на рахунку.")
            elif amount <= 0:
                print("Сума зняття повинна бути більшою за нуль.")
            else:
                self.balance -= amount
                print(f"Знято {amount} грн. Залишок: {self.balance} грн.")

        def check_balance(self):
            return f"Поточний баланс: {self.balance} грн."

    return BankAccount

if __name__ == "__main__":
    # Завдання 1
    Person = create_person_class()
    person = Person("Олена", 20, "Київ")
    print("Завдання 1: Клас Людина")
    print(person.short_info())
    print("-" * 40)

    # Завдання 2
    Car = create_car_class()
    car = Car("Toyota", "Camry", 2020, "чорний")
    print("Завдання 2: Клас Автомобіль")
    print(car.full_info())
    print(car.change_color("білий"))
    print(car.full_info())
    print("-" * 40)

    # Завдання 3
    BankAccount = create_bank_account_class()
    account = BankAccount("Олена Іваненко", "UA1234567890", 5000)
    print("Завдання 3: Клас Банк")
    print(account.check_balance())
    account.deposit(1500)
    account.withdraw(3000)
    account.withdraw(4000)
    print(account.check_balance())
    print("-" * 40)

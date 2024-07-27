from genericList import TypeSafeList

# Usage examples:
print("---------------------1111111111111111111111----------------------")
# Example-->1.1. single type (int)
int_list = TypeSafeList(int)
int_list.append(1)
int_list.append(2)
print(int_list)  #print: [1, 2]

try:
    int_list.append("3")
except TypeError as e:
    print(f"int_list--->Error: {e}")  # Error: Only use (<class 'int'>,) types
    
# Example-->1.2.single type (str)
str_list = TypeSafeList(str)
str_list.append("1")
str_list.append("2")
print(str_list)  #print: [1, 2]

try:
    str_list.append(3)
except TypeError as e:
    print(f"str_list--->Error: {e}")  # Error: Only use (<class 'str'>,) types

print("----------------------2222222222222222222222222-------------------")
# Example--> 2. mixed types (int, str,bool,...)
mixed_list = TypeSafeList((int, str,bool))
mixed_list.append(1)
mixed_list.append("two")
mixed_list.append(True)
jsonType = '{"name": "John", "age": 30}'
mixed_list.append(jsonType)

print(mixed_list)  # print:[1, 'two',True, '{"name": "John", "age": 30}']

try:
    mixed_list.append(3.14)
except TypeError as e:
    print(f" mixed_list--->Error: {e}")  # Error: Only use (<class 'int'>, <class 'str'>) types

print("---------------------3333333333333333333333333333-------------------")
# Example--> 3. for  classes ve inherited classes
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Employee(Person):
    pass
class Manager():
    pass
person_list = TypeSafeList(Person)

person_list.append(Person("Alice"))
person_list.append(Employee("Bob"))  # because Employee is a subclass of Person
print(person_list)  # print:[Person,Employee]

try:
    person_list.append(Manager())
except TypeError as e:
    print(f"person_list--->Error: {e}")  # Error: Only use (<class '__main__.Person'>,) types
    
print("------------------------44444444444444444----------------------------")
# Example--> 4. for mixed types and classes
mixed_types_list = TypeSafeList((int, str,Person))
mixed_types_list.append(1)
mixed_types_list.append("two")
mixed_types_list.append(Person("Ayhan"))
mixed_types_list.append(Employee("Mustafa"))
print(mixed_types_list)  #print:[1, 'two', Person,Employe]
try:
    int_list.append(3.13)
except TypeError as e:
    print(f"mixed_types_list--->Error: {e}")
    
print("----------------------55555555555555555555------------------------------")
# Example--> 5. Instance type
class Car:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    def __str__(self):
        return f"{self.brand} {self.model}"

# for Car instances
car_list = TypeSafeList(Car)

# Car instances added
car_list.append(Car("Toyota", "Corolla"))
car_list.append(Car("Honda", "Civic"))
car_list.append(Car("Ford", "Focus"))

print("Car listesi:")
for car in car_list:
    print(car)

try:
    car_list.append("Not a car")
except TypeError as e:
    print(f"car_list--->Error: {e}")
    
print("-------------------66666666666666666666---------------------------------")
# Example--> 6. diffrent  instance types
class Motorcycle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    def __str__(self):
        return f"{self.brand} {self.model} (Motorcycle)"

vehicle_list = TypeSafeList((Car, Motorcycle))

vehicle_list.append(Car("Tesla", "Model S"))
vehicle_list.append(Motorcycle("Harley-Davidson", "Street 750"))
vehicle_list.append(Car("BMW", "X5"))

print("\nVehicle listesi:")
for vehicle in vehicle_list:
    print(vehicle)

try:
    vehicle_list.append(Person("John"))  # Person instance cannot be added
except TypeError as e:
    print(f"vehicle_list--->Error: {e}")
    
print("-------------------777777777777777777777---------------------------------")
# Example--> 7. inhered class instance types
class ElectricCar(Car):
    def __init__(self, brand: str, model: str, battery_capacity: int):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def __str__(self):
        return f"{super().__str__()} (Electric, {self.battery_capacity} kWh)"

electric_vehicle_list = TypeSafeList(Car)  # Accepts Car and its subclasses

electric_vehicle_list.append(Car("Toyota", "Camry"))
electric_vehicle_list.append(ElectricCar("Tesla", "Model 3", 75))

print("\nElectric Vehicle lists:")
for vehicle in electric_vehicle_list:
    print(vehicle)

try:
    electric_vehicle_list.append(Motorcycle("Yamaha", "MT-07"))  # Motorcycle instance cannot be added
except TypeError as e:
    print(f"electric_vehicle_list--->Error: {e}")
    
print("-------------------8888888888888888888888---------------------------------")   
# Example-->8.Dictionary types

dict_list = TypeSafeList((dict,Car))
dictionary=dict(name="Ayhan",surname="öZTEMEL")
dictionary1=dict(name="Mustafa",surname="Köse")

print(type(dictionary))
dict_list.append(dictionary)
dict_list.append(dictionary1)
dict_list.append(dict())
dict_list.append(dict(name="Selçuk",surname="Karaman"))
dict_list.append(ElectricCar("Tesla", "Model 3", 75))
print(dict_list)

try:
    dict_list.append("Kamil")
except TypeError as e:
    print(f"dict-list----> Error:{e}")




    

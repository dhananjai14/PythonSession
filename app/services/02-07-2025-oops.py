# Instance method 

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print("ANIMAL CREATED")

#     def who_am_i(self):
#         print(self.name)
#         self.name = "NEWNAME defined"
#         print(f"I am an animal. My name is {self.name}")

#     def eat(self):
#         print("I am eating")

# animal_obj = Animal(name = "Dog")
# animal_obj.who_am_i()


# class method 

# class Animal:
#     animal_count = 0 # Class variable 
#     def __init__(self, name):
#         self.name = name
#         print("ANIMAL CREATED")
#         Animal.animal_count = Animal.animal_count + 1
        
#     def who_am_i(self):
#         print(self.name)
#         self.name = "NEWNAME defined"
#         print(f"I am an animal. My name is {self.name}")

#     def eat(self):
#         print("I am eating")

#     @classmethod
#     def get_total_count_animal(cls):
#         print(f"TOtal number of animals {Animal.animal_count}")

# animal_obj = Animal(name = "Dog")
# animal_obj = Animal(name = "Cat")
# animal_obj = Animal(name = "Fish")
# Animal.get_total_count_animal()


# Static method 

# class Calculator:
#     @staticmethod
#     def add_num(num1,num2):
#         return num1+num2
    
#     @staticmethod
#     def get_mul(num1,num2):
#         return num1*num2
    
# print(Calculator.add_num(10, 10))
# print(Calculator.get_mul(10,10))


# Encaptulation

# Public 
# Protected (_)
# class Emp:
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary 
        
#     def _get_salary(self):
#         return self._salary

#     def tax_to_pay(self):
#         salary = self._get_salary()
#         return salary * .1

# emp_obj = Emp("ABC", 1000)
# print(emp_obj._get_salary())

# Private (__)
# class Emp:
#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary 
        
#     def __get_salary(self):
#         return self._salary

#     def tax_to_pay(self):
#         salary = self.__get_salary()
#         return salary * .1

# emp_obj = Emp("ABC", 1000)
# print(emp_obj._Emp__get_salary())


class calculator:
    def add_num(self, *args):
        return sum(args)
    
calculator_obj =calculator()
print(calculator_obj.add_num(2,3,5, 4))

# *args **kwargs 



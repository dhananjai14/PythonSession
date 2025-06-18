# def sum_num(num1, num2):
#     return num1+num2

# print(sum_num(1,2))

# def sum_num(num1, num2, num3 = 0, num4 = 0, num5 = 0):
#     return num1+num2+num3+num4+num5

# print(sum_num(1,2,3))
# print(sum_num(1,2,3,4,5))

# def sum_num(*args):
#     print(type(args))
#     return sum(args)

# print(sum_num(1,2,3,4,5,6,7))
# # print(sum_num(1,2,3,4,5,6,7,8,9))
# # print(sum_num(1,2,3))
# # print(sum_num(1,2,3,4,5))
# # print(sum_num(1,2))


# def sum_num(*xyz):
#     print('from XYZ')
#     print(type(xyz))
#     return sum(xyz)

# print(sum_num(1,2,3,4,5,6,7))

# def take_name_age(name, age):
#     return f"name is {name} and age is {age}"

# print(take_name_age(name = "dhan", age = 20))



# def take_name_age(name, age, **kwargs):
#     if not type(kwargs['lives']) is int:
#         return "Lives should be an int"
#     return f"name is {name} and age is {age}. Lives in {kwargs['lives']}"


# print(take_name_age(name = "dhan", age = 20, company = "ABC"))


# def sample_function( *args, **kwargs ):
#     tuple_sum = sum(args)
#     name = kwargs['name']
#     return f"sum = {tuple_sum} name = {name}"

# print(sample_function(  1,2,3,4,5,6, name = "ABC"))



# Object oriented programming in python 

# class MyFirstClass:
#     def initialize(self):
#         print("my class has been initialized")
#     pass

# class_obj = MyFirstClass


# class MyFirstClass:
#     def __init__(self):
#         print("my class has been initialized")
    

# class_obj_1 = MyFirstClass()
# class_obj_3 = MyFirstClass()
# class_obj_2 = MyFirstClass()



class CreateBuilding:
    def __init__(self,cement, water):
        self.cement = cement
        self.water = water
        print("my class has been initialized")
    

class_obj_1 = CreateBuilding("cement", 'water')
class_obj_3 = CreateBuilding("cement", )
class_obj_2 = CreateBuilding()

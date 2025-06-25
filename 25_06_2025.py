class Animal:
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog Created")

#     def who_am_i(self):
#         Animal.who_am_i(self)
#         print("I am a Dog")

# class Cat(Animal):
#     def __init__(self):
#         print("I am cat")
    
#     def who_am_i(self):
#         print("I am a Cat")


# class Animal:
#     def eat(self):
#         print("I am eating")


# class Dog(Animal):
#     def __init__(self):
#         print("Dog Created")

#     result = Animal().eat()
#     # def who_am_i(self):
#     #     Animal.eat(self)
#     #     print("I am a Dog")

# dog_obj = Dog()
# dog_obj.eat()



class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        Animal.who_am_i(self)
        print("I am a Dog")

class Cat(Animal):
    def __init__(self):
        print("I am cat")
    
    def who_am_i(self):
        print("I am a Cat")


cat_obj = Cat()
dog_obj = Dog()

dog_obj.who_am_i()
cat_obj.who_am_i()


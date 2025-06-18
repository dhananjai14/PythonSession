# Function 

""" Syntax
def function_name(parameters):
    code processing
    return result

"""


# def greet_python():
#     """
#     This function return Hello World.
#     Args:

#     Return:
#         Hello WOrld
#     """
#     print("Hello World")
#     return "Hello World"

# greet_python()

# def greet_python(name:str ):
#     """
#     This function return Hello Name.
#     Args:
#         name: Take only string as input. 

#     Return:
#         None
#     """
#     print(f"Hello {name}")

#     # return "Hello World"


# sample_result = greet_python(name = 1)

# print(sample_result)



def greet_python(name:str = "Default Value" ):
    """
    This function return Hello Name.
    Args:
        name: Take only string as input. Defalute value is "Default Value"

    Return:
        None
    """
    print(f"Hello {name}")

    # return "Hello World"


# sample_result = greet_python()
# print(sample_result)
# sample_result = greet_python(name = "User name")
# print(sample_result)

# NOTE: Python is dynamically typed:

def add_number(a:int, b:int):
    if type(a) is str:
        return "a must be an integer"
    sum: int = a + b
    return sum

# result = add_number(a = 1, b= 2)
# print(result)
# result = add_number(a = "1", b= "2")
# print(result)


def add_number(a:int, b:int) -> int:
    if type(a) is str:
        return "a must be an integer"
    sum: int = a + b
    return sum

result = add_number(a = 1, b= 2)
print(result)
result = add_number(a = "1", b= "2")
print(result)


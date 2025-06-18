# Python practice questions 

# def evenNumbersList(inputList:list) -> list:
#     outputList = []
#     for itm in inputList:
#         if(itm%2 == 0):
#             outputList.append(itm)
#     return outputList


# def number_is_even(number: int) -> bool:
#     if number % 2 == 0:
#         return True
#     else: return False 

# given_list = [1,2,3,4,5,6,7,8]
# result = [itm for itm in given_list if number_is_even(itm)]

# print(result)



# def number_is_even(number: int) -> bool:
#     if number % 2 == 0:
#         return True
#     else: return False 

# def return_even_number_list(my_list: list) -> list:
#     even_list = []
#     for itm in my_list:
#         if number_is_even(itm):
#             even_list.append(itm)
#         else: 
#             pass
#     return even_list

# given_list = [1,2,3,4,5,6,7,8]

# print(return_even_number_list(given_list))


def is_number_not_prime(num: int) -> bool:
    """Check if prime
    Args:
        num
    Returns:
        bool
    """ 
    if num <= 0:
        return False
    if num == 1:
        return True
    if num == 2:
        return False
    if num % 2 == 0:
        return True
    if num % 3 == 0:
        return True
    
    for i in range(3, int(num**.5 +1), 2):
        if num/i == 0:
            return True
    
    return False

print(is_number_not_prime(100))  


# Ques  add nuber 4 different number

# def num_sum(num1, ... ):
#     result  = num1
#     return   

    





# 1. num > 0
# 2. num not be even 
# 3. num not divisible by 3
# 4. 10  -> num / 2 
# 4. 3 to sqrt(num)
# 5  num == 1 -> not a prime 
# 6. num == 2 -> prime





# *args and **kwargs



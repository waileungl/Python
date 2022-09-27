# for x in [0, 1, 2]:
#     pass

# print("hello!")


# tuple1 = ["abc", "male"]

# print(type(tuple1))

# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))




# number = 3
# print(f"My name is {number}")

# import random

# print('Welcome to Python!')

# print('This is a loop printing 5 times')
# for x in range(1, 6):
#     print(f'x is: {x}')

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# day = random.choice(weekdays)

# print(f'Today is: {day}')

# if day == 'Monday':
#     print('It will be a long week!')
# elif(day == 'Friday'):
#     print('Woohoo, time for the weekend!')
# else:
#     print('Not quite there yet.')

# print(type(22))

# str(22)

# print(type(str(22)))



# age = 26
# first_name = "William"
# last_name = "Liu"

# #print(f'my name is {first_name} {last_name}, and I am {age} years old')

# print('my name is ' + first_name + last_name + ', and I am ' + str(age))

'''
x = "hello worldsss wwwa32 44 3w 4wed"
print(x.find('s'))
'''

'''
list = [1,1,2,3,4,'5,5,5','5','5','6','你','你',7,8]
set = set(list)
print(set)
'''

# person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} 
# person['eye_color'] = 'blue' 

# print(person)

# pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# print(pizza_toppings[7])

# pizza_toppings.pop(1)

# print(pizza_toppings)

# person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# print(person['favorite_team'])

# fruit = ('blueberry', 'strawberry', 'banana')

# fruit.append('raspberry')

# fruit[0] = 'cranberry'

# boolean = 'False'

# print(boolean)


# vegetables = ['lettuce', 'cucumber', 'carrots', 'a', '99']

# vegetables.reverse()
# print(vegetables)

from email.policy import default


some_nums = [44,56,2,3,12,19,6]
print("Get started by writing your own code!")

# Some optional challenges to assess and refine your understanding:

# Print the length of the list.
# count = 0
# for i in some_nums:
#     count += 1
# print(count)

# # Use antoher python built-in function and print the result.
# print(len(some_nums))

# Remove an item from the list. Remember to verify that it was removed.
# some_nums.pop(1)

# def verify(array):
#     verify = 0
#     for i in array:
#         if(i == 56):
#             verify += 1
#             print(False)
#     if(verify == 0):
#         print(True)

# # Utilize a method from the documentation and print the result.

# verify(some_nums)


# myTuple = 1,

# print(type(myTuple))

# x = [5,'s',10,1,6]

# for i in x:
#     print(i)

# countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# # Challenge 1: Fix the range!
# for integer in range(0, len(countries)):
#     print("Index:", integer)
#     # Challenge 2: print the index here
#     print("Country:" + countries[integer])
#     # Challenge 3: print the country here

# # Looping over values only...
# for country in countries:
#     print("Country: " + country)
#     # Challenge 4: print the country here


#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!

# def full_name(nam1, nam2):
#     return nam1 + " " + nam2

# name1 = full_name("Eddie", "Aikau")
# print(name1) # should print Eddie Aikau

myDic = {}
myDic["A"] = 1
myDic["B"] = 2
myDic['C'] = 3

print(myDic)

# print(myDic.pop('A'))

print(myDic.get("d"))

print(len(myDic))


num1 = 42 #variable declaration - integer
num2 = 2.3 #variable declaration - float
boolean = True #variable declaration - boolean
string = 'Hello World' #variable declaration - string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #lists
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionaries
fruit = ('blueberry', 'strawberry', 'banana') #tuples
print(type(fruit)) #type define
print(pizza_toppings[1]) #output = Sausage
pizza_toppings.append('Mushrooms') #push string 'Mushrooms' into the list
print(person['name']) #output = John
person['name'] = 'George' #change the corresponding value of name to 'George'
person['eye_color'] = 'blue' #push 'eye_color': 'blue' to the dictionaries"person"
print(fruit[2]) #ouput = banana

if num1 > 45:
    print("It's greater")
else:
    print("It's lower") #output

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!") #<-- this is output,len(string) = 11 (space is also considered as a character)


for x in range(5): 
    print(x) #output = 01234
for x in range(2,5):
    print(x) #output = 234
for x in range(2,10,3):
    print(x) #output = 2, 2+3, 2+3+3 = 258
x = 0
while(x < 5):
    print(x) #output = 01234
    x += 1

pizza_toppings.pop() #last element of the list is removed
pizza_toppings.pop(1) #second element of the list is removed

print(person)
person.pop('eye_color') #'eye_color': 'blue' is removed
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue #skipped
    print('After 1st if statement') #print 3 times for Sausage, Jalepenos, Cheese
    if topping == 'Olives':
        break #exit the for loop

def print_hello_ten_times(): #the function that print 'Hello' 10 times is defined
    for num in range(10):
        print('Hello') 

print_hello_ten_times() #call the function, 'Hello' will be printed for 10 times

def print_hello_x_times(x):  #the function that print 'Hello' x times is defined
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #call the function with parameter 4, that mean there are 4 'Hello' would be printed out

def print_hello_x_or_ten_times(x = 10): #the function that print 'Hello' 10 times is defined
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #'Hello' will be printed for 10 times
print_hello_x_or_ten_times(4) #'Hello' will be printed for 4 times


"""
Bonus section
"""
#print(num3) #num3 is not defined yet
num3 = 72 
fruit[0] = 'cranberry' #the items in tuple are unchangeable
print(person['favorite_team']) #no such key, so key error
print(pizza_toppings[7]) #list index out of range
print(boolean) #output = True
fruit.append('raspberry') #we cannot add items after the tuple has been created
fruit.pop(1) #we cannot remove items after the tuple has been created
x = y = z = 'Orange'
print(x)
print(y)
print(z)

#testing multiple assignments of variables     
j = "gguhruh"
print(j)

#testing for single global variable
f = 'frog'
def my_funtion():
    print("this is a " + f)
    my_function()

#testing multibl global variables 
c = 'twist'
def my_function():
    c = 'ball'
    print('This is me ' + c)
my_function()
print(c)

x = 5
#used for checking the type of variable
print(type(x))

#testing types of numbers 
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#trying convertion of types numberrs
x = 7 #int
y = 3.52 #float
z = 5j #complex

a = float(x)
b = int(x)
c = complex(x)
print(a)
print(b)
print(c)

#testing the random function type
import random
print(random.randrange(1, 11))

for j in 'goat':
    print(j)

d = 'duckling'
print(len(d)) 

v = 'Victor is a good guy'
print( 'goods' in v)

q = 'life is like a banana'
print(q[5:2])
##
#
squares = []
for x in range(10):
    squares.append(x**2)

squares

last_name = 'Adiat'
food = 'beans'
print(f"My last name is {last_name} and I love {food}.")

# testing out random ideas 
g = 53 
h = 58
j = 20
result = (h + j) * g * 2
print(result)

#testing the logic of slicingn and replacing strings
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#test 2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)

def func():
    z += 1
    print(z)
func()
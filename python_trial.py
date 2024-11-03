print("Hello, World!")
#print statement
#variables
"""
This is a comment
written in
more than just one line
"""
a = 5
b = "Hello, World!"
print(a)
print(b)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(type(x))
print(type(y))
print(type(z))

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)

x = 5
y = "John"
print(x, y)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

myfunc()

print("Python is " + x)

if 5 > 2:
 print("Five is greater than two!")  
if 5 > 2:
        print("Five is greater than two!") 

PYTHON FUNDAMENTALS / PYTHON BASICS / VARIABLES
- Variables
- Data Types (int, float, str, bool, None)
- Operators
- Input & Output
- Type Casting
- Strings
- Lists
- Tuples
- Sets
- Dictionaries


print("hello world!")
# print("hello world!")
# print("hello world!")
# print("hello world!")

'''
print("hello world!")
print("hello world!")
print("hello world!")
print("hello world!")
'''


#  ******************** VARIABLES ********************

a = 3
print(a)

b = 55
print(b)

a = 6.5
print(a)

c = True
print(c)

d = "Ayush"
print(d)

e = None
print(e)

a, b, c = 1, 2, 3
print(a, b, c)

x = y = z = 100
print(x, y, z)


x = 10
print(type(x))

a = 10
b = 20
a, b = b, a
print(a,b)

# x = 100
# del x
# print(x)

a = 100
b = a
print(b)


# Key Takeaways
# A variable is a name that refers to a value (object).
# Use = to assign a value.
# Python is dynamically typed, so you don't declare variable types.
# Follow snake_case naming conventions.
# Use type() to check an object's type.
# Multiple variables can refer to the same object.
# Variables must be assigned before they are used.



********************************************************************************************************************************************************************



For a Python developer (backend/fresher job), you've covered about 95% of what you need to know about variables.
The remaining 5% is slightly more advanced and is usually asked in interviews. Here it is:

************* 1. ---------> Object Identity (id()) ********************************

Every object in Python has a unique identity.

x = 10
print(id(x))

Output (will vary):
140727338974024

id() returns the memory identity of the object (implementation-dependent, but often related to its memory address in CPython).

Example:

a = 10
b = 10

print(id(a))
print(id(b))

For small integers, you'll often see the same id because Python reuses certain immutable objects.



************ 2. ---------> Reference vs Copy ***********************************
a = [1, 2, 3]
b = a

b.append(4)

print(a)

Output:

[1, 2, 3, 4]

Why?

Because a and b refer to the same list.


****************  3. ---------> Mutable vs Immutable (Very Important) *************************************************

This is one of the most frequently asked interview topics.

Immutable objects cannot be changed:

x = 10

x = 20

You didn't change 10; you made x refer to a new integer object 20.

Mutable objects can be modified:

numbers = [1, 2, 3]

numbers.append(4)

The existing list itself changes.

You'll study this in detail when learning lists and tuples.


*************************** 4. --------->  Constants **********************************************************************************

Python doesn't enforce constants, but by convention we use uppercase names.

PI = 3.14159
MAX_USERS = 100

This tells other developers these values should not be changed.


*************************  5. ---------> Keywords Cannot Be Variable Names *******************************************************

These are reserved words in Python.

❌ Invalid:

class = 10

✅ Valid:

class_name = "Python"

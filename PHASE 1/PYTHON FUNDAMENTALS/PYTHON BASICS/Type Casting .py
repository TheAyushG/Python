***************** Type casting is the process of manually converting one data type into another data type. ********************

**

---> if we write this code like this then it will give us a error becasue we are adding 1 in a stirng, so we can't add string and a number 
f = "6"
print(f + 1)

----> but if we want to add the number and the string, so firstly we have to change the string into the int, like this below code
f = "6"
print(int(f) + 1)


g = 5
print(g + 1)


****************************************************************************** GPT Explnation ***********************************************************************************

Why Do We Need Type Casting?
Sometimes the data we have is not in the format we need.

**** Example: ****

age = "22"
Here, age is a string, not a number.

If you want to perform arithmetic:
print(age + 5)

You'll get an error:
TypeError: can only concatenate str (not "int") to str

Why?
Because Python cannot add a string and an integer.

So we convert the string to an integer.
age = int(age)

print(age + 5)
Output:
27



Common Type     Casting Functions
Function	      Converts To
int()	          Integer
float()        	Float
str()	          String
bool()	        Boolean
list()	        List
tuple()	        Tuple
set()         	Set
dict()	        Dictionary (only from valid key-value data)

The first four are the ones you'll use most often.



***********  ----> 1. String to Integer **********

age = "22"
print(type(age))

age = int(age)
print(type(age))

Output:
<class 'str'>
<class 'int'>


***********  ----> 2. Integer to Float ***********

num = 10
num = float(num)

print(num)
print(type(num))

Output:
10.0

<class 'float'>
Notice that 10 became 10.0.

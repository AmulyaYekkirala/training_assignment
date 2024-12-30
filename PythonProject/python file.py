#Sum of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter  second number: "))
print("Sum:", a + b)


#Find the Largest Number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Largest:", max(a, b))


#Check Even or Odd
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")


#Print Fibonacci Sequence
n = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#version 2
n = int(input("Enter number of terms"))
a = 0
b= 1
for i in range(n):
    print(a, end=" ")
    temp = a
    b = a+b


# Check Prime Number
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


#Find HCF (GCD)
a = int(input("Enter first number: ")) #20
b = int(input("Enter second number: ")) #40
while b:
    a, b = b, a % b
print("HCF:", a)


#Find HCF (GCD) - version 2
a = int(input("Enter first number: ")) #20
b = int(input("Enter second number: ")) #40
while a:
    a, b = b%a, a
print("HCF:", b)


#Find LCM
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
lcm = abs(a * b) // gcd(a, b)
print("LCM:", lcm)


#Reverse a Number
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed:", rev)

num = int(input("Enter a number: "))
original_num = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
if original_num == rev:
    print(f"{original_num} is a palindrome")
else:
    print(f"Reversed: {rev}")


#Check Palindrome Number
num = input("Enter a number: ")
print("Yes it is Palindrome" if num == num[::-1] else "Not Palindrome")


#Calculate Factorial
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial:", factorial)


#Sum of Digits
num = int(input("Enter a number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)


#Count Digits in a Number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)


#Check Armstrong Number
num = int(input("Enter a number: "))
order = len(str(num))
sum_of_powers = sum(int(digit)**order for digit in str(num))
print("Armstrong" if num == sum_of_powers else "Not Armstrong")


#Print Multiplication Table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


#Print All Factors of a Number
num = int(input("Enter a number: "))
factors = [i for i in range(1, num + 1) if num % i == 0]
print("Factors:", factors)


#Generate a Star Pattern
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)


#Write a program to input your name and print a greeting message.
name=input("enter your name")
print("hello" + name + "have a nice day")

#Write a Python program to take two numbers as input and print their sum
num1=int(input("enter first number"))
num2=int(input("enter second number"))
sum_result=num1+num2
print(sum_result)


print("prime numbers below 100 are:")
for i in range(2,100):
    if all(i % x != 0 for x in range(2, int(i ** 0.5) + 1)):
        print(i,end=" ")
#2
print("prime numbers below 10 are:")
for i in range(2,10):
    if all(i % x != 0 for x in range(2, int(i ** 0.5) )):
        print(i,end=" ")

#if condition
x = 10
if x > 5:
    print("x is greater than 5")# o/p x is greater than 5

#if else
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5") #o/p x is not greater than 5

#elseifladder
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 50:
    print("Grade: E")
else:
    print("Grade: F")

#nested if
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible based on age.")
    experience = int(input("Enter your years of experience: "))
    if experience >= 2:
        print("You are eligible for the competition!")
    else:
        print("You need at least 2 years of experience to participate.")
else:
    print("You must be at least 18 years old to participate.")

#numeric type
from enum import nonmember

x = 10
print(type(x))

y = 3.14
print(type(y))

z = 2 + 3j
print(type(z))

#sequence#string
text = "Hello, World!"
print(type(text))

#list
fruits = ["apple", "banana", "cherry"]
print(type(fruits))

#tupple
numbers = (1, 2, 3)
print(type(numbers))

#mapping type#dictionary
person = {"name": "John", "age": 25}
print(type(person))

#set types#frozen
unique_numbers = {1, 2, 3, 3}
print(type(unique_numbers))

#frozen set
frozen_numbers = frozenset([1, 2, 3])
print(type(frozen_numbers))


#boolean
a = 10
b = 20
result = a < b
print(result)

#bytes
data = b"hello"
print(type(data))

#bytearray
ba = bytearray(b"srinu")
ba[0] = 74
print(ba)

#memory view
data = memoryview(b"srinu")
print(data)
#22
b_data = memoryview(b"srinu")
mv = memoryview(b_data)
print(mv[0])

#none type
def my_function():
    pass
result = my_function()
print(result)

if not None:
    print("None is False")

# Loop from 1 to 5 (i value immutable)
for i in range(1, 6):
    print(i)



#for loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


#for loop with tuple
x='ammu'
for i in x:
    print(i)

#loop from 11 to 20
for i in range(11,21,3):
    print(i)


#for to get values reverse
for i in range(21,11,-1):
    print(i)


#for loop to get only  divisible with 5
for i in range(10,21):
    if i%5==0:
        print(i)


#for loop not divisible by 5
for i in range(10,21):
    if i%5!=0:
        print(i)


#sum of elements in list
numbers = [1, 2, 3, 4, 5]
s=0
for i in numbers:
    s+=i
print("Total with for loop:", s)
total =sum(numbers)
print('Total sum with sum function:', total)


#nested for loop to mutlipy table
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

# logical keywords
#and
a=10
b=20
if a>5 and b>15:
    print("a is greater than b")

# OR
a=10
b=20
if a>5 or b>15:
    print('at least one condition is true')

#not
a=False
if not a:
    print("a is false")

#conditional keywords
#if
x=5
if x>2:
    print("x is greater than 2")

#else
if x>10:
    print("x is greater than 10")
else:
    print("x is less than 10")

#elif
if x>20:
    print("big")
elif x>30:
    print("small")
else:
    print("extra small")

#loops
#for
a = 10
for i in range(a):
    print(i)


#while
k=1
while k>10:
    print(k)
    k=k+1

#in
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#error handling
#try
try:
    num = int(input("Enter a number: "))
    print(f"Square of the number is {num ** 2}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

#expect
try:
    num = int("abc")
except ValueError:
    print("Invalid input! Please enter a number.")


#finally
try:
    f = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution finished.")

#def
def greet(name):
    print(f"Hello, {name}!")

#return
def add(a, b):
    return a + b

result = add(3, 7)
print(result)


#import
import random

print(random.randint(1, 10))


# class
class Animal:
    def sound(self):
        print("This animal makes a sound.")

cat = Animal()
cat.sound()


#from

from math import sqrt

print(sqrt(16))


#as
array = np.array([1, 2, 3])
print(array)

#True
is_valid = True
if is_valid:
    print("The value is true!")

#False
is_ready = False
if not is_ready:
    print("The value is false!")

#None
x = None
if x is None:
    print("x is None!")

#is
a = None
if a is None:
    print("a is None!")

#lambda
multiply = lambda x, y: x * y
print(multiply(4, 5))

#with
with open("sample.txt", "w") as file:
    file.write("Hello, world!")

#global
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)

#nonlocal
def outer_function():
    value = 5

    def inner_function():
        nonlocal value
        value += 1
        return value

    return inner_function()

print(outer_function())

# creating
x = list()
print(x)   # o/p []

x = []
print(x)  # o/p []

# length
x = ["apple", "banana", "cherry"]
print(x)
print(len(x))

# type
x = [5, 2.5, True, "apple", "apple"]
print(type(x))

# indexing
x = [5, 2.5, True, "apple"]
print(x[-1])

# slice
x = [5, 2.5, True, "apple"]
y = x[1:3]
print(y)  # o/p [2.5,True]

# append
x = [5, 2.5, True, "apple"]
x.append(7)
print(x)  # o/p [5,2.5,True,"apple",7]

# insert
x = [5, 2.5, True, "apple"]
x.insert(1, "banana")
print(x)   # o/p [5,banana,2.5,True,"apple"]

# EXTEND
x = [5, 2.5, True, "apple"]
y = [2, 3, "banana"]
x.extend(y)
print(x)  # o/p [5,2.5,True,"apple",2,3,"banana"]

# remove (removes specified item)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # o/p ["apple","cherry"]

# pop (removes item at particular index)
x = [5, 2.5, True, "apple"]
x.pop(1)
print(x)  # o/p [5,True,"apple"]

# sort
x = [5, 2]
x.sort()
print(x)  # o/p [2,5]

x = ["apple", "mango", "banana"]
x.sort(reverse=True)
print(x)  # o/p ["mango","banana","apple"]

# reverse
x = [5, 2.5, True, "apple"]
x.reverse()
print(x)  # o/p ["apple",True,2.5,5]

# split
x = " ammu is a student"
y = x.split()
print(y)

# join
x = ["Durga", "mam", "is", "our", "trainer"]
y = " ".join(x)
print(y)

# count
x=[5, 6, 6, 7, 7, 8, 9]
y=x.count(2)
print(y)  # o/p 0

# index
x=[5, 6, 6, 7, 7, 8, 9]
print(x.index(6))   # o/p 1

# tuple creating
x=()
print(x)     # o/p ()

x=tuple()
print(x)         # o/p ()
print(type(x))   # o/p <class "tuple">

# length
x=(1,2,2.5,True,"hi")
print(len(x))    # o/p 5

# changing values by converting to list
x = ("apple", "banana", "cherry", "apple")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)    # o/p ("apple", "kiwi", "cherry", "apple")

# add tuple to a tuple
x = ("apple","banana","cherry")
y=(True,"hi")
x+=y
print(x)    # o/p ("apple","banana","cherry",True,"hi")

# count
x = ("apple", "banana", "cherry", "apple")
y=x.count("apple")
print(y)    # o/p 2

# index
x = ("apple", "banana", "cherry", "apple")
print(x.index("apple")) # o/p 0

list = [1, 2, 3, 4]
list.remove(2)
del list[1]
popped = list.pop(0)
print(list)
#creating a and b variables
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)


#comparision operators
a=10
b=20
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

#logical operators
a=True
b=False
print(a and b)
print( a or b)
print(not a)
print(not b)

#assignment operators
a = 10
a -= 3
a *= 2
a /= 4
print(a)
print("final value of a:",a)

#bitwise operators
a = 8 #1000
b = 5 #0101
and_result = a & b
or_result = a | b
not_result = ~a
xor_result = a ^ b
leftshift_result = a << b
rightshift_result = a >> b
print(and_result, or_result, not_result, xor_result, leftshift_result, rightshift_result)

#create a list
my_list = [1,2,3,'ammu','hema']
a=(1,2,3,'ammu','hema')
b=[1,2,3,'ammu','hema']
identity_check_is = (a is my_list)
identity_check_is_not = (b is not my_list)
check_in = 2 in my_list
check_not_in = "ammu"  in my_list
check_not_in = "balu" in my_list

#code to print a name 100 times
name=input('enter your name')
for _ in range(100):
    print(name)

#to check number even or odd
num=int(input("enter a number"))
print("even" if num%2==0 else "odd")

#print 7th table
for i in range(1,11):
    print(f"7*{i} = {7*i}")

#comparasion of 2 num check weather which variable is minimum and maximum
num1=24
num2=10
largest=max(num1,num2)
smallest=min(num1,num2)
print("max num is ",largest,"min num is",smallest)

#find largest of 3 numbers
num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
largest=max(num1,num2,num3)
print(largest)

#list
list1 = [1, 2, 3, 5, 6]
list2 = [4, 5, 6, 3, 2, 1]
intersect = set(list1) & set(list2)
print("Intersection of the lists:", intersect)


#palindrome
num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#string
str1="hello"
str2="amulya"
common_char=set(str1)&set(str2)
print(common_char)

#programme to find the longest word in given list of words
#count the words
file=open("amulya.txt","r")
content = file.read()
words = content.split()
wordcount=len(words)
print("the num of words in the file is:")
print(wordcount)

#Write a program to calculate the area of a circle given its radius.
#circle formula=3.14*r*r
diameter = int(input("Enter the diameter of the circle: "))
radius = diameter / 2
area_of_circle = 3.14 * radius ** 2

print("The area of the circle is:", area_of_circle)

##Reverse a string without using slicing (e.g., "hello" -> "olleh").
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
input_string = "hello"
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)

#Lists: Write a program to find the largest number in a list.
def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
numbers = [1,2,3,4,6]
largest_numbers = largest_number(numbers)
print(largest_numbers)

#largest string in list
def largest_string(strings):
    largest = strings[0]
    for string in strings:
         if string > largest:
             largest = string
    return largest
strings = ["hellobaby","amulyayekkirala","myworld"]
largest_strings = largest_string(strings)
print(largest_strings)
print(strings)
print([x for x in strings if len(x)==max([len(x) for x in strings])])



longest_length = 0
    for string in strings:
        if len(string) > longest_length:
            longest_length = len(string)
    return longest_length

strings = ["hellobaby", "amulyayekkirala", "myworld"]
longest_length = longest_string_length(strings)
print(longest_length)

def longest_string_length(strings):
    longest_length = 0
    for string in strings:
        if len(string) > longest_length:
            longest_length = len(string)
    return longest_length

strings = ["hellobaby", "amulyayekkirala", "myworld"]
longest_length = longest_string_length(strings)
print(longest_length)

strings=["hello","ammu","world"]
largest_string=max(strings ,key=len)
print(largest_string)


# LIST:
list_names = ["Ammu", "bunny", "Madhu"]
print(", ".join(list_names))

# Duplicates:
list_a = ["Amulya", "Rachana", "Madhu", "Archana"]
print(list_a)

# List Length:
names = ["Ammu", "Rachana", "bunny"]
print(f"The number of names in the list is: {len(names)}")

# List Items - Data Types:
# List of strings
list1 = ["Ammu", "Rachana", "bunny"]

# List of integers
list2 = [1, 5, 7, 9, 3]

# List of booleans
list3 = [True, False, False]

# Printing the lists
print("List of Strings:", list1)
print("List of Integers:", list2)
print("List of Booleans:", list3)

# Access Items:
# List of fruits
thislist = ["apple", "banana", "cherry"]
# Print the second item of the list
print(thislist[1])  # Output: banana

# DICTIONARY:
a = {'a': 123456, 1: 'abc'}
print(a)
# Output: {'a': 123456, 1: 'abc'}

# get()
my = {'a': 1, 'b': 2, 'c': 3}
print(my.get('b'))  # Output: 2
print(my.get('d'))  # Output: None

# update()
k = {'a': 1, 'b': 2}
k.update({'b': 10, 'c': 3})
print(k)
# Output: {'a': 1, 'b': 10, 'c': 3}

# pop()
amulya = {'a': 1, 'b': 2, 'c': 3}
value = amulya.pop('b')
print(value)  # Output: 2
print(amulya)  # Output: {'a': 1, 'c': 3}

# popitem()
h = {'a': 1, 'b': 2, 'c': 3}
key_value_amulya = h.popitem()
print(key_value_amulya)  # Output: ('c', 3)
print(h)  # Output: {'a': 1, 'b': 2}

# values()
my_dict = {'a': 1, 'b': 2, 'c': 3}
values = my_dict.values()
print(list(values))  # Output: [1, 2, 3]

# keys()
keys = my_dict.keys()
print(list(keys))  # Output: ['a', 'b', 'c']

# items()
items = my_dict.items()
print(list(items))  # Output: [('a', 1), ('b', 2), ('c', 3)]

# SET:
# Set example
amulya = {1, 2, 8, 4, 2}
k = set(amulya)
print(k)  # Output: {1, 2, 8, 4}

# Add()
my = {1, 2, 3}
my.add(4)
print(my)  # Output: {1, 2, 3, 4}

# Clear()
my1 = {1, 2, 3}
my1.clear()
print(my1)  # Output: set()

# Copy()
a = {1, 2, 3}
new = a.copy()
print(new)  # Output: {1, 2, 3}

# Difference
set1 = {1, 2, 3}
set2 = {3, 1, 5}
print(set1.difference(set2))  # Output: {2}

# Discard()
my1 = {1, 2, 3}
my1.discard(2)
my1.discard(4)
print(my1)  # Output: {1, 3}

# Intersection()
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2))  # Output: {2, 3}

# isdisjoint()
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True

# pop()
lucky = {1, 2, 3}
element = lucky.pop()
print(element)
print(lucky)  # Remaining set after pop

# Remove()
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

# Symmetric difference()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}

# Union
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}

# Update()
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}

# Length
b = {1, 2, 3, 4}
print(len(b))  # Output: 4

# Max()
amulya = {10, 20, 5, 7}
print(max(amulya))  # Output: 20

# Sorted()
j = {3, 1, 4, 2}
print(sorted(j))  # Output: [1, 2, 3, 4]

#create list
my_list = [1,2,3,4]

#access the list
first_element = my_list[0]
second_element = my_list[1]
third_element = my_list[2]
fourth_element = my_list[3]

#change the list item
my_list[3]=2

#try to replace the values
my_list=[1,2,3,4]
index_to_replace = 3
new_value = 30
my_list[index_to_replace] = new_value
print(my_list)

#perform append operators
my_list=[1,2,3,4]
my_list.append=4
print(my_list)

#try to insert new items to list
my_list=[1,2,3,4]
(my_list.insert(5,6))

#extend your items to a list
# Example: Using extend()
my_list = [1, 2, 3]
new_items = [4, 5, 6]

my_list.extend(new_items)

print(my_list)

#remove an item from list
my_list = [1, 2, 3]
my_list.remove(3)
print(my_list)

#clearing the entire list
my_list = [1, 2, 3]
my_list.clear()
print(my_list)

#open file
file=open("amulya.txt","r")
content=file.read()
print(content)
file.close()

#Writing file
file = open("amulya.txt", "w")
file.write("Hello world\n")
file.close()

#appending a file
file = open("amulya.txt","a")
file.write("i love python")
file.close()

#closingfile
file.close()

#checking if file exists
import os
if os.path.exists("amulya.txt"):
    print("file exists")
else:
    print("file does not exists")





























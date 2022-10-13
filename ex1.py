#Write a program to print numbers from 1 to 10.
#for loop
for i in range (1,11):
    print (i)


#while loop
i = 0
while i <= 10:
    print(i)
    i += 1

#ex2
#Write a program to calculate the sum of 1 to 10.
#while loop
i = 1
a = 0
while i <= 10:
    a += i
    i += 1

print("the total sum is" , a)

# #for loop
i = 1
a = 0
for i in range (1,11):
    a += i
    print(a)

#ex 3
#Write a program to calculate the factorial of a number.
# for loop
num = int(input("enter a number"))
b = 1
for i in range(num,1,-1):
    b = i * b

print("Total",b)

# while loop
num = int(input("enter a number"))
c = 1
while num >= 1:
    c = c * num
    num = num - 1
print("total", c)

#ex4
#Write a program to Sum of squares of first n natural numbers.
#for loop
sum = 0
user = int(input("enter a number"))
for i in range(user,0,-1):
    sum += i**2
print(sum)

#while loop
var = 1
sum = 0
user = int(input("enter a number"))
while var <= user:
   sum += var ** 2
   var += 1
print("total", sum)

#ex 5
#Write a program to nth multiple of a number in Fibonacci Series.
n = int(input("enter a number: "))
a, b = 0, 1

for n in range(1, n + 1):
    #next_num = a + b
    print(b)
    a, b = b, a+b

#ex 6
#Write a program to check whether a number is Prime or not from 1 to 10.

for i in range (2, 11):
    for j in range(2,i):
        if i%j == 0:
            print(i, "is not a  prime number")
            break


# ex7
#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700.

lower_limit = 1500
upper_limit = 2700

for i in range(lower_limit, upper_limit+1 ):
    if(i%7 == 0 and i%5 == 0):
        print("the number divisible by 7 and multiple of 5 are : ",i)

#while condition
i = lower_limit
while i <= upper_limit:
    if (i%7 == 0, i%5 == 0):
        print("The number divisible by 7 and mutiple of 5 are :",  i)
        i += 1


# ex 8

# number = [1,2,3,4,5,6,7,8,9,10]
# even_count = 0
# odd_count = 0
# num = 0
# while (num<len(number)):
#     if number[num]%2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#         num += 1
#         print("even number are", even_count)
#         print("odd number are",odd_count)

#ex9:
#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(7):
    if(i==3 or i==6):
        continue
    print(i)


#ex:10

#Write a Python program to get the Fibonacci series between 0 to 50.

a = 0
b = 1
while b<50 :
    print(b)
    a, b = b, a+b

#ex11
#Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
#variable decleration
# a = 0
# #for loop
for a in range(a, 51):
    #if elif else statement
    if(a%3 == 0 and a%5 == 0):
        print("FizzBuzz")
    elif(a%3 == 0):
        print("Fizz")
    elif(a%5 == 0):
        print("Buzz")
    else:
        print(a)

#ex12
#Write a Python program to check the validity of password input by users. Go to the editor
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re
password = input("enter your password")
x = True
while x:
     if (len(password) < 6 or len(password) > 16):
        break
     elif not re.search("[a-z]", password):
        break
     elif not re.search("[0-9]", password):
        break
     elif not re.search("[A-Z]", password):
        break
     elif not re.search("[$#@]", password):
        break
     else:
         print("Valid Password")
         x = False
         break

if x:
    print("Not a Valid Password")

#ex 13
#Write a Python program that accepts a string and calculate the number of digits and letters.
String = input ("enter string and number")
total_number = 0
total_letter = 0
for i in String:
    if i.isnumeric():
        total_number += 1
    else:
        total_letter += 1
print("total number entered are ", total_number)
print("total letters entered are ", total_letter)













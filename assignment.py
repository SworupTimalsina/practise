# Print "1" if a is equal to b, print "2" if a is greater than b,otherwise print "3"
a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
if a == b:print("1")
elif a > b:print("2")
else:print("3")
# Print "Hello" if a is equal to b, or if c is equal to d
a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
c = int(input("Please enter another number: "))
d = int(input("Please enter another number: "))
if a == b or c == d:
    x = "Hello."
print(x)
# Print "Hello" if a is equal to b, and c is equal to d
a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
c = int(input("Please enter another number: "))
d = int(input("Please enter another number: "))
if a == b and c == d:
    x = "Hello."
print(x)
# For given integer x, print ‘True’ if it is positive, print ‘False’ if itis negative and print ‘zero’ if it is 0.
x=float(input("Enter a number:"))
if x >0:
     print("True")
elif x==0:
    print("Zero")
else:
    print("False")
# Check whether the user input number is even or odd and display it to user
a = int(input("Please enter a number: "))
if (a % 2) == 0:
    print("Even.")
else:
    print("Odd.")
# WAP which accepts marks of four subjects and display total marks,percentage and grade.# Hint: more than 70% –> distinction, more than 60% –> first, more than40% –> pass, less than 40% –> fail
a = int(input("Please enter marks: "))
b = int(input("Please enter marks of another subject: "))
c = int(input("Please enter marks of another subject: "))
d = int(input("Please enter marks of another subject: "))
total = a + b + c + d
percent = total / 4
print(f"Total = {total}")
print(f"Percentage = {percent}")
if percent >= 70:
    print("Distinction.")
elif percent >= 60:
    print("First.")
elif percent >= 40:
    print("Pass.")
else:
    print("Fail.")
# What is the output of ‘APPLE’ > ‘apple’?
print("Apple" > "apple") #
#  ANSWER - FALSE (smaller a has greater ASCIIValue)
# Write a Python program to display your details like name, age, addressin three different linesprint
def personal_details():
    name, age="Sworup", 19, 
    address="Shantinagar"
    print(f"Name:{name}\nAge:{age} \nAdress:{address}")
personal_details()
# Write a python program which accepts the radius of circle from user andcompute the area
from math import pi
r=int(input("Enter the radius of a circle:"))
print("Area of the circle is "+str (pi*r**2))
# A school decided to replace the desks in three classrooms. Each desksits two students. Given the number of students in each class,# print the smallest possible number of desks that can be purchased. Theprogram should read three integers: the number of students# in each of the three classes, a, b and c respectively.# Hint - In the first test there are three groups. The first group has 20students and thus needs 10 desks. The second group has 21# students, so they can get by with no fewer than 11 desks. 11 desks arealso enough for the third group of 22 students.# So, we need 32 desks in total.
a = int(input("Enter total number of students in class A: "))
b = int(input("Enter total number of students in class B: "))
c = int(input("Enter total number of students in class C: "))
x = 0
y = 0
z = 0
if (a % 2 == 0):x = a / 2
else:x = (a + 1) / 2
if (b % 2 == 0):y = b / 2
else:y = (b + 1) / 2
if (c % 2 == 0):z = c / 2
else:z = (c + 1) / 2
total = x + y + z
print(f"Total benches = {total}")
# Write a python program which calculates tax of an employee with givencondition:#      Salary                  Tax Rate
#    Below 20000                  15%#    20000 to 50000               25%#    50000 to 100000              30%#    Above 100000                 35%
i = int(input("Enter your income: "))
if i <= 20000:tax = (i) * 0.15
elif i <= 50000:tax = (i - 20000) * 0.25 + 3000
elif i <= 100000:tax = (i - 50000) * 0.30 + 12500
else:tax = (i - 100000) * 0.30 + 30000
print("you owe", tax, "Rupees in tax!")
# Given three integers, print the smallest one. (Three integers should be user input)
a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
c = int(input("Please enter another number: "))
if a < b and a < c:print(f"{a} is the smallest number.")
elif b < a and b < c:print(f"{b} is the smallest number.")
elif c < a and c < b:print(f"{c} is the smallest number.")
else:print("Add different numbers.")
# N students take K apples and distribute them among each other evenly.The remaining (the undivisible) part remains in the basket.# How many apples will each single student get? How many apples willremain in the basket? The program reads the numbers N and K.# It should print the two answers for the questions above.
N = int(input("Number of students: "))
K = int(input("Number of apples: "))
print("Each student will get" , K // N , "apples.")
print("The basket has", K % N, "remaining apples." )
# Check whether 5 is in list of first 5 natural numbers or not. Hint: List=> [1,2,3,4,5]
x = [1, 2, 3, 4, 5]
print (5 in x) # True
# Write a program that asks the user for a number in the range of 1 to 12.The program should display the corresponding month, where# 1=january, 2=february, 3=march, 4=april, 5=may, 6=june, 7=july,8=august, 9=september, 10=october, 11=november, 12=december.# The program should display an error message if the user enters a numberthat is outside the range of 1 to 12.
a = int(input("Enter a number:"))
if a == 1:
    print("January")
elif a == 2:
    print("February")
elif a == 3:
    print("March")
elif a == 4:
    print("April")
elif a == 5:
    print("May")
elif a == 6:
    print("June")
elif a == 7:
        print("July")
elif a == 8:
    print("August")
elif a == 9:
    print("September")
elif a == 10:
    print("October")
elif a == 11:
    print("November")
elif a == 12:
    print("December")
else:
    print("Try Again.")

# Given x = 5, what will be the value of x after we run x+=3?x = 5print(x) # 5x += 3

x = 5
print(x) # 5
x += 3
print(x) # 8 (x = x + 3)

# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
a = int(input("Enter your marks:"))
if a >= 80 and a <= 100:
    print("Grade A")
elif a < 80 and a >= 60:
    print("Grade B")
elif a < 60 and a >= 50:
    print("Grade C")
elif a < 50 and a >= 45:
    print("Grade D")
elif a < 45 and a >= 25:
    print("Grade E")
elif a < 25 and a >= 0:
    print("Grade F")
else:
    print("Try again.")

# Take input of age of 3 people by user and determine oldest and youngest among them
a = int(input("Enter a age:"))
b = int(input("Enter another age:"))
c = int(input("Enter another age:"))
if a > b and a > c:
    print(f"{a} is the oldest.")
elif b > a and b > c:   
    print(f"{b} is the oldest.")
elif c > a and c > b:
    print(f"{c} is the oldest.")
else:
    print("Add different ages.")
if a < b and a < c:
    print(f"{a} is the youngest.")
elif b < a and b < c:
    print(f"{b} is the youngest.")
elif c < a and c < b:
    print(f"{c} is the youngest.")
else:
    print("Add different ages.")
# Write a program to check whether aperson is eligible for voting or not.(accept age from user)
age = int(input("Enter your age: "))
if age > 18 :
    print(f"You can vote because you are {age}.")
else:
    print("You can't vote.")

# Write a program to check whether a number is divisible by 7 or not
a = int(input("Enter a number: "))
if a % 7 == 0:
    print("The number is divisible by 7.")
else:
    print("The number is not divisible by 7.")

# Accept any city from the user and display monument of that city
# City Monument
# Delhi Red Fort
# Agra Taj Mahal
# Jaipur Jal Mahal
city = str(input("Enter a city:"))
if city == "Dehli":
    print("Monument: Red Fort")
elif city == "Agra":
    print("Monument: Taj Mahal")
elif city == "Jaipur":
    print("Monument: Jal Mahal")
else:
    print("Sorry, we don't have data about that city.")

# Write a program to whether a number (accepted from user) is divisible by 2 and 3 both
a = int(input("Enter a number:"))
if a % 2 == 0 and a % 3 == 0:
    print("It is divisible by 2 and 3.")
else:
    print("It is not divisible by 2 and 3.")
# Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# Like:
# Enter First Number: 7
# Enter Second Number : 9
# Enter operator : +
# Your Answer is : 16
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
operator = input("Enter a mathematical operator:")
if operator == "+":
    print("Your answer is: ", a+b)
elif operator == "-":
    print("Your answer is: ", a-b)
elif operator == "*":
    print("Your answer is: ", a*b)
elif operator == "/":
    print("Your answer is: ", a/b)
else:
    print("Try again.")

#Write the syntax of simple if statement.
# is test
# expression statement (s)


#Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".
number=int(input("Enter a number"))
if number%5 ==0:
    print("Hello")
else:
    print ("Bye")

#Write a program to accept a number from 1 to 7 and display the name of the day like 1 for sunday, 2 for monday and so on.
n=int(input("Enter a number from 1 to 7"))
if n==1:
    print ("Sunbday")
elif n==2:
    print("Monday")
elif n==3:
    print ("Tuesday")
elif n==4:
    print ("Wenesday")
elif n==5:
    print ("Thursday")
elif n==6:
    print ("Friday")   
elif n==7:
    print ("Saturday")
else:
    print("Enter a number from 1 to 7")

#Write the logical expression for the following:A is greater than B and C is greater than D
#A>B C>D

#Write a program to check whether a number entered is three digit number or not.
a=int(input("Enter a number:"))
if a>=100 and a<=1000:
    print("Three Digit")
else:
    print("Not Three digit")



#Write a program to check whether a person is senior citizen or not.
age=int(input("enter age"))
if age>=60:
    print("Senior citizen")
else:
    print("Not a senior citizen")

#Write a program to find the lowest number out of two numbers expected from user.
a=int(input("Enter a number"))
b=int(input("Enter another number"))
if a >b:
    print (f"{a} is the smaller number")
else:
    print (f"{b}is the smallest number")

#Out of "elif" and "else if",  which is the correct statement in python?
#elif is the correct statement

#Accept the following from the user and calculate the percentage of class attended:
#a. Total number of working days
#b. Total number of days for absent
#After calculating percentage show that, if the percentage is less than 75, than student will not be able to sit in exam.
workingdays=int(input("Total number of working days"))
absentdays=int(input("Total number of absent days"))
presentpercentage=(100-(absentdays/workingdays)*100)
print(presentpercentage)
if presentpercentage<75:
    print("You will be abl;e to give exam")
else:
    print("You can give exam")

#Accept the age, sex('M', 'F'), number of days and display the wages accordingly.
#Age		Sex	Wage/day
#>=18 and <30	M	700
#		F	750
#>=30 and <=40	M	800
#		F	850
a=int(input("Enter age"))
g=int(input("Enter gender(m/f)"))
n=int(input("Enter number of days"))
if a>=18 and a<30 and g=="m":
    print("total wage is",n*700)
elif a>=18 and g=="f":
    print("Total wage is",n*750)
elif a>=30 and a<=40 and g=="m":
    print("Total wage is",n*800)
else:
    print("Total wage is",n*800) 

#Accept the number of days from the user and calculaye the charge for library according to following:
# Till five days: Rs 2/day
#Six to ten days: Rs 3/day
#11 to 15 days: Rs 4/day
#After 15 days: Rs 5/day
day =int(input("Enter number of day"))
if day<=5:
    print("Rs 2 per day")
elif day>=6 and day<=10:
    print("Rs 3 day")
elif day>=10 and day<=15:
    print("rs 4 per day")
elif day>15:
    print("rs 5 per day")


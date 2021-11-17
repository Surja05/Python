# print ("Hello World")
# var1 = 25
# var2 = 50
# var3 ="STRING"
# print("The total of the 2 numbers :", var1 + var2)

# num1 = input("Enter 1st number\n")
# num2 = input("Enter 2nd number\n")
# print("The sum of the 2 numbers is", int(num1) + int(num2))
# print("The subtraction of the 2 numbers is", int(num1) - int(num2))
# print("The product of the 2 numbers is", int(num1) * int(num2))
# print("The division of the 2 numbers is", int(num1) / int(num2))

# str ="string Slicing And Other Functions In Python"
# print(str[-40:-5:3])
# print(len(str))
# print(str.upper())
# print(str.capitalize())
# print(str[::-1]) # To reverse the string
# print(str.endswith('n'))
# print(str.count('o'))
# print(str.find('P'))
# print(str.replace('s','S'))
# print(str.split(','))

# list1 = [9.5, 5, 12, 98, 54, 15]
# list1.sort()
# list1.append(25)
# list1.remove(9.5)
# list1.insert(3,150)
# list1.pop(2)
# list1.reverse()
# print(list1)

# tuple1 = (5,20,48,99,65,73,99,99,99)
# print(max(tuple1))
# print(tuple1.count(99))

# dict1 = {2:8,3:27,4:64,5:125}
# print(dict1.keys())
# print(dict1.values())
# dict1["six"]="216"
# dict1["six"]="666"
# print(dict1)
# print(dict1.items())

# set1 = {5,6,8,9,1,3,4,0}
# set2 = {25,36,64,81,2,16,9,0,2,5,4,9,6}
# set1.add(25)
# set1.update([50,60,70])
# set1.remove(0)
# set1.pop()
# print(set1.union(set2))
# print(set1.intersection(set2))

# list1 = [[2,4],[3,9],[4,16],[5,25]]
# for numbers,squares in list1:
#     print(numbers, "and the resp square values is", squares) 

# tuple1 = ([2,4],[3,9],[4,16],[5,25])
# for numbers,squares in tuple1:
#     print(numbers, "and the resp square values is", squares) 

# dict1 = {2:4, 3:9, 4:16, 5:25}
# for numbers,squares in dict1.items():
#     print(numbers, "and the resp square values is", squares) 

# i=0
# while(True):
#     if i+1<5:
#         i=i+1
#         continue
#     print(i+1, end=" ")
#     if (i==44):
#         break
#     i=i+1
    
# def func1(a,b):
#     print("The sum of 2 numbers is",int(a)+int(b))
#     # return 0
# a= input("Enter the 1st Number\n")
# b= input("Enter the 2nd Number\n")
# # print(func1(a,b)) # Returns a None as the function returns nothing
# func1(a,b)

# num1 = input("Enter the number\n")
# num2 = input("Enter the number\n")

# try:
#     print("The sume of 2 numbers is", int(num1)+int(num2))

# except Exception as e:
#     print("This is an invalid input")

# x=89
# def abc():
#     x=20
#     def cde():
#         global x
#         x=88
#     print("before calling function 2", x) #since cde() is a property of the abc(), hence the value of x does not change
#     cde()
#     print("after calling function 2", x)
# abc()
# print("the new value", x)

# Factorial (Iterative Method)
# def fact(n):
#     factorial = 1
#     for i in range(n):
#         factorial = factorial*(i+1)
#     return factorial
# number = int(input("Enter a number for factorial\n"))
# print(fact(number))

# Factorial (Recursive Method)
# def fact(n):
#     if n == 0 or n ==1:
#         return 1
#     else:
#         return n*fact(n-1)
# number = int(input("Enter a number for factorial\n"))
# print(fact(number))

# Fibonacci Series: 0 1 1 2 3 5 8 (Sum of the previous 2 numbers)
# def fibo(n):
#     if n == 1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# number = int(input("Enter the number for the series\n"))
# print(fibo(number))

# class Employee:
#     print("This is Employee 1")
#     no_of_leaves = 12

#     def details(self):
#         print(f"The Employee works in {self.company}\nAge is{self.age} and the Salary is{self.salary} ")
    

# me= Employee()

# me.company = "ABCD"
# me.age = 25
# me.salary = "50k"
# me.no_of_leaves = 15

# print(me.details())



# class Employee:
#     print("This is an Employee")
#     no_of_leaves = 12 #((Class Variable))

#     def __init__(self, company, age):

#         self.company = company
#         self.age = age
        

#     def printDetails(self):
#         print(f"The company name is{self.company} and the age of the Employee is{self.age}")
# # To change the Class Variable with an instance, we can use @class method:
#     @classmethod
#     def changeleaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

# me = Employee("ABD Solutions", 50)
# me.printDetails()
# me.changeleaves(15)
# print(Employee.no_of_leaves)

# class Employee:
#     print("This is Employee 1")
#     no_of_leaves = 12

#     #Construtor is Important
#     def __init__(self, name, salary, target):
#         self.name = name
#         self.salary = salary
#         self.targets = target
    
#     def printdetails(self):
#         print(f"Employee 1 is {self.name} and the salary is{self.salary} with annual targets of {self.targets}")

#     @classmethod
#     def leaves(cls, leaves):
#         cls.no_of_leaves = leaves

#     @staticmethod
#     def printme(string):
#         print(f"Like Follow and Subcribe {string}")

# class Sales:
#     def __init__(self, revenue, area):
#         self.revenue = revenue
#         self.area = area
    
#     def report(self):
#         print(f"The revenue from {self.area} is {self.revenue}")

# class Presenter(Sales, Employee):
#     pass
    
# surja = Presenter(36000, "Mumbai")
# surja.report()


# class Student:
#     print("Welcome to the Student's Profile")
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = email
    
#     def printinfo(self):
#         print(f"The full name of the the Student is {self.fname} {self.lname}\n ")
    
# # Suppose I do not want to use a method and instead want to use a property so we use @property 

#     @property
#     def email(self):
#         print(f"{self.fname}.{self.lname}@sch.com")

# # Also, when we want to set a value based on a given attribute and wants to get that automatically, we use @setter 
    
#     @email.setter
#     def email(self, string):
#        mailids = string.split("@")[0]
#        self.fname = mailids.split(".")[0]
#        self.lname = mailids.split(".")[1]
        
# info = Student("Surja", "Goswami")

# info.fname = "sammy"
# info.email = "Samm.123@mail.com"
# print(info.email)


#:::::PRACTICE PROBLEMS:::::

#Take age/year of birth as input and guess when they will turn 100 years old.(Do not use any datetime modules). They can tell a year and the program should tell them their age at that specific year. (All errors to be handled)

actualyear_age = int(input("Enter your Year of Birth or Your Age\n"))

if len(str(actualyear_age)) == 4:
    if actualyear_age>2021:
        print("You are not yet born")

    elif actualyear_age<1900:
        print("You are the Oldest of us all")
    
    else:    
        year_age = actualyear_age + 100
        print(f"You will be of Age 100 at {year_age}")

elif len(str(actualyear_age)) <4:

    if actualyear_age<0:
        print("You are not yet born")

    elif actualyear_age>121:
        print("You are the Oldest of us all")

    else:
         year_age = (2021 - actualyear_age) + 100
         print(f"You will be of Age 100 at {year_age}")
         
  


choice = int(input("Want to know your age at a specific year?"))
actualyear_age = 2021-actualyear_age
print(f"Your age at {choice} would be {choice - actualyear_age}")

        





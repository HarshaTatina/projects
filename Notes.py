# what is python
# python is a popular object oriented programing language with simple syntax and easy learning curve
# why is it popular 
# 1. Simple syntax
#2. Huge community
#3. Used in AI/ML
#4. Web dev
#5.Automation
#INSTALLATIION : chorme>type>python download>first link >64bit python >go with follow>open cmd > type > python --version > version 
# print statement : print("hello world")
#comment : with (#) we comment anyline the line will be in code but not get in output
# name = "harsha" → here name is a variable and harsha is a value to that variable 
# DATA_TYPE 
# string : the characters that are written in b/t "" marks that is a string 
# ex: Name = "sai" → sai is a string 
# name = "Sai"
# print(name)
# Number : the digital letter like (1,2,3,4)
# value = 23
# print(value)
# Float : decimal numbers like 1.5 
# Boolean : the values are only two (True or False) the start letter should be capital 
# Boolean = True
# print(Boolean)
# BOolean = False
# print(BOolean)
# INTERPETER_LANGUAGE : (it check line to line if any error that line will stop) 
# (remaning will run upto the error )(line next of error will not excute it stops at the error) 
# Type : it is used for to check the datatype 
# ex : print(type(2))/
#string operator
# Name = "sai"
# print("My Name is ",Name) → concatition 
# print(f"My nmae is {Name}") → formatted string
# print(Name.upper()) → to change small letters to captial letters
#print(Name.lower()) → to change captial letters to small letters
# print(len(Name)) → to find the length of the string
#print(Name[2:]) → it is called slicing where it done through index values (:) means remianing all
# print(Name[2]) → it is called index here index will start from 0 
#ex : harsha is a name index is h-0 , a-1 , r-2 , s-3 , h-4 , a-5
#integer operator
# (+,-,*,/) 
# print(2+2)
# print(2-3)
# print(2*3)
# print(2/2)
# (==) → comparision operator it gives true or false values only
# ex : print(2==3) → false
# Control Statements 
# if(condition):  → here condition is true means excute or move to elif block
#   print("ok")   → the spaces are very important 
# elif(condition): → same true means excute and false means moves to else
#   print("ok")
# else:            → it is deafult value if above all are wrong it will excute 
#   print("default")
# a_marks = 891
# b_marks = 921
# if(a_marks >= b_marks):
#     print(f"a is toper marks are {a_marks}")
# elif(b_marks >= a_marks):
#     print(f"b is topper marks are {b_marks}")    
# else:
#     print("Both get good marks")
# INPUT : it is used to take values by user or our own value without predefinded
# input("Any statement or according to the use ") → it will take only string to convert it we need to change it into int so for that → (int(input("")))
# OBJECT : no of data type written in [] object is written in []
# if we want to get a element from object separtly by only index 
# ex : obj = ["wqa",1,true,2.2] → here i want 2.2 element so i will give 3
# print(obj[3])
# obj = ["sai","nam",1,1.2,True,False]
# print(len(obj))  
# LOOPS : repeated work done in a single line  
# for loop
# for i in range(0,10):
#     print(i)
#     if(i==3):
#         print("i")
#         continue
# continue : it is used for to skip a fixed position and remaining will same 
# break : it stops at a fixed point and remaning will not print
# while loop 
# countdown = 0 → initalization
# while(countdown<10): → condition
#     print("count ", countdown)
#     countdown+=1 → increment/decrment
# the above code will give 0 to 9 
# if we want 9 to 0 
# countdown = 10 → initalization
# while(countdown>0): → condition
#     print("count ", countdown)
#     countdown-=1 → increment/decrment
# FUNCTION : reusable code means once write again and again used
# syntax : def any_variable(): → function define
#               print("A") it is a block of code or recallable code
#          any_variable() → function call,we can call n-no times
# FUNCTION WITH PARAMETER
# def variable(a,b):
    # return a+b
# print(variable(10,20)) → we can give new new value when we call
# num = int(input())
# for i in range(1,num+1):
#     spaces = " "*(num-i)
#     star = "*"*i
#     print(spaces+star)
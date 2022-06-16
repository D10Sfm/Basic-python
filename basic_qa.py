# 1. Write a Python program to print the following string in a specific format (see the output)
# print("Twinkle, twinkle, little star,\n\t\t\t How I wonder what you are!\n\t\t\t\t\t\t Up above the world so high,\n\t\t\t\t\t\tLike a diamond in the sky.\n Twinkle, twinkle, little star,\n\t\t\t How I wonder what you are")
#
#  2. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
#
# a = input("Enter Firstname: ")
# b = input("Enter Lastname: ")
# print("Hi "+b+" "+a)
#
#
#
# 3 Write a Python program to print the documents (syntax, description etc.) of Python built-in function
# print(range.__doc__,reversed.__doc__,ascii.__doc__,sep="\n")
#
# 4 Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
# num = int(input("Enter num:"))
# i = 17
# if num > i:
#     print(abs(num-i)*2)
#
# 5 Write a Python program to count the number 4 in a given list
# x = input("Enter numbers: ")
# sum = 0
# for i in x:
#     if i == '4':
#         sum +=1
#         continue
# print("The number 4 appear ",sum,"times in the list")
#
# 6 Write a Python program to test whether a passed letter is a vowel or not
# x = input("Enter a letter: ")
# if x in ['a', 'e', 'i', 'o', 'u']:
#     print(x,"Is an vowel letter!")
# else:
#     print(x,"Is not an vowel letter!")
#
# 7 Write a Python program that will accept the base and height of a triangle and compute the area
# par = float(input("Enter triangle height: ")),float(input("Enter triangle base: "))
# print("The triangle area is(Cms):",0.5*par[1]*par[0])
#
# 8 Write a Python program to get the least common multiple (LCM) of two positive integers
# x = int(input("Enter num: ")),int(input("Enter num: "))
# a = x[0]//2
# b = x[1]//2
# if a > b:
#     print(a)
# elif b > a:
#     print(b)
#
# # 9 Write a python program to get the path and name of the file that is currently executing
# import os
# from os import *
# print(getcwd())
#
# 10 Write a Python program to print to stderr
# import sys
# sys.stderr.write("This an error message!")
#
# 11 Write a Python program to convert all units of time into seconds
# days = int(input("Enter days: "))*3600*24
# hours = int(input("Enter hours: "))*3600
# minute = int(input("Enter minute: "))*60
# seconds = int(input("Enter second: "))
# time = days+hours+minute+seconds
# print("The time in seconds is ",time)
#
# 12 Write a Python program to get an absolute file path
# import sys
# print(sys.path[0])
#
# 13 Write a Python program to find the available built-in modules
# import sys
# import textwrap
# module_name = ', '.join(sorted(sys.builtin_module_names))
# print(textwrap.fill(module_name, width=100))
#
# 14 Write a Python program to remove the first item from a specified list
# ls = [1,2,"fasil",5]
# ls.pop(0)
# print(ls)
#
# 15 Write a Python program to filter the positive numbers from a list
# x = [1,2,-4,-3,5,-9,5,-7,5,-15,1,0]
# for i in x:
#      if i < 0:
#         x.pop(x.index(i))
# print(x)
#
# 16 Write a Python program to input a number, if it is not a number generates an error message
# import sys
# x = input("Entr num: ")
# if x.isdigit() == False:
#     print(sys.stderr.write("The input is not a num!"))
# else:
#     pass
#
# 17 Write a Python program to check whether an integer fits in 64 bits
# try:
#  x = int(input("Enter num: "))
#  if x.bit_length() == 64:
#       print(x," is capture 64 bit in the memory!")
#  else:
#       pass
#
# except ValueError as err:
#     print(err)
#
# 18 Write a Python program to check whether lowercase letters exist in a string
# str = input("Enter str: ")
# for i in str:
#     if i.islower() == True:
#         print(str, " have an lowercase letter!")
#         break
#
# 19 Write a Python program to calculate the time runs (difference between start and current time) of a program
# import time
# start = time.time()
# s = [1,2,3,50,5,51,60,22,99,98,50,12]
# f = []
# for i in s:
#     if i % 2 == 0:
#         f.append(i)
#         s.pop(s.index(i))
# print(s,f)
# end = time.time()
# print(end-start)
#
# 20 Write a Python program to extract single key-value pair of a dictionary in variables
# x ={
#     "name":"Messi"
# }
# (d1,d2), = x.items()
# print(d1,d2)


# 21 Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user
# x = int(input("Enter num: ")),int(input("Enter num: "))
# if x[0] % x[1] == 0:
#     print(x[0],"is divided by ",x[1],"\nThe result is: ",float(x[0]/x[1]))
# else:
#     pass
#
# 22 Write a Python function to find the maximum and minimum numbers from a sequence of numbers
# ls = [10,25,30,54,60,28,90,11102,54,63,200]
# print(max(ls))
# print(min(ls))
#
# 23 Write a Python program to add two positive integers without using the '+' operator
# from math import *
# x = 1
# y = x.__add__(1)
# print(y)
#
# 24 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
# 1
# n = int(input("Enter num:"))
# x = [n,str(n)*2,str(n)*3]
# print(x[0]+int(x[1])+int(x[2]))
#
# 2
# s = input("Enter num: ")
# n1 = int("%s" % s[0])
# n2 = int("%s" % s[1])
# print(n1+n2)



# Exam
# 1
# x = int(input("Enter a num: "))
# print(x**2)
#
# 2
# x = int(input("Enter your age: "))
# print(x+20)
#
# 3
# x = int(input("Enter the price: "))
# print(x*1.17)
#
# 4
# nums = int(input("Enter num: ")),int(input("Enter num: "))
# print("sum: ",nums[0]+nums[1],"\nDistance: ",abs(nums[0]-nums[1]),"\nMulti: ",nums[0]*nums[1],"\nDivisio: ",nums[0]/nums[1])
#
# 5
# from datetime import *
# print("Welcom\n",datetime.now())
#
# 6
# x = int(input("Enter num: ")),int(input("Enter num: ")),int(input("Enter num: ")),int(input("Enter num: "))
# print((x[0]+x[1]+x[2]+x[3])/len(x))
#
# 7
# x = int(input("Enter num of nails: "))
# print("Number of nails boxes: ",x//40,"\nNails Excess: ",x%40)
#
# 8
# par = int(input("Enter Distance(Kms): ")),int(input("Enter Speed(Kmh): "))
# minutes = par[0]/par[1]*60
# hours = par[0]/par[1]
# print("Time in hours: ",round(hours,2),"\nTime in minute: ",round(minutes,2))

# 10
# x = input("Enter a phone number without the first digit: ")
# print("The number is:","0"+x)
# """This is an class ehouram"""
#
# # QA1
# print("good day :-)")
#
# QA2
# print("Fasil Masfin\nTech-Career Qa Class")
#
# QA3
# print("^^^^Fasil Masfin\nTech-Career Qa Class")
#
# QA4
# TypeError- print("abcd"+3)
#
# QA5
# print(5**2)
# print(10**3)
# print(25**2)
#
# QA6
# print((25+25+10)//6)
#
# QA7
# print("(25+25)//5 =",(25+25)//5)
#
# QA8
# num = int(input("Enter int num: "))
# print(int(num+1),"the follow num",int(num-1),"the backward num",int(num**2),"the pow by 2")
#
# QA9
# n3 = 11
# print(n3/3)
# print(n3/3.0)
#
# # QA10
# hour = 25
# y = 5
# print(hour/y)
# print(hour%y)
# print(float(hour)/float(y),"this a float dividing", (float(hour)+float(y))/2,"This is the average")
#
# QA11
# hour = input("Enter double digit num:")
# print(int(hour[0])+int(hour[1]))
#
# hour = input("Enter double digit num:")
# print(int(hour)%10+int(hour)//10)
#
#
# QA12
# money_balance = int(input("Enter Starting Money balance:"))
# Money_spanding = int(input("Enter amount of money that spanding:"))
# print(money_balance-Money_spanding)
#
# QA13
# hour = int(input("Enter 2 digit num:"))
# print(str(hour%10)+str(hour//10))
#
# QA14
# hour = input("Enter 3 digit number:")
# y = str(int(hour[1]))
# print(int(hour[0])+int(hour[1])+int(hour[2]))
# print(str(int(hour)%10)+y+str(int(hour)//100))
#
# a = input("Israeli Citizen?y/n: ")
# if a == "n":
#      print("Unauthorised")
# elif a not in ["y","n"]:
#     print("Wrong Character ")
# else:
#     a == "y"
#     b = int(input("Enter Age: "))
#     if b >= 18:
#         print("Entitled to Discount")
#     elif b < 18:
#         print("Underage")
#
#
#
# ConditionPractice
#
# QA1
# a = int(input("Enter 1 num: "))
# b = int(input("Enter 2 num: "))
# print("The Largest num",mahour(a,b))
#
# QA2
# a = int(input("Enter Num1: "))
# b = int(input("Enter Num2: "))
# result1 = a%2
# result2 = b%2
# if result1 == 0 and result2 == 0:
#     print("evan numbers")
# else:
#     print("one or more of the num not evan")
# if a%b == 0 or b%a == 0:
#     print("Divided number each others")
# else:
#     print("Num not divded")
#
#
# The longest way QA3
# user_name1 = input("Enter UserName: ")
# address1 = input("Enter Address: ")
# institution_name1 = input("Enter Institution_name: ")
# age = int(input("Enter Age: "))
# user_name2 = input("Enter UserName: ")
# address2 = input("Enter Address: ")
# institution_name2 = input("Enter Institution_name: ")
# age2 = int(input("Enter Age: "))
# user_name3 = input("Enter UserName: ")
# address3 = input("Enter Address: ")
# institution_name3 = input("Enter Institution_name: ")
# age3 = int(input("Enter Age: "))
# if age < age2 and age < age3:
#     print(user_name1,address1,institution_name1,age)
# elif age2 < age3 and age2 < age:
#     print(user_name2, address2, institution_name2, age2)
# elif age3 < age2 and age3 < age:
#     print(user_name3, address3, institution_name3, age3)
#
# The shortest way(indeehour[]) QA3
# user_name1 = input("Enter UserName: "),input("Enter Address: "),input("Enter Institution_name: "),int(input("Enter Age: "))
# user_name2 = input("Enter UserName: "),input("Enter Address: "),input("Enter Institution_name: "),int(input("Enter Age: "))
# user_name3 = input("Enter UserName: "),input("Enter Address: "),input("Enter Institution_name: "),int(input("Enter Age: "))
# if user_name1[3] < user_name2[3] and user_name1[3] < user_name3[3]:
#     print(user_name1)
# elif user_name2[3] < user_name1[3] and user_name2 < user_name3[3]:
#     print(user_name2)
# elif user_name3[3] < user_name1[3] and user_name3[3] < user_name2[3]:
#     print(user_name3)
#
# QA4
# class_name = input("Enter a name: "),input("Enter a name: "),input("Enter a name: ")
# class_amount = int(input("Enter amount: ")),int(input("Enter amount: ")),int(input("Enter amount: "))
# if class_amount[0] > class_amount[1] and class_amount[0] > class_amount[2]:
#     print(class_name[0]+"your are The Biggest Classrom!")
# elif class_amount[1] > class_amount[0] and class_amount[1] > class_amount[2]:
#     print(class_name[1]+"your are The Biggest Classrom!")
# elif class_amount[2] > class_amount[0] and class_amount[2] > class_amount[1]:
#     print(class_name[2]+"your are The Biggest Classrom!")
#
# QA5
# st_grade = int(input("st1 grade: ")),int(input("st2 grade: ")),int(input("st3 grade: ")),int(input("st4 grade: "))
# avg = (st_grade[0]+st_grade[1]+st_grade[2]+st_grade[3])//len(st_grade)
# print(min(st_grade),mahour(st_grade),(st_grade[0]+st_grade[1]+st_grade[2]+st_grade[3])//len(st_grade))
# print(min(st_grade))
# print(mahour(st_grade))
# print(avg)
# print((st_grade[0]+st_grade[1]+st_grade[2]+st_grade[3])//len(st_grade))
#
#
# QA6
# age = int(input("Enter age: "))
# high_limit = 180
# age_floor1 = 20
# age_floor2 = 30
# age_ceil1 = 40
# age_ceil2 = 50
# if age < age_floor1 or age > age_ceil1:
#     print("Your not in the age range")
# else:
#   hight = int(input("Enter your hight: "))
#   if age >= age_floor1 and age <= age_ceil1 or age >= age_floor2 and age_ceil2 and hight >= high_limit:
#     print("You are qualify to continue")
#   else:
#     print("Your are not qualify")
#
#
# QA7/8
# limit = 7
# age = int(input("Enter age: "))
# if age > 7:
#     print("Go Left")
# else:
#     print("Go Right")
#
#
# QA9
# from random import *
# a = randint(0,50),randint(20,75),randint(35,80)
# numbers_of_guess = 0
# limit = 3
# while numbers_of_guess < limit:
#     print(a)
#     choice = int(input("Enter the highest: "))
#     if mahour(a) == choice:
#         print("Bravo")
#         numbers_of_guess += 1
#     elif mahour(a) != choice and choice in a:
#         print("Wrong Mate")
#         numbers_of_guess += 1
#     elif choice !=  a:
#         print("Num dosen't ehourist")
#         numbers_of_guess += 1
#
# print("You our out of guesses!")
#
# QA10
# a = int(input("Enter One Digit: "))
# if len(str(a)) > 1:
#     print("Not one digit num")
# elif len(str(a)) <= 1 and abs(a) == True:
#     if a%2 == 0 or a%3 == 0:
#      print("Divided by 2 or 3")
#     else:
#       print("Not divided by 2 or 3")
#
# QA11
# age = int(input("Enter yor age: "))
# if 0 < age > 100:
#     print("Unordionary Age")
# else:
#     print("Ordionary age")
#
# QA12
# nums = int(input("Enter Num: ")),int(input("Enter Num: "))
# num1 = nums[0]
# if nums[0] > 0 and nums[0]%2 == 0 and nums[1]%2 == 0 and nums[1] > 0:
#     if nums[0]-1 == nums[1] or nums[0]+1 == nums[1]:
#         print("Followed numbers")
#     else:
#         print("Not Followed numbers")
# else:
#     print("invalid nums")
#
# QA 13
# angle = int(input("Enert an angle: "))
# a = range(90)
# st = 90
# ka = range(91,180)
# if angle in a:
#     print("זווית לא חדה")
# elif angle == st:
#     print("זווית חדה")
# elif angle in ka:
#     print("זווית קהה")
#
# QA 14
# details = input("Enter name: "),int(input("Enter ehourprianc: ")),int(input("Enter age: "))
# ehourp_limit = 3
# age_range = range(25,41)
# if details[1] >= 3 and details[2] in age_range:
#     print("התקבלתה!")
# else:
#     print("מצטערים "+details[0]+" אבל אינך עונה לתנאי המכרז.")
#
# nums = int(input("Enter num1: ")),int(input("Enter num2: ")),int(input("Enter num3: "))
# if nums[0] in range(nums[1],nums[2]+1):
#     print("you in the boundery")
#
#
# grade = 0
# limit = 0
# while grade < 100 and limit < 5:
#     grade = int(input("Enter your grade: "))
#     if grade < 100:
#         print("אתה צריך לעשות מבחן חוזר!")
#         limit += 1
#
# if grade == 100:
#  print("את/ה אלוף !!")
# else:
#     print("נגמרו המועדי ב'!")
#
# num = int(input("Enter Number: "))
# print(pow(num,2))
#
#
# QA1
# a = 0
# while a <= 20:
#     if a%2 != 0:
#         print(a)
#     a += 1
#
#
# for i in range(0,21):
#     if i%2 != 0:
#         print(i)
#
#
# nums= int(input("Enter Start: ")),int(input("Enter End:"))
# for i in range(nums[0],nums[1]+1):
#     if i%2 != 0:
#         print(i)
#
#
# try:
#  nums= int(input("Enter Start: ")),int(input("Enter End:"))
#  range = range(nums[0],nums[1]+1)
#  indehour = range[0]
#  while indehour < nums[1] :
#     if indehour%2 != 0:
#         print(indehour)
#     indehour+=1
#
# ehourcept IndehourError as err:
#     print(err)
#
# num =0
# for i in range(0,10):
#     num = num + i
# print(num)
# -----------------------------------------------------------------------------------------#
#
# even = 0
# divine_4 = 0
# for i in range(0,51):
#     if i % 2 == 0:
#         even += 1
#     if i % 4 == 0:
#         divine_4 += 1
# print(even,divine_4)
#
#
# num1 = 1
# num2 = 1
# for i in range(43):
#     num3 = num1 + num2
#     num1 = num2
#     num2 = num3
# print(num3)
#
# 1
# hour = int(input("Enter num:"))
# if hour > 50:
#     print(hour,"Is bigger than 50")
# else:
#     print(hour,"Is smallest than 50")
#
# 2
# hour = int(input("Enter num: ")),int(input("Enter num: ")),int(input("Enter num: "))
# print("The mahour num is ",mahour(hour),"\nThe min num is:",min(hour))
#
# 3
# hour = int(input("Enter num: "))
# if hour % 2 == 0:
#     print(hour,"Is even num!")
#
# 4
# hour = int(input("Enter num: "))
# if hour < 40:
#     if hour % 2 == 0:
#         print(hour)
#
#
# 5
# hour = int(input("Enter num: "))
# if hour > 100:
#     hour *= 5
# elif hour == 100:
#     hour += 10
# else:
#     hour *= 10
# print(hour)
#
# 6
# hour = int(input("Enter num: "))
# if hour % 2 != 0:
#     pass
# else:
#     if hour > 30:
#         print(hour,"Is even num that greater than 30!")
#     else:
#         print(hour,"Is even number but not greater than 30!")
#
# 7
# hour = int(input("Enter age: ")),int(input("Enter height: ")),input("Enter name: ")
# if hour[0] >= 18 and hour[1] == 156 and hour[2][0] in ['a','b']:
#     print("Congratulation you can apply to the job!")
# else:
#     print("We sorry you not stand in the parameters of the job")
#
# hour = int(input("Enter age: ")),float(input("Enter height: ")),input("Enter name: ")
# if hour[0] > 18:
#     if hour[1] == 1.56:
#         if hour[2][0] in ['a','b']:
#             print("Congratulation you can apply to the job!")
#         else:
#             print("The name "+hour[2],"is invalid!")
#     else:
#         print(hour[1],"Is not match to the valid height!")
# else:
#     print(hour[0],"Is invalid age!")
#
#
# count = 0
# sum = 52
# while count <= 52:
#     print(sum)
#     count += 1
#     sum -= 1
#
#
#
# sum = 100
# while sum <= 250:
#     if sum % 2 != 0:
#         print(sum)
#     sum += 1
#
#
# flag = False
# even = 0
# bigger_than_50 = 0
# divided_6 = 0
# while flag == False:
#     num = int(input("Enter num: "))
#     if num == 7:
#         print("Correct!")
#         flag = True
#     if num % 2 == 0:
#         even += 1
#     if num > 50:
#         bigger_than_50 += 1
#     if num % 6 == 0:
#         divided_6 += 1
#     else:
#         print("Wrong!")
# y = 0
# r = 0
# f = 0
# s =  0
# hour = int(input("Enter num: ")),int(input("Enter num: ")),int(input("Enter num: ")),int(input("Enter num: ")),int(input("Enter num: ")),int(input("Enter num: "))
# y = (mahour(hour))
# r = (min(hour))
# for i in hour:
#     if i > 5:
#         f +=1
#     if i % 2 == 0:
#         s += 1
#
# print("The mahour num:",y,"\nThe min num:",r,"\nThe amount of numbers that bigger than 5:",f,"\nThe even numbers:",s)
#
# hour = []
# for i in range(0,101):
#     hour.append(i)
#
# print(hour)
#
# hour = []
# for i in range(10):
#     n = input("Enter name: ")
#     hour.append(n)
# for i in hour:
#     print(i)
#
# hour = ["Messi","Neymar","Ronaldiniho","houravi","Pep","Pique","Guli","Henry","Jeffren","Puyol"]
# y = []
# for i in hour:
#   if "M"  in i or "m" in i:
#       y.append(i)
#
# print(y)
#
# QA
# from Parking import parkinprice
# parkinprice(10,2022)
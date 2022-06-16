# While Loops exercise

# 1
# a = 0
# while a <= 20:
#     if a%2 != 0:
#         print(a)
#     a += 1
'''-----------------'''
# 2
# try:
#  nums= int(input("Enter Start: ")),int(input("Enter End:"))
#  range = range(nums[0],nums[1]+1)
#  index = range[0]
#  while index < nums[1] :
#     if index%2 != 0:
#         print(index)
#     index+=1
#
# except IndexError as err:
#    print(err)
'''------------------'''
#3
# try:
#  nums= int(input("Enter Start: ")),int(input("Enter End:"))
#  choose = int(input("Enter num 1-Even numbers 2-Not even numbers: "))
#  range = range(nums[0],nums[1]+1)
#  index = range[0]
#  valid = 1,2
#  while index < nums[1] and choose in valid:
#     if index%2 != 0 and choose == 2:
#         print(index)
#     elif index%2 == 0 and choose == 1:
#         print(index)
#     index+=1
#  if choose not in valid:
#     print("Invalid Choose")
# except IndexError as err:
#     if err:
#         print(err)
#
# except ValueError as err2:
#     if err2:
#         print(err2)

'''--------------------------'''
# 16
# sum = 0
# flag = True
# num_round = 0
# while flag == True:
#     num = input("Enter num: ")
#     num_round +=1
#     if num == "q":
#         flag = False
#     else:
#         sum += int(num)
#
# print(sum//(num_round-1),)


# 16
# try:
#   sum = 0
#   flag = True
#   num_round = 0
#   list = []
#   while flag == True:
#      num = input("Enter num: ")
#      num_round +=1
#      if num == "done":
#         flag = False
#      else:
#         list.append(num)
#         sum += int(num)
# except ValueError as err:
#     print(err)
#
# print(sum//(num_round-1),min(list),max(list))






# Side Exercise
# from random import *
# Winner_num = randint(0,100)
# Winner_num_test = 5
# num_guesses = 0
# limit = 4
# win = False
# while num_guesses < limit and win is not True:
#     choice = int(input("Enter num: "))
#     if choice != Winner_num_test and choice < Winner_num :
#         print("Go Higher")
#         num_guesses += 1
#     elif choice != Winner_num_test and choice > Winner_num :
#         print("Go Lower")
#         num_guesses += 1
#     else:
#         win = True
#
# if win == True:
#   print("You Win")
#   print(Winner_num)
# else:
#   print("You out of guesses")

# avg = 0
# amount = 0
# total = 0
# price = input("Please enter a price:for exit enter 'exit")
# while price != 'stop':
#     total = total +int(price)
#     amount += 1
#     avg = total / amount
#     price = input("Please enter a price:for exit enter 'exit")
#
# print(total,avg)


# num = int(input("Enter num: "))
# while num>0:
#     if num%3 == 0:
#         print(num)
#     num -=1


# a = "I love python"
# times = 4
# i = 0
# while i < times:
#     print(a)
#     i += 1

# guess = int(input("Guess num: "))
# num = 10
# if guess in range(0, num):
#     print("Found!")
# else:
#     pass

# num = 20
# while num > 0:
#     if num%2 == 0:
#         print(num)
#     num -=1


# a = 0
# sum = 0
# p = False
# while a < 32:
#      sum += a
#      a +=1
#      if sum >= 20 and p == False:
#          p = True
#          print(a)
#
# print(sum)

# from random import *
# Winner_num = randint(0,100)
# Winner_num_test = 5
# num_guesses = 0
# limit = 4
# win = False
# while num_guesses < limit and win is not True:
#     choice = int(input("Enter num: "))
#     if choice != Winner_num_test:
#         print("Wrong")
#         num_guesses += 1
#     else:
#         win = True
#
# if win:
#   print("You Win")
# else:
#   print("You out of guesses")

# avg = 0
# amount = 0
# total = 0
# price = input("Please enter a price:for exit enter 'exit")
# while price != 'stop':
#     total = total +int(price)
#     amount += 1
#     avg = total / amount
#     price = input("Please enter a price:for exit enter 'exit")
#
# print(total,avg)


# num = int(input("Enter num: "))
# while num>0:
#     if num%3 == 0:
#         print(num)
#     num -=1


# a = "I love python"
# times = 4
# i = 0
# while i < times:
#     print(a)
#     i += 1

# guess = int(input("Guess num: "))
# num = 10
# if guess in range(0, num):
#     print("Found!")
# else:
#     pass

# num = 20
# while num > 0:
#     if num%2 == 0:
#         print(num)
#     num -=1


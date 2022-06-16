 #1
# nums= int(input("Enter Start: ")),int(input("Enter End:"))
# for i in range(nums[0],nums[1]+1):
#     if i%2 != 0:
#         print(i)
'''-----------------------'''
#2

# num =0
# for i in range(0,10):
#     num = num + i
# print(num)
# '''------------------------'''
#

#4
# try:
#  nums= int(input("Enter Start: ")),int(input("Enter End: "))
#  choose = int(input("1-Even 2-Not Even: "))
#  if choose != 2 and choose != 1:
#      print("Invalid")
#  else:
#      for i in range(nums[0],nums[1]+1):
#       if choose == 1 and i%2==0:
#         print(i)
#       elif choose == 2 and i%2!=0:
#         print(i)
#
# except IndexError as err:
#     print(err)
# except ValueError as err2:
#     print(err2)

# 6
# x = 0
# for i in range(1,14):
#     for j in range(i+1,14):
#         x = x+j+i
#         break
# print(x)

# 7
# for i in range(1,11):
#     print(i * 1,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10,sep="\t",end="\n")

# 8
# x = input("Enter 5 digit num:")
# y = input("Enter 5 digit num:")
# for (i,j) in zip(x,y):
#     if i == j:
#      print(i)

# 9
# x = input("Enter nums: ")
# y = input("Enter num: ")
# for i in x:
#     if i == y:
#         print(i," in nums!")
#     else:
#         continue
# print(y+" is not in nums!")


# 10
# sum = 0
# nums = int(input("Enter num: ")),int(input("Enter num: ")),int(input("Enter num: ")),int(input("Enter num: ")),int(input("Enter num: "))
# for (i,j) in zip(nums,nums):
#     sum = sum +i+j-nums[0]
#
# print(sum//len(nums))

# 11
# index = 0
# m = []
# for i in range(2,100):
#     flag = False
#     for j in range(2, i):
#         if i % j == 0:
#             flag = True
#             break
#
#     if flag != 1:
#        m.insert(index, i)
#        index += 1
# print(m)

# 12
# for i in range(1,11):
#     print(i * 1,i*2,i*3,i*4,i*5,i*6,i*7,i*8,i*9,i*10,sep="\t")

# 13
# for i in range(100,5000,4):
#     print(i)

# 14
# for i in range(5,2501):
#     if i%6 != 0:
#         continue
#     else:
#         print(i)

# 15

# a = input("Enter str: ")
# b = []
# index = 0
# for i in a:
#     b.insert(index,i)
#     index += 1
#
# print(b)

# a = input("Enter str: ")
# index = 0
# for i in a:
#     print(i)

# for i in range(11):
#  print(i)

# numbers = int(input("Enter num1: ")),int(input("Enter num2: "))
# for i in range(numbers[0],numbers[1]+1):
#     print(i)

# multi = 1
# for i in range(1,100):
#     multi *= i
#
# print(multi)
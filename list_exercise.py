# x = []
# for i in range(1,11):
#     x.append(i)
# print(x)
# 2.1
# x = [i for i in range(1,11)]
# print(x)
#3
# x = []
# for i in range(5):
#     n = int(input("Enter nume: "))
#     x.append(n)
# print(sorted(x,reverse=False))


#4
# ls = []
# ls_divided_11 = []
# even_nums = []
# bigger_10 = 0
# lower_10 = 0
# divided_3 = 0


# for i in range(11):
#     n = int(input("Please Enter num: "))
#     ls.append(n)
# for i in ls:
#     x = i/11
#     ls_divided_11.append(round(x,2))
#     if i > 10:
#         bigger_10 += 1
#     if i < 10:
#         lower_10 += 1
#     if i % 2 == 0:
#         even_nums.append(i)
#     if i % 3 == 0:
#         divided_3 += 1
# print("The sum of the list:",sum(ls),"\nThe result of divine by 11:",ls_divided_11,"\nThe number that biggert than 10:",bigger_10,"\nThe number that lower than 10:",lower_10,"\nThe max num:",max(ls),"\nThe even nums:",even_nums,"\nThe amount of nums that divided with 3:",divided_3)


#5
# ls = []
# for i in range(11):
#     n = int(input("Enter num: "))
#     ls.append(n)
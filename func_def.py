'''definition of an function'''

from time import *



# def caculater():
#  n = int(input("select an action,1-adding 2-minus 3-dividing 4-multi: "))
#  if n == 1:
#     par = int(input("Enter nums: ")),int(input("Enter nums: "))
#     beauty_print(adding(par[0],par[1]))
#  elif n == 2:
#     par = int(input("Enter nums: ")),int(input("Enter nums: "))
#     beauty_print(minus(par[0],par[1]))
#  elif n == 3:
#     par = int(input("Enter nums: ")),int(input("Enter nums: "))
#     beauty_print(divding(par[0],par[1]))
#  elif n == 4:
#     par = int(input("Enter nums: ")),int(input("Enter nums: "))
#     beauty_print(multi(par[0],par[1]))
#
# caculater()

#1
# def adding(x,y):
#     z = x+y
#     return z

#2
# def minus(x,y):
#   z = x-y
#   return z

#3
# def divding(x,y):
#      z = x/y
#      return z

#4
# def multi(x, y):
#     z = x * y
#     return z

#5
# def beauty_print(z):
#     print("^^^^^^^^^^")
#     print("The number is:",z)
#     print("________________________")


"""Exam"""
#QA1
# the func build in

# def even(n):
#     if n % 2 == 0:
#         return 0
#     else:
#         return 1

# def beauty(z):
#     print("*"*5)
#     print(z)
#     print("*"*5)


# limit = 0
# while limit < 3:
#     choose = int(input("Enter num: "))
#     beauty(even(choose))

#QA2
# def avg(s,n):
#     z = s/n
#     beauty(z)
#
# avg(280,4)

#QA3
# def amount(x):
#     z = len(str(x))
#     beauty(z)

# amount(123454616)

#QA4
# def twenty(x):
#     f = x//20
#     return f
#
# def ten(x):
#     z = abs(twenty(x)*20-x)
#     f = z//10
#     return f
#
# def five(x):
#     z = abs((ten(x)*10)+(twenty(x)*20)-x)
#     f = z // 5
#     return f
#
# def change(x):
#     print(twenty(x))
#     print(ten(x))
#     print(five(x))
#
#
# change(115)

#5
# def power(x,y):
#     z = x ** y
#     print(z)
#
# power(2,2)

#6
# def discount(x):
#     z = x * 0.15
#     return x - z
#
# def price(x):
#     if x > 1000:
#         print(discount(x))
#     else:
#         z = x * 0.10
#         print(x-z)
#
# price(1050)
#9
# from math import *
# def a(x,y):
#     ls = []
#     for i in range(1,y+1):
#         if x%i == 0 and y%i == 0:
#           ls.append(i)
#     return max(ls)
# def b(x,y):
#     ls = []
#     for i in range(1,y+1):
#         if x%i == 0 and y%i == 0:
#           ls.append(i)
#     return min(ls)
# def c(x,y):
#     z = x ** y
#     return z
# def d(x,y):
#     result = sqrt(x)-sqrt(y)
#     return round(result,2)
# #
# def choice(x,y):
#     z = input("Choose action \na-max divider \nb-min divider \nc-pow \nd-result sqrt(x)-sqrt(y) \ne-exit: \nyour choise: ")
#     if z == 'a':
#         print(a(x,y))
#     elif z == 'b':
#         print(b(x,y))
#     elif z == 'c':
#         print(c(x,y))
#     elif z == 'd':
#         print(d(x,y))
#     elif z == 'e':
#         return
#     else:
#         print("Invalid choise")
#
#
# choice(3,8)

#11
# def print_outcome(x):
#     print("Give Customer number ",x," Special treatment!")
# def bookshop():
#     customer_no = int(input("Enter customer number: "))
#     goods_value = int(input("Enter the value of the goods purchased in a year: "))
#     bills_pay = int(input("customer pay is bills on time? 1-yes 2-no: "))
#     seniority = int(input("Number of years as customer: "))
#     if bills_pay == 2 or goods_value < 8000:
#         return
#     else:
#         print_outcome(customer_no)
#
# bookshop()

'------------'
# def avg():
#     ls = []
#     s = True
#     while s == True:
#         n = input("Enter num: ")
#         if n == 'q':
#             print(sum(ls)/len(ls))
#             s = False
#         else:
#             ls.append(int(n))
#
# avg()

# def polindrom(st):
#     start = 0
#     end = len(st)-1
#     for i in range(len(st)//2):
#         if st[start] != st[end]:
#             print("Not polindrom!")
#             return
#         else:
#             start +=1
#             end -= 1
#     print("is a Polindom")
#
# polindrom("ablewasiereisawelba")


# def list(t):
#     for i in t:
#         if i < 0 or type(i) == float:
#             print("The list have an negetive or incomplete numbers!")
#             return
#     print("The list is without negetive or incomplete numbers!")
#
# list([1,2,2,3,3.5])

# def hours_cac(x):
#     z = x/60
#     print("The time in hours ",round(z,1))
#
# hours_cac(53)


# def true_false(x,y):
#     if x == y:
#         return True
#     else:
#           return False
#
# true_false("fasil","fasil")


# def new(ls):
#     sum = 0
#     nls = []
#     for (i,s) in zip(ls,ls[1],ls[-1]):
#         if i == s:
#             sum += 1
#         for j in range(len(ls)):
#             nls.append(sum)
#         else:
#             nls.append(i)
#     print(nls)
#
#
# new([1,2,3,4,5,5])



# def a(x,y):
#     ls = []
#     for i in range(1,y+1):
#         if x%i == 0 and y%i == 0:
#           ls.append(i)
#     return max(ls)
#
# def gcd(x, y):
#    gcd = 1
#    if x % y == 0:
#        return y
#    for k in range(int(y / 2), 0, -1):
#        if x % k == 0 and y % k == 0:
#            gcd = k
#            break
#    return gcd
#
# start = process_time()
# gcd(1000,100)
# end = process_time()
# print(end - start)


# def convert(coin):
#     y = float(input("Enter dolar rate: "))
#     return round(coin*y)


# def cardprice(weight:float,flight_class:str):
#  card_price = 1
#  if weight <= 20:
#     if flight_class == "First class" or flight_class == "Business":
#         return card_price - (card_price / 100 * 25)
#     elif flight_class == "Tourist":
#         return card_price - (card_price / 100 * 21.5)
#     else:
#         return card_price - (card_price / 100 * 20)
#
#  elif weight > 20 and weight <= 40:
#     if flight_class == "First class" or flight_class == "Business":
#         return card_price - (card_price / 100 * 30)
#     elif flight_class == "Tourist":
#         return card_price - (card_price / 100 * 26.5)
#     else:
#         return card_price - (card_price / 100 * 25)
#  elif weight > 40 and weight <= 100:
#     if flight_class == "First class" or flight_class == "Business":
#         return card_price - (card_price / 100 * 35)
#     elif flight_class == "Tourist":
#         return card_price - (card_price / 100 * 31.5)
#     else:
#         return card_price - (card_price / 100 * 30)


def parkinprice(hour, model):
    price1 = hour * 20
    price2 = hour * 15
    price3 = hour * 10
    price4 = hour * 5
    car_type = input("Enter your car type-engine/electric: ")
    if abs(hour) == hour or abs(model) == model and len(model) == 4:
        if model == 2022 and car_type == "electric":
            if hour <= 3:
                print("You got 20% discount!")
                print(f"The price is:{20} shekel for an hour\nsum: ", round(price1-(price1/100*10),2), "!")
            elif hour in range(4, 6):
                print("You got 20% discount!")
                print(f"The price is:{15} shekel for an hour\nsum: ", round(price2-(price2/100*10),2), "!")
            elif hour in range(6, 25):
                print("You got 20% discount!")
                print(f"The price is:{10} shekel for an hour\nsum: ", round(price3-(price3/100*10),2), "!")
            elif hour > 24:
                print("You got 20% discount!")
                print(f"The price is:{5} shekel for an hour\nsum: ", round(price4-(price4/100*20),2), "!", )
        elif model == 2022 and car_type == "engine":
            if hour <= 3:
                print("You got 15% discount!")
                print(f"The price is:{20} shekel for an hour\nsum: ", round(price1-(price1/100*15),2), "!")
            elif hour in range(4, 6):
                print("You got 15% discount!")
                print(f"The price is:{15} shekel for an hour\nsum: ", round(price2-(price2/100*15),2), "!")
            elif hour in range(6, 25):
                print("You got 15% discount!")
                print(f"The price is:{10} shekel for an hour\nsum: ", round(price3-(price3/100*15),2), "!")
            elif hour > 24:
                print("You got 15% discount!")
                print(f"The price is:{5} shekel for an hour\nsum: ", round(price4-(price4/100*15),2), "!", )
        elif model < 2022 and car_type in ("engine" or "electric") :
            if hour <= 3:
                print("You got 10% discount!")
                print(f"The price is:{20} shekel for an hour\nsum: ", round(price1-(price1/100*10),2), "!")
            elif hour in range(4, 6):
                print("You got 10% discount!")
                print(f"The price is:{15} shekel for an hour\nsum: ", round(price2-(price2/100*10),2), "!")
            elif hour in range(6, 25):
                print("You got 10% discount!")
                print(f"The price is:{10} shekel for an hour\nsum: ", round(price3-(price3/100*10),2), "!")
            elif hour > 24:
                print("You got 10% discount!")
                print(f"The price is:{5} shekel for an hour\nsum: ", round(price4-(price4/100*10),2), "!", )

    else:
        print("Invalid Hour or model!")
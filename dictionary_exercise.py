# players = [{
# "name":"messi",
# "age":34,
# "pos":"All field"
# },
#     {
#         "name":"xavi",
#         "age":35,
#         "pos":"cm/atm"
#     },
    # {
    #     "name":"iniesta",
    #     "age":35,
    #     "pos":"cm/atm"
    # }]

# for x in players:
#     print(players[x])

# for x in players:
#     if x["name"] in "xavi":
#      print(x["name"])

'''exercise'''
#QA1
# best_player = {
#     "name":"messi",
#     "age":34,
#     "nationality":"argentina",
#     "pos":"all field",
#     "fav drink":"mata",
#     "bff":"suarez",
#     "team":"psg"
# }

# print(best_player.keys())

# print(best_player.values()

# print(best_player["name"])

# for x in best_player.items():
#     print(x)

# players = "messi","xavi","iniesta","ronaldiniho","casillas"
# for i in players:
#     print("The name in index",players.index(i),"is ",i)

# def looplist(x):
#     for i in range(x):
#         return i
#
# print(looplist(5))

# def looplist(x):
#     for i in range(x):
#         yield i
#
# print(looplist(5))
#
#
# def looplist(x):
#     for i in range(x):
#         yield i
#
# print(list(looplist(5)))


# def hello(x="Messi"):
#     print("Hello ",x)
#
# def multi(x=1,y=7):
#     return x*y
#
# def fa(x=8):
#     for i in range(x):
#         yield i
#
# hello()
# print(multi())
# print(list(fa()))
#
#
# def faa(x=8):
#     for i in range(x):
#         print(i)
# faa()
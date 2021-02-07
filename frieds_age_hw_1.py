# число друзей из одноклассников
num_cl_fr = 3
#  имена  одноклассников
cl_fr_1 = "Oxe"
cl_fr_2 = "John"
cl_fr_3 = "Helen"
#  вывод на экран
monolog = f"I have {num_cl_fr} friends. His names arw {cl_fr_1}, {cl_fr_2}  and {cl_fr_3}"
print(monolog)
# откуда приехал Oxe, и сколько ему лет
oxe_city = input("Oxe, where are you from?")
oxe_age = int(input("Oxe, how old  are you ?"))
# while type(oxe_age) != int:
#     print("Это не число! Пробуй еще раз")
#     oxe_age = input("Oxe, how old  are you ")
# else:
#     print(" Good, Oxe!")
#     print(" And now , John!")
print(" Good, Oxe!")
print(" And now , John!")
# откуда приехал John, и сколько ему лет
john_city = input("John, where are you from?")
john_age = int(input("John, how old  are you ?"))
print(" Good, John!")
print(" And now , Helen!")
# откуда приехал Helen, и сколько ему лет
Helen_city = input("Helen, where are you from?")
Helen_age = int(input("Helen, how old  are you ?"))
print(" Good, Helen!")
print(" Well Done!!!")
f_monolog = f"So i have {num_cl_fr}  friends:  John from {john_city} and he is {john_age} years old." \
            f" Helen from {Helen_city} and she is {Helen_age} years old." \
            f" And Oxe from {oxe_city} and she is {oxe_age} years old.  "
# финальный мололог
print(f_monolog)

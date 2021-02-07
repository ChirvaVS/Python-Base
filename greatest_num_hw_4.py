# число для операций
num = int(input("Напиши любое целое число !"))
a = num % 10
a_1 = num % 100
b = a_1 // 10
c = num // 10

if a >= b:
    big = a
else:
    big = b
while c > 10:
    c = c // 10
    b = c % 10
    if b >= big:
     big = b
sign = f"Самая большая цифра в числе: {big}"
print(sign)
# print(a)
# print(b)
# print(c)
# print(big)
# while c > 10:
#
# if a >= b:
#     big = a
# else:
#     big = b
# while b > 10:
#     if a >= b:
#         big = a
#     else:
#         big = b
# print(big)
# print(a)
# print(b)
# print(c)
# print(big)




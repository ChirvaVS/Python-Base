
print("Привет!")
t = int(input("Введи время в секундах!"))
hour = str(t // 360)
hour_2 = hour.zfill(2)
min = str(t // 60)
min_2 = min.zfill(2)
sec = str(t % 60)
sec_2 = sec.zfill(2)
time = f"Время в  общепринятом формате {hour_2}:{min_2}:{sec_2}"
print(time)

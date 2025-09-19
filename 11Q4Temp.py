t = int(input("please tell the temprature :- "))

if t < 0:
    print("Freezing cold")

elif t >= 0 and t <10:
    print("very cold")

elif t >= 10 and t <20:
    print("cold")

elif t >= 20 and t <30:
    print("plesant")

elif t >= 30 and t <40:
    print("hot")

else:
    print("temprature is very hot ")
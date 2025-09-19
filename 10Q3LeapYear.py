year = int(input("tell your year :- "))

if year %100 == 0 and year %400 == 0:
    print("Its a leap year")

elif  year %100 != 0 and year %4 ==0:
    print("Its a leap year")

else:
    print("its a normal year")
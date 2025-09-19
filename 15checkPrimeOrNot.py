n = int(input("check your number is prime or not  :-"))

count = 0

for i in range(1,n+1):
    if n%i == 0:
        count = count + 1

if count == 2:
    print("your number is prime")
else:
    print("your number is not prime")
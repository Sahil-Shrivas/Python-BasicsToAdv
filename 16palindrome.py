a = "NAMAN"

b = ""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]


if b == a:
    print("your string is palindrome")

else:
    print("its not a palindrome")
a = int(input("tell your number :- "))

try:                                    # with try except is always use.
    print(10/a)

except Exception as err:
    print(f"sorry there is an err as {err}")

else:
    print("good there is no exception")

finally:
    print("i will run no matter what")


print("ok i have done the division")



# try :: wrap the code that might cause an exception
# except :: handle the exception if it occurs
# else :: run code only if no exception occurs
# finally :: run code no matter whether there's an exception or not
# raise :: manually throw an exception

def decorate(func):
    def wrapper(*args,**kwargs):
        print("the addition to your numbers are ")
        func(*args,**kwargs)
        print("thankyou I hope you liked it ")
    return wrapper


@decorate
def addition(a,b):
    print(f"your total is {a + b} ")

addition(12,67)

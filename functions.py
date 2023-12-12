def my_func(param1='defauly'):
    print("My First python function")


my_func()


def add_numbers(num1, num2):
    if type(num1) == type(num2):
        return num1 + num2
    else:
        return "Invalid input, Need an integer"


result = add_numbers(2, 3)
print(result)

# Lambda Expression -> basically a any. function
mylist = [1,2,3,4,5,6,7,8]
evens = filter(lambda num: num%2==0, mylist)
print(list(evens))


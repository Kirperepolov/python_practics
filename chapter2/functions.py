# define a basic function
def func1():
    print('I am a function 1')


# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)


# function that returns a value
def func3(x):
    return x * x * x


# functions with default values for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


# function with variable number of arguments
def multi_add(*args):
    result = 0
    for i in args:
        result  = result + i
    return result



# func1()
# print(func1())
# print(func1)  # a function is passed as an object

# func2(10, 20)
# print(func2(10, 20))
#
# print(func3(3))

print(power(2))
print(power(2, 3))
print(power(x=2, num=5))

print(multi_add(1,2,4))
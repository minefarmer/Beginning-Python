# Define/Create a function
def say_hello():
    # Body of function
    print("Hello, world!")


say_hello()  # Hello, world!


def say_hello():
    # Body of function
    return "Hello, world!"


print(say_hello())  # Hello, world!

say_hello()  # Hello, world!


def add_num(x, y):
    # Body of Function
    return x + y


print(add_num(2, 3))  # 5


def say_name(name="Rich Matson"):
    print("My name is", name)


say_name()  # By default, the value will be Rich Matson
say_name("RM")  # It will print RM


def print_num(x, *y):
    print(x)

    for i in y:
        print(i)


print_num(0)
print_num(1, 2, 3, 4, 5, 6, 7)  # [2, 3, 4, 5, 6, 7] is a tuple.  ## 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7


def print_num(x, *y):
    print(x)

    for i in y:
        print(i)


print_num(0)
print_num(1, True, 3.5, "RM")  # [True, 3.5, "RM"] is a tuple.  ## 0
# 1
# True
# 3.5
# RM


# Anonymous functions  ## lambda
# This is a variable that acts like a function. Since it acts like a function I have to invoke it lik a function.
def my_name(name, idn): return print("Name: ", name, "ID:", idn)


my_name("RM", 12345)  # Name:  RM ID: 12345



# add_me = lambda x, y: x + y
# print(add_me())  # Traceback (most recent call last):
#                 # File "/home/rich/Desktop/CarlsHub/Beginning-Python/ClassNotes/FunctionsModules/Functions.py", line 79, in <module>
#                 #     print(add_me())
#                 # TypeError: <lambda>() missing 2 required positional arguments: 'x' and 'y'


add_me = lambda x, y: x + y
print(add_me(3, 5))  # 8

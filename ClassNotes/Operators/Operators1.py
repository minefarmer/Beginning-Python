'''                 OPERATORS
What are they?
    Symbols, such as +, -, /, %, etc.

What do they do?
    They allow you to compute an operation on variables and their values.
    They are one of the most basic and yet essential parts of any programming language.



                    ASSIGNMENT OPERATORS    
This type of operator allows me to set a value to a variable.
    Example:
    a = 3
    b = 4
    c, d = a, b  # This means that  c = a, and d = b.
WARNING:
    Do not confuse it with the 'equal' sign! They are not the same.



                    ARITHMETIC OPERATORS
This type of operator allows you to perform arithmetic operations (or basic math), and then yield a value.
    Example:
    a = 3
    b = 2
    print( a+b )  # Addition
    print( a-b )  # Subtraction
    print( a*b )  # Multiplication
    print( a/b )  # Division
    print( a%b )  # Modulus  ## shows a remainder of one.
    print( a**b )  # Exponentiation  # 3 to the power of 2 is a call  to 9
    print( a//b )  # Floor Division  # rounds to the lower number. i.e. rounds to 1.



                    ASSIGNMENT OPERATORS
Assignment operators can also perform an operation on theleft operand.  # operand =  (variable on the left side of the 'assignment'.)
    Example:
print( a+b )  # Addition
a = 3
b = 2
c = a + b  # 5

print( a-b )  # Subtraction
a = 3
b = 2
c = a - b
print(c)  # 1

print( a*b )  # Multiplication
a = 3
b = 2
c = a * b  # 6



print( a/b )  # Division
a = 3
b = 2
c = a / b  # 1



print(a%b)  # Modulus
a = 3
b = 2
c % a  # 1   ## shows a remainder of one.



# print( a**b )  # Exponentiation  # 3 to the power of 2 is a call  to 9
a = 3
b = 2
c = a ** b  
print(c)  # 9



# c +=
a = 3
b = 2
c = a + b
c += a  # Equivalent of c = c + a
print(c)  # 8



# c -=
a = 3
b = 2
c = a + b  # 5
c -= a  # Equivalent of c = c - a 
print(c)  # 2



c *=
a = 3
b = 2
c = a + b  # 5
c *= a  # Equivalent of c = c * a 
print(c)  # 15



# c /=
a = 3
b = 2
c = a + b  # 5
c /= a  # Equivalent of c /= c / a 
print(c)  # 1.6666666666666667



# c %=
a = 3
b = 2
c = a + b
c %= a  # Equivalent of c = 5 % 3 = the remainder of 2.
print(c)  # 2



# c **=
a = 3
b = 2
c = a + b
c **= a 
print(c)  # 125


# c //=
a = 3
b = 2
c = a + b
c //= a  # Equivalent of c = c // a = using floor division.
print(c)  # 1




                    COMPARISION OPERATORS
This type of operator checks if both elements are similar on both sides of the operator, then returns True or False.
    Example:
        a = 3
        b = 2
        print( a == b)  # Returns False
        print( a != b)  # Returns True
        print( a <= b )  # Returns False
        print( a >= b )  # Returns True




                    LOGICAL OPERATORS
They determin whether two or more expressions are the same.
The 'and' operator.  # The and operator expects both sides to be the same and then it returns True.

The 'or' operator.  # The or operator expects either one of the expressions to be true in order to return True.

The 'not' operator.  #  also (!)
Example:
    x = 2
    y = 3
print( x == 2 and y == 3 ) # Returns True if BOTH statements are true.
print( x == 2 or y == 3 ) # Returns True if EITHER statements are true.
print( not (x == 2 and y == 3 ) ) # Returns True if the OPPOSITE statements are true.




                    MEMBERSHIP OPERATORS.
They allow me to look into the elements in a list or tuple and determine if the list/tuple contains that element.
The "in" operator.
The "not in" operator.
    Example:
list_a = [1, 2.3, "4", True]
var_1, var_2 = 5, 2.3
print(var_1 in list_a)  # False
print(var_2 not in list_a)  # False





                    IDENTITY OPERATORS
 
They compare memory location (identity) of the variables on both sides of the operator.
Python's id() function allows you to determine what the memory location of a variable is.
The 'is' operator determins whether or not two variables are located in the same memory location inside my computer.
The 'is not' operator determins whether or not two variables don't have the same memory location inside my computer.
    Example:
        d,e,f = 15, 20, 30
        print(d is e)  # Returns False
        print(e is not f)  # Returns True

'''

d,e,f = 15, 20, 30
print(d is e)  # Returns False
print(e is not f)  # Returns True

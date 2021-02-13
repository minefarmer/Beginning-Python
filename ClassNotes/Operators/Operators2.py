var1 = 3
var2 = 4

str_1 = "Hello"
str_2 = " Carl"

# Arithmetics operators
print("A:", var1, "B:", var2)  # ('A:', 3, 'B:', 4)
print("A + B:", var1 + var2)  # A + B: 7
print("Str_1 + Str_2:", str_1 + str_2)  # Str_1 + Str_2: Hello Carl

print("A - B:", var1 - var2)  # B: -1
print("A * B:", var1 * var2)  # B: 12
print("A / B:", var1 / var2)  # B: 0.75
print("A % B:", var1 % var2)  # Modulus  # B: 3
print("A ** B:", var1 ** var2)  # Exponent  # B: 81
print("A // B:", var1 // var2)  # Floor Division  # B: 0

# Comparison Operators
print("Is Var1 == Var2? ", var1 == var2)  # False
print("Is Var1 != Var2? ", var1 != var2)  # True
print("Is Var1 <= Var2? ", var1 <= var2)  # True
print("Is Var1 >= Var2? ", var1 >= var2)  # False
print("Is Var1 < Var2? ", var1 < var2)  # True
print("Is Var1 > Var2? ", var1 > var2)  # False

# Assignment Operators
x = 5

x += 2
print(x)  # x += y is the same as  x = x + y  # 7
x -= 2
print(x)  # x ++ y is the same as  x = x - y  # 5
x *= 2
print(x)  # x ++ y is the same as  x = x * y  # 10
x /= 2
print(x)  # x ++ y is the same as  x = x / y  # 5.0
x %= 2
print(x)  # x ++ y is the same as  x = x % y  # 1.0
x **= 2
print(x)  # x ++ y is the same as  x = x ** y  # 1.0
x //= 2
print(x) # x ++ y is the same as  x = x // y  # 0.0

# Logical Operator
print("Is Var1 Equal 3 AND Var2 NOT EQUAL 7?", var1 == 3 and var2 != 7)  # Is Var1 Equal 3 AND Var2 NOT EQUAL 7? True
print("Is Var1 Equal 3 OR Var2 NOT EQUAL 7?", var1 == 3 or var2 == 7)  # Is Var1 Equal 3 OR Var2 NOT EQUAL 7? True
print("Is Var1 NOT EQUAL 3 OR Var2 NOT EQUAL 7?", not(var1 != 3 and var2 == 7))  # Is Var1 NOT EQUAL 3 OR Var2 NOT EQUAL 7? True

# Membership Operator
tuple_a =(1, 3.5, "Hello", False)
search_1 = "RM"
search_2 = False

print("Is 'RM' found in Tuple_a?", search_1 in tuple_a)  # Is 'RM' found in Tuple_a? False
print("Is 'False' found in Tuple_a?", search_2 in tuple_a)  # Is 'False' found in Tuple_a? True
print("Is 'RM' NOT found in Tuple_a?", search_1 not in tuple_a)  # Is 'False' NOT found in Tuple_a? True

# Identity Operator
var3 = 5
var4 = 6
var5 = var3

print("Memory Location (ID) of Var3:", id(var3))  # Memory Location (ID) of Var5: 93963224423872
print("Memory Location (ID) of Var4:", id(var4))  # Memory Location (ID) of Var5: 93963224423872
print("Memory Location (ID) of Var5:", id(var5))  # Memory Location (ID) of Var5: 93963224423872

print("Is Var3 the same as Var4?", var3 is var4)  # Is Var3 the same as Var4? False
print("Is Var4 NOT the same as Var5?", var4 is not var5)  # Is Var4 NOT the same as Var5? True
print("Is Var3 the same as Var5?", var3 is var5)  # Is Var3 the same as Var5? True

'''                 FLOW CONTROL
Simply means to use loops to control the behavior of my code.
Allows code to keep running until condition is fulfilled.

Types of Loops
    While loop
    While-Else loops
    For loops
Useful commands when using loops.
    Break Statement
    Continue Statement

                    While Loops
While loops repeat whatever statements are found within it's body indefintely, until the condition becomes false.
Example:
    x = 0
    while (x < 5):
        print(x)
        count += 1 # count = count + 1
    print('End of loop')
While loops are also best used when you want a code to be looping constantly, like on servers.

                    While-Else Loops
Unlike other programming languages, Python also has an 'else' statement that can accompany a while loop.
Example:
    count = 0
    while count <= 5:
        print(count, 'is less than 5!')
        count += 1
    else:
        print('Count is greater than 5')
    print("Loop has ended")

                    For Loops
For loops, unlike while loops, allow me to loop through a sequence (e.g.:lists, tuples
or range.
Example:
    list_a = [1, 2, 3, 4, 5]
    for var in list_a:
        print(var)
NOTE: Because strings are similar to lists, I can loop through the characters of the string Too!

What the loop is going to do is that is going to go over every single elemens and site list _a and print each variable separately under the name var.
So on the first iteration being the first time it loops

'''

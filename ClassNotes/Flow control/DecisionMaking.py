'''                 Decision Making
Another very important programming language aspect.
    Allows code to execute under very specific conditions.
What are they?
                    IF Statements
Useful if I want my code to execute under a certain condition.
Example:
    my_age = 82
    if my_age <= 18:
        print('Welcome to the club!)
Can also be written on one line.
    if my_age >= 18 : print('Welcome to the Club!')
NOTE: Only do so IF I have only ONE command!  # Otherwise I'll receive an error.


                    IF-ELSE Statement
Useful whenI want one alternative to a condition.
Think of it like: "Do this if condition is met; otherwise do that."
Example:
    my_age = 82
    if my_age <= 18:
        print('Welcome to the club!) 
    else:
        print("You're too young to be part of the club!)
NOTE: Only do so IF I have only ONE command!  # Otherwise I'll receive an error.


                    IF-ELIF statements
Also known as 'else if' in other programming languages.
Allows more than one conditional alternative.
Example:
    my_age = 82
    if my_age >= 21:
        print('You\'re legal')
    elif my_age >= 18:
        print('You\'re mature!')
An 'else' statement is optional.


                    NESTED conditions
Simply means 'conditions within conditions'.
Example:
    my_age = 82
    if my_age >= 18:
        if my_age >= 21:
            print('You\'re awesome!')
        else:
            print('You\'re okay!)
    else:
        print('Sorry, not good enough')


'''
""""

 def - used to define a function 
nothing in the parenthesis in the function definition hello() suggests that this function is not going to take any input 
the collon ':' specifies that all intended statements following the colon are part of the hello() function


def hello():
    print("hello")


#### next step is to parameterize the function hello to take in user input
### assigning default value of world to 'to' variable in case no input is passed by the user
def hello(to="world"):
    print("hello,", to)

hello()
name = input ("What's your name? ")
### name variable is passed to the to variable to be consumed by the hello function
hello(name)

"""
##### ============================== writing your code top to bottom ==============================

### define the main function which calls the hello function

def main():
    name = input ("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

#use or call main to trigger main() function

#scope of variable can be used only where its being defined


main()
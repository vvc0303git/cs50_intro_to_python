#ask user for name
#name = input("What's your name? ")

"""" 
#remove whitespace from str
#strip() - method that allows to manipulate str whic removes all whitespaces
#reads right to left, assigning new value (manipulated value) for name
name = name.strip()

#title() -method that capitilizes first letter of each word in a title or name (i.e. capitalize first latter of first and last name)
name = name.title()
"""

#remove whitespace from str AND capitilizae user's name

#name = name.strip().title()

""""
combine everything into one line of code that will
1. ask for user input
2. remove extra white spaces at the beginning and end of input
3. capitlize first letters of users input

"""
name = input("What's your name? ").strip().title()

#split users name into first name and last name; uses white space between the first and second input to split input into two values

first, last = name.split(" ")
#say hello to user
# str data type that stores string values
# print function by default ends with end = '\n', which cause the next statement to be printed on the next line
#f string - format string - tells pythong to format string in a "special way"

#outputs just the first name from the user's input
print (f"hello, , {first}")

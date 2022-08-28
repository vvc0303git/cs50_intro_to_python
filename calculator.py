""""
x = input ("What's x?")
y = input ("what's y?")


#convert input str value to int value
z=int(x)+int(y)


#nesting functions ; in this case the value from the input functions becomes the nested value for the int function

x = int(input ("What's x? "))
y = int(input ("What's y? "))
print (x + y)

"""

#float - floating point value => decimals
"""addition
x = float(input ("What's x? "))
y = float(input ("What's y? "))
#print (x + y)


#round output to nearest wholse number
z = round (x+y)

#insert comma after every three 000, to clearly display i.e. 1,000 10,000 100,000 ..etc ; improves readability of the ouput with comma separation
print (f"{z:,}")

"""
x = float(input ("What's x? "))
y = float(input ("What's y? "))

#rounds output to include only 2 integers after the decimal point
#z = round (x/y, 2)
z = x / y
#using format function to format output to round to two numbers after the decimal point
print (f"{z:,.2f}")

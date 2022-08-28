def main():
    x = int(input("What's x? "))
    print ("x squared is", square(x))

def square(n):

# user return to return the result; thefore providing a return for the square function , pass the return function to the main function
    ### return n*n
    ### use pow function in python to take in value for n and raise to the power of following the value after the comman
    ### in example bellow take value of n and raise to the power of 3
    return pow (n,3)

main()
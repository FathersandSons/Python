x = "awesome"
def myFunc(): #defining a function
    print("Python is " + x)

myFunc()

# variables that are created outside of a function are called global variables
# global variables can be used both inside and outside of a function

y = "super"
def yes():
    y = "fantastic"
    print("Python is " + y)

yes()
print("Python is " + y)

def no():
    global z
    z = "amazing"

no()
print("Python is " + z)

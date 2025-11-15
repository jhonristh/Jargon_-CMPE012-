"""
#There's a built in functiond
# as well as use defined functions , def __name__ > code
#funnc with parameters, no return
def get_the_product(input1, input2):
    product = input1 * input2
    print(product)

a = 12
b = 13
get_the_product(a, b)

a = 434
b = 23
get_the_product(a, b)

a = 1
b = 78
get_the_product(a, b)

#func with parameters, with return
def get_the_product(input1, input2):
    product = input1 * input2
    print(product)
    return product
a = 12
b = 5
c = 23
d = 39
print(get_the_product(a, b) * get_the_product(c, d))
"""

import time
#function with no parameters and no return
def print_countdown():
    print("Counting down")
    for i in range (10, 0 , -1):
        time.sleep(1)
        print(i)

print_countdown()

##review
#def - keyword
#nameoffunction -
#() - with or without parameters
#:
#(parameter1,parameter2) - parameters
#body or code block - where u write commands
#return
#funnc with parameters, no return
#func with parameters, with return
#function with no parameters and no return

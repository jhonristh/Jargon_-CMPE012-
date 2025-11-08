"""
print("before loop")

for i in range (10):
    if i % 2 == 0:
        print("Even number: " + str(i))
        continue
    elif i > 6:
        print(str(i) + " is greater than 6")
        break
    print("i value now is: " + str(i))

print("after loop")

break Statement
break ends the loop immediately, regardless of where you are in the iteration.

Useful when a certain condition is met and you no longer need to continue looping.
continue Statement
continue skips the current iteration and moves directly to the next one.

Useful when you want to skip some values or conditions but continue looping for others.
"""

#timed interation with continue and break
import time

isConnected = "No"
for retry in range (4):
    time.sleep(2)
    isConnected = input("Is connected?")
    if isConnected == "Yes":
        print("Connection established")
        break
    else:
        print("Request timed out")

print("Now Processing")

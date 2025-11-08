"""
#now with dICt
myInfo = {
    "Citizenship": "Filipino",
    "Age": 78,
    "Registered": True,
}

if myInfo["Citizenship"] == "Filipino" and myInfo["Age"] >= 18:
    if myInfo["Registered"]:
        print("You can vote, explanation: a Filo, Legal of age, registered")
    else :
        print("You are not registered, can't vote awww")
elif myInfo["Citizenship"] == "Filipino" and myInfo["Age"] < 18:
    print("You cannot vote. Please wait until you are eligible and then register.")
else:
    print("You can not vote nor register ")
#more suffering

"""


Citizenship = "Filipino"
Age = 11
Registered = True

if Citizenship == "Filipino" and Age >= 18:
    if Registered:
        print("You can vote")
    else :
        print("You are not registered, can't vote awww")

elif Citizenship == "Filipino" and Age < 18:
    print("You cannot vote. Please wait until you are eligible and then register.")
else:
    print("you can not vote nor register ")



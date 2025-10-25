#list of a nested dict
ATMMachineDataBase = [
    { "Name": {
        "LastName": "Bond",
        "FirstName": "James", }
        ,
    "AccountNo": 133437,
    "PIN" :3647  ,
    "ControlNo" : 551 ,
    "Balance" : 1433.90
    } ,
{ "Name": {
        "LastName": "Cardo",
        "FirstName": "Dalisay", }
        ,
    "AccountNo": 14547,
    "PIN" :1234  ,
    "ControlNo" : 896,
    "Balance" : 1434.00
    } ,
{ "Name": {
        "LastName": "Jeans",
        "FirstName": "Billy", }
        ,
    "AccountNo": 167897,
    "PIN" :3244  ,
    "ControlNo" : 534,
"Balance" : 1334.67
    } ,
    ]
myName = input("Enter your name: ")
PIN = input("Enter your PIN: ")
print(f'Good Day! [{myName}]', "your balance is ", f'[{Balance}]' )
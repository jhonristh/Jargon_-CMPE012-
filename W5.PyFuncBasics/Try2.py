from operator import index

strFullName = "Jhon Rey Oquendo"

strModified = strFullName.capitalize()
print(strModified)

strModified = strFullName.count("o")
print(strModified)

strModified = strFullName.upper()
print(strModified)

strModified = strFullName.split(" ")
print(strModified)

strModified = strFullName.swapcase()
print(strModified)

strModified = strFullName.replace("Jhon Rey","Jose Mari")
print(strModified)

strModified = strFullName.replace(" ","...")
print(strModified)
print(" ")
print(" ")
print(" ")

#join
strFirst = "Juan"
strMid = "Desales"
strLast = "Oquendo"
strFullName = "_".join([strFirst, strMid, strLast])
print("Good morning,", strFullName)

#join
strFirst = "Juan"
strMid = "Desales"
strLast = "Oquendo"
strFullName = "_".join([strFirst, strMid, strLast])
print(strFullName)

#boolean if numeric
newValue = strFullName.isnumeric()
print(newValue)

#making subscript
newValue = strFullName[3:10]
print(newValue) #substring
newValue = strFullName[3:10:4]
print(newValue) #substring with jump ,3rd value will be the interval for it's jump
#return low low low low low
print(strFullName.index("e"))
print(strFullName.index("e",3,9))


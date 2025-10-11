strInput = "93585843959J7668687h9899on98 897 R879798e808y"
newString = (" ")
for char in strInput:
    if not char.isnumeric():
        newString = newString + char

print(newString)
#TASK  : fix overload input error, receiver decoding
charList = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', " ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
    "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"',
    ",", "<", ".", ">", "/", "?", "\\", "|", "`", "~"
]

myPIN = "BDyu9058~"
output = ""
key = 3
indexCounter = 0

for letter in myPIN:
    indexCounter = charList.index(letter)
    print(indexCounter)

CListLen =(len(charList))
print(CListLen)


if indexCounter > CListLen:
    -
    for charList in charList:
        indexCounter = charList.index(charList
    )
    output = output + charList[charLIST + key]
else :
    output = output + charList[indexCounter + key]

print(output)

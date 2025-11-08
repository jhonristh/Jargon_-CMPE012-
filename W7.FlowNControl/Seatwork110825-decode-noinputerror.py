#TASK  : fix overload input error, receiver decoding process
### RUN code
##interactive pin encrypter and decrypter

import time
print("Good day! ")
for delayeffect in range(2):
    time.sleep(0.5)
    print("Now loading...")
print("Encrypt and Decrypt...")
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
for _ in range(3): #3 times trial for pin double check
    myPIN0 = input("Set your PIN: ")
    myPIN = input("Confirm your PIN: ")
    for delayeffect in range(3): #time kuno
        time.sleep(0.5)
        print("initializing")
    if myPIN0 == myPIN: #if same, dat same char as stated
        print("PIN is correct!")
        break
    else: #false then tryagain and reloop
        print("PINs do not match. Try again.")
else:
    print("Too many attempts. Request timed out.")
    exit()#tama na please

#for delayeffect in range(1):
    #time.sleep(1)
    #print("initializing")
output = "" #changes overcode
key = 5 #pangpalito
cap = len(charList) #check overall char quantites
#print("Max Char # :", cap)

for delayeffect in range(2):
    time.sleep(1)
    print("initializing")
#iterations with just right and overindexing chars
for letter in myPIN:
    if letter in charList:
        indexCounter = charList.index(letter)
        newIndex = (indexCounter + key) % cap #%modulo len()
        output = output + charList[newIndex]
print("You're encrypted PIN:" , output) #Encypted PIN done


##decoding
DecodeRequest = input("Do you want to decode your PIN? (Y/N): ")
if DecodeRequest.upper() == "Y": #auto caps for human error
    nEwoutput = "" #changes overcode
    for letter in output:
        if letter in charList:
            indexCounter = charList.index(letter)
            origIndex = (indexCounter - key) % cap #reverse in encryption
            nEwoutput += charList[origIndex] #+= all character appended not only the last one
        else:
            nEwoutput += letter
    print("Your decrypted PIN:", nEwoutput)
    print("Thanks, setup completed.")
else:
    print("Thanks, setup completed.")




"""#trial and error
DecodeRequest = input("Do you want to decode your PIN ? (Y/N) : ")
if DecodeRequest == "Y":
    nEwoutput = output - charList[(indexCounter + key) % len(charList)]
    print("You're decrypted PIN token: " , nEwoutput)
else :
    print("thanks, setup completed")
myPIN = "Bu8`"
output = ""
key = 3
#indexCounter = 0
cap = len(charList)
print("Max Char # : " , cap)

for letter in myPIN:
    indexCounter = charList.index(letter)
    #print(indexCounter)
    if indexCounter > cap:
        indexCounter = (indexCounter + key) % len(charList)
        output = output + charList[indexCounter + key]
    else:
        indexCounter = charList.index(letter)
        output = output + charList[indexCounter + key]
print(output)


if indexCounter > cap:
    output = output + charList[(indexCounter + key) % len(charList)]
else:
    output = output + charList[indexCounter + key]

print(output)

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

"""
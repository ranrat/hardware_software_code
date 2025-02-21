
def dectohex(num):
    num = int(num)
    hexdict = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
    if num > 1:
        dectohex(num // 16)
    a = str(num % 16)
    for old, new in hexdict.items():
        a = a.replace(old, new)
    a = str(a)
    print(a, end='')
    
def dectobin(num):
    num = int(num)
    if num > 1:
        dectobin(num // 2)
    print(num % 2, end='')

def dectooct(num): 
    num = int(num)
    if num > 1:
        dectooct(num // 8)
    print(num % 8, end='')

def bintodec(num):
    num = int(num)
    value = 0
    lenstr = len(decimal)
    for x in decimal:
        if x == '1':
            bindigit = pow(2, (lenstr-1))
            value = value + bindigit
            lenstr = lenstr - 1
        elif x == '0':
            lenstr = lenstr - 1
    print(value)

def bintooct(num):
    num = int(num)
    value = 0
    lenstr = len(decimal)
    for x in decimal:
        if x == '1':
            bindigit = pow(2, (lenstr-1))
            value = value + bindigit
            lenstr = lenstr - 1
        elif x == '0':
            lenstr = lenstr - 1
    num = value
    dectooct(num)
    
def bintohex(num):
    num = int(num)
    value = 0
    lenstr = len(decimal)
    for x in decimal:
        if x == '1':
            bindigit = pow(2, (lenstr-1))
            value = value + bindigit
            lenstr = lenstr - 1
        elif x == '0':
            lenstr = lenstr - 1
    num = value
    dectohex(num)

def hextodec(decimal):
    hexdict = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}
    value = 0
    lenstr = len(decimal)
    for x in decimal:
        if "A" or "B" or "C" or "D" or "E" or "F" in x:
            for old, new in hexdict.items():
                x = x.replace(old, new)
            newnum = int(x)
            hexdigit = (newnum * (pow(16, (lenstr-1))))
            value = value + hexdigit
            lenstr = lenstr - 1
        else:
            newnum = int(x)
            hexdigit = (newnum * (pow(16, (lenstr-1))))
            value = value + hexdigit
            lenstr = lenstr - 1
    print(value)

def hextooct(decimal):
    hexdict = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}
    value = 0
    lenstr = len(decimal)
    for x in decimal:
        if "A" or "B" or "C" or "D" or "E" or "F" in x:
            for old, new in hexdict.items():
                x = x.replace(old, new)
            newnum = int(x)
            hexdigit = (newnum * (pow(16, (lenstr-1))))
            value = value + hexdigit
            lenstr = lenstr - 1
        else:
            newnum = int(x)
            hexdigit = (newnum * (pow(16, (lenstr-1))))
            value = value + hexdigit
            lenstr = lenstr - 1
    num = value
    dectooct(num)

def hextobin(decimal):
    hexdict = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}
    value = 0
    lenstr = len(decimal)
    for x in decimal:
        if "A" or "B" or "C" or "D" or "E" or "F" in x:
            for old, new in hexdict.items():
                x = x.replace(old, new)
            newnum = int(x)
            hexdigit = (newnum * (pow(16, (lenstr-1))))
            value = value + hexdigit
            lenstr = lenstr - 1
        else:
            newnum = int(x)
            hexdigit = (newnum * (pow(16, (lenstr-1))))
            value = value + hexdigit
            lenstr = lenstr - 1
    num = value
    dectobin(num)

def octtodec(num):
    num = int(num)
    value = 0
    lenstr = len(decimal)
    for x in decimal:
        if x == '8':
            print("That aint it chief")
            value = ''
            break
        elif x == '9':
            print("that aint it chief")
            value = ''
            break
        else:
            newnum = int(x)
            octdigit = (newnum * (pow(8, lenstr-1)))
            value = value + octdigit    
            lenstr = lenstr - 1         
    print(value)

def octtobin(num):
    num = int(num)
    value = 0
    lenstr = len(decimal)
    for x in decimal:
        if x == '8':
            print("That aint it chief")
            value = ''
            break    
        elif x == '9':
            print("that aint it chief")
            value = ''
            break
        else:
            newnum = int(x)
            octdigit = (newnum * (pow(8, lenstr-1)))
            value = value + octdigit    
            lenstr = lenstr - 1 
    num = value
    if num == '':
        return None
    else:
        dectobin(num)    

def octtohex(num):
    num = int(num)
    value = 0
    lenstr = len(decimal)
    for x in decimal:
        if x == '8':
            print("That aint it chief")
            value = ''
            break    
        elif x == '9':
            print("that aint it chief")
            value = ''
            break
        else:
            newnum = int(x)
            octdigit = (newnum * (pow(8, lenstr-1)))
            value = value + octdigit    
            lenstr = lenstr - 1 
    num = value
    if num == '':
        return None
    else:
        dectohex(num)   

def ending():
    newanswer = input('''
    Would you like to keep converting?''').lower().strip()
    if newanswer == "yes":
        print("Ok then.")
        main()
    elif newanswer == "no":
        print("Thanks for converting with me!")
    else:
        print("Sorry, didn't catch that.")
        ending()


print("This program converts numbers from one base system to another.")
decimal = input("Enter your number: ").strip()
num = decimal

def main():
    print("Specify how you want to convert your numbers. For example, enter in decimal to binary, or hexadecimal to octal.")
    answer = input("Enter your desired conversion: ").lower().strip()
    if answer == "decimal to binary":
        
        dectobin(num)
    elif answer == "decimal to hexadecimal":
        
        dectohex(num)
    elif answer == "decimal to octal":
        
        dectooct(num)
    elif answer == "binary to decimal":
        
        bintodec(num)
    elif answer == "binary to hexadecimal":
        
        bintohex(num)
    elif answer == "binary to octal":
        
        bintooct(num)
    elif answer == "hexadecimal to decimal":
        
        hextodec(decimal)
    elif answer == "hexadecimal to binary":
        
        hextobin(decimal)
    elif answer == "hexadecimal to octal":
        
        hextooct(decimal)
    elif answer == "octal to decimal":
        
        octtodec(num)
    elif answer == "octal to binary":
        
        octtobin(num)
    elif answer == "octal to hexadecimal":
        
        octtohex(num)
    else:
        print("Sorry, didn't catch that. Try again.")
        main()
    ending()











if __name__ == "__main__":
    main()
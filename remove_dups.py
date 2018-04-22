__author__='abhishek'
def removeDuplicated(mystring):
    if mystring == None:
        return
    
    chars = set()
    newPos = 0
    for c in mystring:
        if c not in chars:
            chars.add(c)
            mystring[newPos] = c
            newPos += 1

    print(mystring[:newPos])

if __name__ == "__main__":
    myString = bytearray("geeks for geeks", "ascii")
removeDuplicated(myString)
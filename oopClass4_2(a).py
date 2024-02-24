def isPale(string):
    ln = len(string)
    for i in range(0,int(ln/2)):
        if(string[i]!=string[ln-i-1]):
            return False
    return True
string = input()
if(isPale(string)):
    print("Palindrome")
else:
    print("Not Palindrome")

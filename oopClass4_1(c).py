def primeCheck(num):
    for i in range(2, num):
        if(i*i>num):
            break
        if(num%i==0):
            return False
    return True

num = int(input())
if(primeCheck(num)):
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")

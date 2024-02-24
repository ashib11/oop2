def rec(num):
    if(num <=0):
        return 0
    return num + rec(num-1)
num = int(input())
print(rec(num))



x,y = [int(x) for x in input().split()]
num = int(input())

if(num >= x and num <=y):
    print("within range")
else:
    print("out of range")

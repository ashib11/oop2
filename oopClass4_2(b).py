def calFacto(num):
    ans = num; 
    while(num > 1):
        num-=1
        ans*=num
    return ans

num = int(input())
print(calFacto(num))

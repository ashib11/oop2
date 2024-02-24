def printEven(lst):
    for el in lst:
        if int(el) % 2 == 0:
            print(el , end = ' ')


x = input()
num_list = x.split()
printEven(num_list)





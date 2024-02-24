def unique(input_list):
    un_set = set(input_list)
    un_list = list(un_set)
    return un_list
input_list = input().split()
res_list = unique(input_list)
print(res_list)

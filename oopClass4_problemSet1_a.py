def count_uppper_lower(string):
    upper_cnt=0
    lower_cnt=0
    for char in string:
        if char.isupper():
            upper_cnt+=1
        elif char.islower():
            lower_cnt+=1
    return upper_cnt, lower_cnt

input_string = input()
upper, lower = count_uppper_lower(input_string)

print("No. of Uppercase characters: ", upper)
print("No. of Lower case Characters: ", lower)



def c_to_f(temp):
    return(int)( float(5/9)*(temp-32))
def f_to_c(tep):
    return (int)(float(9*tep/5)+32)
tmp = float(input())
print(f"{tmp}*C is {f_to_c(tmp)} in Fahrenheit\n")
tep = float(input())
print(f"{tep}*F is {c_to_f(tep)} in Celsius\n")

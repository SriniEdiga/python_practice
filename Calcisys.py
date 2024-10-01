import sys

def add(num1,num2):
    sum = num1 + num2
    return sum

def sub(num1,num2):
    s = num1 - num2
    return s

def mul(num1,num2):
    m = num1 * num2
    return m


num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

if operator == "add":
    output = add(num1, num2)
    print(output)
elif operator == "sub":
    output = sub(num1, num2)
    print(output)
else:
    output = mul(num1, num2)
    print(output)


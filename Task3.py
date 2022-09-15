def make_operation (sign, *args):
    result = 0
    if sign == "*":
        result = 1
    for num in args:
        if sign == "+":
            result = result + num
        if sign == "*":
            result = result * num
        if sign == "-":
            result = result - num

    return result

calculation = make_operation('*', 88, 7, 4, 12)

print(calculation)


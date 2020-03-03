
def print_negot_power(number, power):
    num = 1/number
    if power == 0:
        print(1)
    elif power == -1:
        print(num)
    else:
        while power <= -2:
            num *= num
            power += 1
        print(num)

print_negot_power(2, -2)
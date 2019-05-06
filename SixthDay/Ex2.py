def digital_root(n):
    rem = 0
    while int(n / 10) != 0:
        rem = rem + n % 10
        n = int(n/10)
        if(int(n/10) == 0):
            n = rem + n % 10
            rem = 0

    return n


data = int(input('Enter your number'))
print(digital_root(data))

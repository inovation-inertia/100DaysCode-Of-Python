# Add Function
def Add(x, y):
    return x+y


print('1. Add')
print('2. Substract')
print('3. Multiply')
print('4. Divide')
a = int(input('Enter your choice'))
firstnum = int(input('Enter first number'))
secondnum = int(input('Enter second number'))
temp = Add(firstnum, secondnum)  # calling function
print(temp)

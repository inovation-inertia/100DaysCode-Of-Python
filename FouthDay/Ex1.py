class Person:
    def __init__(self, userinput1, userinput2):
        self.data1 = userinput1
        self.data2 = userinput2

    def add(self):
        c = str(self.data1 + self.data2)
        print("Result of Add -:  " + c)

    def substract(self):
        if self.data1 > self.data2:
            c = str(self.data1 - self.data2)
        else:
            c = str(self.data2 - self.data1)
        print("Result of Substract -:  " + c)

    def multiply(self):
        c = str(self.data1 * self.data2)
        print("Result of Multiply -:  " + c)

    def divide(self):
        if self.data2 != 0:
            c = str(self.data1 / self.data2)
        else:
            c = "Infinte Value"
        print("Result of Divide -:  " + c)


print('1. Add')
print('2. Substract')
print('3. Multiply')
print('4. Divide')
a = int(input('Enter your choice'))
firstnum = int(input('Enter first number'))
secondnum = int(input('Enter second number'))
p1 = Person(firstnum, secondnum)
if a == 1:
    p1.add()

elif a == 2:
    p1.substract()

elif a == 3:
    p1.multiply()

elif a == 4:
    p1.divide()

else:
    print('Sorry ! you enter a wong input')

class hiddenVar:

    __hidden = 8

    def add(self, arg):
        self.__hidden += arg
        print(self.__hidden)


obj1 = hiddenVar()
obj1.add(22)
obj1.add(22)
print(obj1.__hidden)

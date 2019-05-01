# 1.For Loop Basic work
even_list = list(range(2, 10, 2))
for i in range(3):
    print(i)

# 2. Printing a Patteren
# *
# * *
# * * *
# * * * *
# * * * * * [ Like That ]

for i in range(1, 5):
    for j in range(i):
        print('*', end=" ")
    print("")
# Here i learned one thing Identation is really matter @ time of code
# Other Langauge having a proper paranthesis then code is proper maintain but in python complete code being a part Identation otherwise it will produced a wrong result
i = 0
while i < 5:
    print(i)
    i += 1

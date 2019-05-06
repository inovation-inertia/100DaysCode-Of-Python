# Write a Solution For this Problem -:
# def countBits(n):
#     a_bin = bin(n)
#     count = 0
#     for i in a_bin:
#         if(i == '1'):
#             count = count+1
#     print(count)


# call Function From there -:
# countBits(36)


# Write a Optimum Code Base
def countBits(n):
    return bin(n).count("1")


print(countBits(36))

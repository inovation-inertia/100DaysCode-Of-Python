a = int(input('Enter a First Number'))
b = int(input('Enter a Scond Number'))
try:
    c = a/b
    print("Result -:", c)
except:
    print("Error is occurred")


#################################################
# User Define exception -:
class UserException(RuntimeError):
    def __init__(self, arg):
        self.value = arg


try:
    # Here to genearte an Exception
    raise UserException("Error")

# Here to handle a exception
except UserException as e:
    print(e.value)

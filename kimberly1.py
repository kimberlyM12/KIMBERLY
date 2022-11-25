try:
    print(x)
except NameError:
    print("La variable no se ha declarado")
except:
    print("Algo anda mal")

x = - 1

if x < 0:
    raise Exception("perdon,el numero es menor a 0")

x = "hello"

if not type(x)is int:
 raise TypeError("Only integers are allowed")

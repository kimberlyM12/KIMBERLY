class menu:
    def __init__(self):
        self.nombre = input('Registra tu nombre')
        self.apellido = input('Registra tus apellidos')
        self.edad = int(input('Registra tu grado')
        self.seccion = input('Registra tu seccion')
        self.ID = int(input('Registra tu ID'))
        self.direccion = input('Registra tu direccion')
        self.telefono = input('Registra tu telefono')
    def nombre (self):
        print(f'Nombres: ', self.nombres)
    def apellidos(self):
        print(f'apellidos: ', self.apellidos)
    def edad(self):
        print(f'edad: ', self.edad)
    def grado(self):
        print(f'grado: ', self.grado)
    def seccion(self):
        print(f'seccion: ', self.seccion)
    def ID(self):
        print(f'ID: ', self.ID)
    def direccion(self):
        print(f'direccion: ', self.direccion)
    def telefono(self):
        print(f'telefono: ', self,telefono)
x = menu()
Y = 0
while y < 5:
    print('Bienvenido al menu')
    print(' ')
    print('1. datos personales')
    print('2. datos escolares')
    print('3. datos de contacto')
    print('4.salir')
    print(' ')
    print('-------')
    op = input('que deseas registrar? ')
    

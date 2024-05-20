lista_clientes = []
lista_empleados = []

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Clientes(Persona):
    def __init__(self, nombre, apellido, telefono, identificador, saldo = 0):
        super().__init__(nombre, apellido)
        self.telefono = telefono
        self.identificador = identificador
        self.saldo = saldo
    
    def crear_cliente(self):
        lista_clientes.append(self)

    def agregar_cliente_lista_centro(self, lista_centro):
        if self not in lista_centro:
            lista_centro.append(self)
        else:
            print("Lo sentimos, pero este cliente ya está en la lista del centro")

    def quitar_cliente(self, lista_centro):
        if self not in lista_centro:
            lista_centro.remove(self)
        else:
            print("No se puede eliminar el cliente porque tiene reservas hechas")

    def mostrar_morosos(self):
        for cliente in lista_clientes:
            if cliente.saldo <= -2000:
                print(f"{cliente.nombre} - {cliente.apellido}")

class Empleados(Persona):
    def __init__(self, nombre, apellido, desocupado, lista_tareas = []):
        super().__init__(nombre, apellido)
        self.desocupado = desocupado
        self.lista_tareas = lista_tareas

    def crear_empleado(self):
        lista_empleados.append(self)

    def registrar_empleado_cancha(self, cancha):
        cancha.lista_empleados.append(self)

    def agregar_tareas(self, tarea):
        self.append(tarea)

    def quitar_tareas(self, tarea):
        self.lista_tareas.remove(self.lista_tareas[tarea])
                           
    def imprimir_descopudaos(self, lista_emlpeados):
        for empleado in lista_emlpeados:
            if empleado.desocpuado == True:
                print(f"{empleado.nombre}")

    def quitar_empleado_de_cancha(self, cancha):
        cancha.lista_empleados.remove(self)
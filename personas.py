class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.nombre} {self.apellido} "
        

class Clientes(Persona):
    def __init__(self, nombre, apellido, telefono, identificador, saldo, lista_reservas = []):
        super().__init__(nombre, apellido)
        self.telefono = telefono
        self.identificador = identificador
        self.saldo = saldo
        self.lista_reservas = lista_reservas

    def __str__(self):
        return super().__str__() + f"Teléfono: {self.telefono} - ID: {self.identificador} - Saldo: {self.saldo}"

    def agregar_cliente_lista_centro(self, lista_centro_clientes):
        if self not in lista_centro_clientes:
            lista_centro_clientes.append(self)
        else:
            print("Lo sentimos, pero este cliente ya está en la lista del centro")

    def quitar_cliente(self, lista_centro_clientes):
        if self not in lista_centro_clientes:
            lista_centro_clientes.remove(self)
        else:
            print("No se puede eliminar el cliente porque tiene reservas hechas")

    def mostrar_morosos(self, lista_centro_clientes):
        for cliente in lista_centro_clientes:
            if cliente.saldo <= -2000:
                print(f"{cliente.nombre} - {cliente.apellido}")

    def listar_reservas_cliente(self, lista_centro_clientes):
            if self in lista_centro_clientes:
                for reserva in self.lista_reservas:
                    print(f"El cliente {self.nombre} {self.apellido} tiene reservada la cancha {reserva.cancha} con fecha de {reserva.fecha}")

class Empleados(Persona):
    def __init__(self, nombre, apellido, desocupado, lista_tareas = []):
        super().__init__(nombre, apellido)
        self.desocupado = desocupado
        self.lista_tareas = lista_tareas

    def __str__(self):
        return super().__str__() + f"Estado: {self.desocupado}"

    def crear_empleado(self, lista_centro_emplpeados):
        lista_centro_emplpeados.append(self)

    def registrar_empleado_cancha(self, cancha):
        cancha.lista_empleados.append(self)

    def agregar_tareas(self, tarea):
        self.append(tarea)

    def quitar_tareas(self, tarea):
        self.lista_tareas.remove(self.lista_tareas[tarea])
                           
    def imprimir_descopudaos(self, lista_centro_empleados):
        for empleado in lista_centro_empleados:
            if empleado.desocpuado == True:
                print(f"{empleado.nombre}")

    def quitar_empleado_de_cancha(self, cancha):
        cancha.lista_empleados.remove(self)
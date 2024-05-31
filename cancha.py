class Cancha:
    
    def __init__(self, num_cancha, deporte, precio, habilitada = True, lista_reservas = None, lista_empleados = None):
        self.num_cancha = num_cancha
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.lista_reservas = lista_reservas if lista_reservas is not None else []
        self.lista_empleados = lista_empleados if lista_empleados is not None else []
        
    def __str__(self):
        return f"Cancha: {self.num_cancha}. Deporte: {self.deporte}. Precio: {self.precio}"

    def agregar_cancha_a_centro(self, lista_centro_canchas):
        if self not in lista_centro_canchas:
            lista_centro_canchas.append(self)
        else:
            print("Lo sentimos, pero esa cancha ya está en la lista del centro")

    def listar_canchas_por_deporte(tipo_deporte, lista_centro_canchas):
        canchas_disponibles_para_deporte = False
        for cancha in lista_centro_canchas:
            if cancha.deporte == tipo_deporte:
                print(cancha)
                canchas_disponibles_para_deporte = True
        if canchas_disponibles_para_deporte == False:
            print(f"No hay canchas disponibles para hacer {tipo_deporte}")
        
    def quitar_cancha(self, lista_centro_canchas):
        if len(self.lista_reservas) == 0:
            lista_centro_canchas.remove(self)
            print(f"La cancha con numero {self.num_cancha} en la que se practica "
            f"{self.deporte} ha sido eliminada")
        else:
            print("No se puede eliminar la cancha porque tiene reservas pendientes")

    
    def registrar_empleado_cancha(self, empleado):
        if empleado not in self.lista_empleados:
            self.lista_empleados.append(empleado)
            print(f"{empleado.nombre} ha sido asignado a la cancha {self.num_cancha}.")
        else:
            print(f"{empleado.nombre} ya está asignado a esta cancha.") 
        
    def quitar_empleado_de_cancha(self, empleado):
        self.lista_empleados.remove(empleado)
        
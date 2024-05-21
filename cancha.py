from centro_Pablo import Centro

class Cancha:
    
    def __init__(self, num_cancha, deporte, precio, habilitada = True, lista_reservas = [], lista_empleados = []):
        self.num_cancha = num_cancha
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.lista_reservas = lista_reservas
        self.lista_empleados = lista_empleados
        
    def __str__(self):
        return f"Cancha: {self.num_cancha}. Deporte: {self.deporte}. Precio: {self.precio}"

    def agregar_cancha_a_centro(self):
        if self not in Centro.lista_cancha:
            Centro.lista_cancha.append(self)
        else:
            print("Lo sentimos, pero esa cancha ya está en la lista del centro")

    @staticmethod
    def listar_canchas_por_deporte(tipo_deporte):
        canchas_disponibles_para_deporte = False
        for cancha in Centro.lista_canchas:
            if cancha.deporte == tipo_deporte:
                print(cancha)
                canchas_disponibles_para_deporte = True
        if canchas_disponibles_para_deporte == False:
            print(f"No hay canchas disponibles para hacer {tipo_deporte}")
        

    def quitar_cancha(self):#cambiado a Centro.lista_cancha
        if not self.lista_reservas:
            Centro.lista_cancha.remove(self)
        else:
            print("No se puede eliminar la cancha porque tiene reservas pendientes")
            
    
        
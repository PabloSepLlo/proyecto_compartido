lista_canchas = []

class cancha:
    def __init__(self, num_cancha, deporte, precio, habilitada = True, lista_reservas = [], lista_empleados = []):
        self.num_cancha = num_cancha
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.lista_reservas = lista_reservas
        self.lista_empleados = lista_empleados
        
    def añadir_cancha(self):
        lista_canchas.append(self)
        
    def agregar_cancha_a_centro(self, lista_centro):
        if self not in lista_centro:
            lista_centro.append(self)
        else:
            print("Lo sentimos, pero esa cancha ya está en la lista del centro")
    
    def listar_canchas(self):
        diccionario = {}
        for cancha in lista_canchas:
            if cancha not in diccionario:
                diccionario[cancha.deporte] = 1
            else:
                diccionario[cancha.deporte] += 1
        return diccionario
    
    def listar_reservas_cancha(self):
        for reserva in range(len(self.lista_reservas)):
            print(f"La cancha con numero {self.num_cancha} tiene el numero de identificacion {self.lista_reservas[reserva].num_reserva} 
            con fecha {self.lista_reservas[reserva].num_reserva}")
                
    def quitar_cancha(self, lista_centro):
        if not self.lista_reservas:
            lista_centro.remove(self)
        else:
            print("No se puede eliminar la cancha porque tiene reservas pendientes")
            
            
    
        
lista_reserva = []

class Reserva:
    def __init__(self, num_reserva, fecha, cliente, cancha):
        self.num_reserva = num_reserva
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha
            
    def listar_reservas_cliente(self, cliente):
        for self in lista_reserva:
            if cliente in self:
                print(f"El cliente {cliente.nombre} {cliente.apellido} tiene reservada la cancha {self.cancha} con fecha de {self.fecha}")
                
    def pagar_cancha(self, cliente, cancha, centro):
        cancha_pagada = False
        if (cliente.saldo - cancha.precio) >= -2000:
            cliente.saldo -= cancha.precio
            centro.saldo += cancha.precio
            print(cliente.saldo)
            cancha_pagada = True
        else: 
            print("No hay suficiente saldo para realizar la reserva ")
        return cancha_pagada
        
class Reserva:
    
    def __init__(self, num_reserva, fecha, cliente, cancha):
        self.num_reserva = num_reserva
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha
                
    def pagar_cancha(self, cliente, cancha, saldo_centro):
        cancha_pagada = False
        if (cliente.saldo - cancha.precio) >= -2000:
            cliente.saldo -= cancha.precio
            saldo_centro += cancha.precio
            print(f"Ahora el saldo del cliente es {cliente.saldo}")
            cancha_pagada = True
        else: 
            print("No hay suficiente saldo para realizar la reserva: ") 
        return cancha_pagada
        
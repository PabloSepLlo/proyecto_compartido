from cancha import Cancha
from personas import Clientes, Empleados
from reserva import Reserva

class Centro2:
    def __init__(self, nombre, direccion, lista_clientes=[], lista_canchas=[], lista_empleados=[], lista_reservas=[]):
        self.nombre = nombre
        self.direccion = direccion
        self.lista_clientes = lista_clientes
        self.lista_canchas = lista_canchas
        self.lista_empleados = lista_empleados
        self.lista_reservas = lista_reservas

    def añadir_cliente(self):
        nombre = input("Escriba su nombre: ")
        apellido = input("Escriba su apellido: ")
        telefono = input("Escriba su telefono: ")
        identificador = input("Escriba su identificador: ")
        saldo = float(input("Escriba el dinero que va a introducir como saldo inicial: "))
        cliente = Clientes(nombre, apellido, telefono, identificador, saldo)
        cliente.agregar_cliente_lista_centro(self.lista_clientes)
        print(f"Cliente {nombre} {apellido} añadido con éxito.")

    def añadir_cancha(self):
        num_cancha = int(input("Escriba el número de la cancha: "))
        deporte = input("Escriba el deporte que se practica en la cancha: ")
        precio = float(input("Escriba el precio que cuesta usar la cancha: "))
        cancha = Cancha(num_cancha, deporte, precio)
        cancha.agregar_cancha_a_centro(self.lista_canchas)
        print(f"Cancha {num_cancha} añadida con éxito.")

    def mostrar_cancha(self):
        for indice, cancha in enumerate(self.lista_canchas):
            print(f"{indice}: {cancha}")

    def eliminar_cancha(self):
        self.mostrar_cancha()
        seleccion = int(input("Indique el número (índice) de la cancha que quiere eliminar: "))
        cancha_a_eliminar = self.lista_canchas[seleccion]
        cancha_a_eliminar.quitar_cancha(self.lista_canchas)
        if cancha_a_eliminar not in self.lista_canchas:
            print("Cancha eliminada con éxito.")
        else:
            print("No se pudo eliminar la cancha porque tiene reservas pendientes.")

    def mostrar_cliente(self):
        for indice, cliente in enumerate(self.lista_clientes):
            print(f"{indice}: {cliente}")

    def eliminar_cliente(self):
        self.mostrar_cliente()
        seleccion = int(input("Indique el número (índice) del cliente que quiere eliminar: "))
        self.lista_clientes[seleccion].quitar_cliente(self.lista_clientes)
        print(f"Cliente {self.lista_clientes[seleccion].nombre} {self.lista_clientes[seleccion].apellido} eliminado con éxito.")

    def consultar_disponibilidad_cancha_por_deporte(self):
        tipo_deporte = input("Indique qué deporte quiere practicar para consultar si hay canchas disponibles: ")
        Cancha.listar_canchas_por_deporte(tipo_deporte, self.lista_canchas)

    def reservar_cancha(self):
        print("CANCHAS:")
        self.mostrar_cancha()
        cancha_seleccionada = int(input("Indique el número (índice) de la cancha que quiere reservar: "))
        print("CLIENTES:")
        self.mostrar_cliente()
        cliente_seleccionado = int(input("Indique el número (índice) del cliente que quiere realizar la reserva: "))
        fecha_reserva = input("Indique la fecha de la reserva (DD/MM/AAAA): ")
        
        cancha = self.lista_canchas[cancha_seleccionada]
        cliente = self.lista_clientes[cliente_seleccionado]
        num_reserva = len(self.lista_reservas) + 1
        
        reserva = Reserva(num_reserva, fecha_reserva, cliente, cancha)
        self.lista_reservas.append(reserva)
        cancha.lista_reservas.append(reserva)
        cliente.lista_reservas.append(reserva)
        
        if reserva.pagar_cancha(cliente, cancha, self):
            print(f"Reserva realizada con éxito para el cliente {cliente.nombre} {cliente.apellido} en la cancha {cancha.num_cancha} el {fecha_reserva}.")
        else:
            self.lista_reservas.remove(reserva)
            cancha.lista_reservas.remove(reserva)
            cliente.lista_reservas.remove(reserva)
            print("No se pudo realizar la reserva debido a fondos insuficientes.")

    def mostrar_reservas_cliente(self):
        self.mostrar_cliente()
        seleccion = int(input("Indique el número (índice) del cliente del que quiere consultar las reservas: "))
        cliente = self.lista_clientes[seleccion]
        Reserva.listar_reservas_cliente(cliente)

    def menu():
        while True:
            opcion = int(input("1. Añadir cliente\n2. Añadir cancha\n3. Mostrar cancha\n4. Mostrar cliente\n"
                               "5. Eliminar cancha\n6. Eliminar cliente\n7. Consultar disponiblidad de cancha\n"
                               "8. Reservar cancha\n9. Mostrar reservas del cliente\n10. Salir\nIntroduce tu elección: "))
            if opcion == 1:
                Centro2.añadir_cliente(Centro2)
            elif opcion == 2:
                Centro2.añadir_cancha(Centro2)
            elif opcion == 3:
                Centro2.mostrar_cancha(Centro2)
            elif opcion == 4:
                Centro2.mostrar_cliente(Centro2)
            elif opcion == 5:
                Centro2.eliminar_cancha(Centro2)
            elif opcion == 6:
                Centro2.eliminar_cliente(Centro2)
            elif opcion == 7:
                Centro2.consultar_disponibilidad_cancha_por_deporte(Centro2)
            elif opcion == 8:
                Centro2.reservar_cancha(Centro2)
            elif opcion == 9:
                Centro2.mostrar_reservas_cliente(Centro2)
            elif opcion == 10:
                break
            else:
                print("Opción no válida")

Centro2.menu()
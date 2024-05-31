from cancha import Cancha
from personas import Clientes, Empleados
from reserva import Reserva

class Centro2:
    
    nombre = "Centro deportivo San Miguel"
    direccion = "Calle del deporte S/N"
    lista_clientes = []
    lista_canchas = []
    lista_empleados = []
    lista_reservas = []
    saldo_centro = 0

    @classmethod
    def añadir_cliente(cls):
        try:
            nombre = input("Escriba su nombre: ")
            apellido = input("Escriba su apellido: ")
            telefono = input("Escriba su telefono: ")
            identificador = input("Escriba su identificador: ")
            saldo = float(input("Escriba el dinero que va a introducir como saldo inicial: "))
        except ValueError as err:
            print("Alguno de los datos de cliente introducidos no es del tipo correcto")
            print("Mensaje: ", err)
        else:
            cliente = Clientes(nombre, apellido, telefono, identificador, saldo)
            cliente.agregar_cliente_lista_centro(cls.lista_clientes)
            print(f"Cliente {nombre} {apellido} añadido con éxito.")
        
    @classmethod
    def añadir_empleado(cls):
        try:
            nombre = input("Escriba su nombre: ")
            apellido = input("Escriba su apellido: ")
            desocupado = input("¿Hay tareas pendientes? ")
        except ValueError as err:
            print("Alguno de los datos de empleado introducidos no es del tipo correcto")
            print("Mensaje: ", err)
        else:
            empleado = Empleados(nombre, apellido, desocupado)
            empleado.añadir_empleado(cls.lista_empleados)
            print(f"El empleado {nombre} {apellido} ha sido contratado.")

    @classmethod
    def añadir_cancha(cls):
        try:
            num_cancha = int(input("Escriba el número de la cancha: "))
            deporte = input("Escriba el deporte que se practica en la cancha: ")
            precio = float(input("Escriba el precio que cuesta usar la cancha: "))
            habilitada = "True"
        except ValueError as err:
            print("Alguno de los datos de cancha introducidos no es del tipo correcto")
            print("Mensaje: ", err)
        else:
            cancha = Cancha(num_cancha, deporte, precio, habilitada)
            cancha.agregar_cancha_a_centro(cls.lista_canchas)
            print(f"Cancha {num_cancha} añadida con éxito.")

    @classmethod
    def mostrar_cancha(cls):
        for indice, cancha in enumerate(cls.lista_canchas):
            print(f"{indice}: {cancha}")

    @classmethod
    def eliminar_cancha(cls):
        cls.mostrar_cancha()
        try:
            seleccion = int(input("Indique el número (índice) de la cancha que quiere eliminar: "))
        except ValueError as err:
            print("El indice de la cancha debe ser un entero")
            print("Mensaje: ", err)
        else:
            cancha_a_eliminar = cls.lista_canchas[seleccion]
            cancha_a_eliminar.quitar_cancha(cls.lista_canchas)

    @classmethod
    def mostrar_cliente(cls):
        for indice, cliente in enumerate(cls.lista_clientes):
            print(f"{indice}: {cliente}")

    @classmethod
    def eliminar_cliente(cls):
        cls.mostrar_cliente()
        try:
            seleccion = int(input("Indique el número (índice) del cliente que quiere eliminar: "))
        except ValueError as err:
            print("El indice del cliente debe ser un entero")
            print("Mensaje: ", err)
        else:
            cliente = cls.lista_clientes[seleccion]
            cliente.quitar_cliente(cls.lista_clientes)
            

    @classmethod
    def consultar_disponibilidad_cancha_por_deporte(cls):
        tipo_deporte = input("Indique qué deporte quiere practicar para consultar si hay canchas disponibles: ")
        Cancha.listar_canchas_por_deporte(tipo_deporte, cls.lista_canchas)

    @classmethod
    def reservar_cancha(cls):
        print("CANCHAS:")
        cls.mostrar_cancha()
        print("CLIENTES:")
        cls.mostrar_cliente()
        try:
            cancha_seleccionada = int(input("Indique el número (índice) de la cancha que quiere reservar: "))
            cliente_seleccionado = int(input("Indique el número (índice) del cliente que quiere realizar la reserva: "))
            fecha_reserva = input("Indique la fecha de la reserva (DD/MM/AAAA): ")
        except ValueError as err:
            print("El tipo (o tipos) de dato introducido para realizar una reserva debe ser entero (menos en el caso de la fecha)")
            print("Mensaje: ", err)
        else:
            cancha = cls.lista_canchas[cancha_seleccionada]
            cliente = cls.lista_clientes[cliente_seleccionado]
            num_reserva = len(cls.lista_reservas) + 1
            
            reserva = Reserva(num_reserva, fecha_reserva, cliente, cancha)
            cls.lista_reservas.append(reserva)
            cancha.lista_reservas.append(reserva)
            cliente.lista_reservas.append(reserva)
            
            if reserva.pagar_cancha(cliente, cancha, cls.saldo_centro):
                print(f"Reserva realizada con éxito para el cliente {cliente.nombre} {cliente.apellido} en la cancha {cancha.num_cancha} el {fecha_reserva}.")
            else:
                cls.lista_reservas.remove(reserva)
                cancha.lista_reservas.remove(reserva)
                cliente.lista_reservas.remove(reserva)
                print("No se pudo realizar la reserva debido a fondos insuficientes.")

    @classmethod
    def mostrar_reservas_cliente(cls):
        cls.mostrar_cliente()
        try:
            seleccion = int(input("Indique el número (índice) del cliente del que quiere consultar las reservas: "))
        except ValueError as err:
            print("El indice del cliente debe ser un entero")
            print("Mensaje: ", err)
        else:
            cliente = cls.lista_clientes[seleccion]
            cliente.listar_reservas_cliente(cls.lista_clientes)

    @classmethod
    def menu(cls):
        while True:
            try:
                opcion = int(input("1. Añadir cliente\n2. Añadir cancha\n3. Mostrar cancha\n4. Mostrar cliente\n"
                                "5. Eliminar cancha\n6. Eliminar cliente\n7. Consultar disponibilidad de cancha\n"
                                "8. Reservar cancha\n9. Mostrar reservas del cliente\n10. Salir\nIntroduce tu elección: "))
            except ValueError as err:
                print("La opción debe ser un entero")
                print("Mensaje: ", err)
            else:
                if opcion == 1:
                    cls.añadir_cliente()
                elif opcion == 2:
                    cls.añadir_cancha()
                elif opcion == 3:
                    cls.mostrar_cancha()
                elif opcion == 4:
                    cls.mostrar_cliente()
                elif opcion == 5:
                    cls.eliminar_cancha()
                elif opcion == 6:
                    cls.eliminar_cliente()
                elif opcion == 7:
                    cls.consultar_disponibilidad_cancha_por_deporte()
                elif opcion == 8:
                    cls.reservar_cancha()
                elif opcion == 9:
                    cls.mostrar_reservas_cliente()
                elif opcion == 10:
                    break
                else:
                    print("Opción no válida")

Centro2.menu()

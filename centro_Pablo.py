from cancha import Cancha
from personas import Clientes
from personas import Empleados
from reserva import Reserva

class Centro:
    
    nombre = ""
    direccion = ""
    lista_clientes = []
    lista_canchas = []
    lista_empleados = []
    lista_reservas = []
    saldo = 0
    
    #habría que hacer a lo mejor una lista en clientes también para las reservas que puedan tener
    
    '''def añadir_cliente():
        nombre = str(input("Escriba su nombre: "))
        apellido = str(input("Escriba su apellido: "))
        telefono = int(input("Escriba su telefono: "))
        identificador = int(input("Escriba su identificador: "))
        saldo = int(input("Escriba el dinero que va introducir como saldo inicial: "))
        cliente = Clientes(nombre, apellido, telefono, identificador, saldo) 
        Clientes.agregar_cliente_lista_centro(cliente, Centro.lista_clientes)'''
    
    def añadir_empleado():
        nombre = str(input("Escriba su nombre: "))
        apellido = str(input("Escriba su apellido: "))
        desocupado = str(input("¿Hay tareas pendientes? "))
        empleado = Empleados(nombre, apellido, desocupado)
        empleado.crear_empleado(Centro.lista_empleados)
    
    @staticmethod
    def añadir_cancha():
        num_cancha = int(input("Escriba el numero de la cancha: "))
        deporte = str(input("Escriba el deporte que se prectica en la cancha: "))
        precio = int(input("Escriba el precio que cuesta usar la cancha: "))
        cancha = Cancha(num_cancha, deporte, precio)
        Cancha.agregar_cancha_a_centro(cancha, Centro.lista_canchas)
    
    @staticmethod
    def mostrar_cancha():
        for indice, cancha in enumerate(Centro.lista_canchas):
            print(f"{indice}: {cancha}")
    
    @staticmethod
    def mostrar_cliente():
        for indice, cliente in enumerate(Centro.lista_clientes):
            print(f"{indice}: {cliente}")

    def mostrar_empleados():
        for indice, empleado in enumerate(Centro.lista_empleados):
            print(f"{indice}: {empleado}")
            
    @staticmethod
    def eliminar_cancha():
        Centro.mostrar_cancha()
        seleccion = int(input("Indique el numero (indice) de la cancha que quiere eliminar: "))
        Cancha.quitar_cancha(Centro.lista_cancha[seleccion]) #quitada la lista
    
    @staticmethod
    def eliminar_cliente():
        Centro.mostrar_cliente()
        seleccion = int(input("Indique el numero (indice) del cliente que quiere eliminar: ")) #no quitada la lista
        Clientes.quitar_cliente(Centro.lista_clientes[seleccion], Centro.lista_clientes)
    
    @staticmethod
    def consultar_disponibilidad_cancha_por_deporte():
        seleccion = str(input("Indique qué deporte quiere practicar para consultar si hay canchas disponibles: "))
        Cancha.listar_canchas_por_deporte(seleccion)
    
    @staticmethod
    def reservar_cancha():
        print("CANCHAS:")
        Centro.mostrar_cancha()
        print("CLIENTES:")
        Centro.mostrar_cliente()
        num_reserva = int(input("Escriba el numero de reserva: "))
        num_cancha = int(input("Seleccione el número de la cancha que quiere reservar: "))
        num_cliente = int(input("Seleccione el número del cliente que quiere hacer la reserva: "))
        fecha = str(input("Indique la fecha de la reserva: "))
        reserva = Reserva(num_reserva, fecha, Centro.lista_clientes[num_cliente], Centro.lista_canchas[num_cancha])
        if reserva.pagar_cancha(Centro.lista_clientes[num_cliente], Centro.lista_canchas[num_cancha], Centro.saldo):
            Centro.lista_reservas.append(reserva)
            Centro.lista_clientes[num_cliente].lista_reservas.append(reserva)
            Centro.lista_canchas[num_cancha].lista_reservas.append(reserva)
    
    @staticmethod
    def mostrar_reservas_cliente():
        Centro.mostrar_cliente()
        seleccion = int(input("Indique el numero (indice) del cliente del que quiere consultar las reservas: "))
        print(f"{Centro.lista_clientes[seleccion].nombre} tiene las siguientes reservas: ")
        for reserva in Centro.lista_clientes[seleccion].lista_reservas:
            reserva.listar_reservas_cliente(Centro.lista_clientes[seleccion])
    
    def asignar_tarea_empleado():
        Centro.mostrar_empleados()
        seleccion = int(input("Indique el numero (indice) del empleado al que quiere asignar una tarea: "))
        tarea = str(input("Indique la tarea que quiere asignar: "))
        Centro.lista_empleados[seleccion].agregar_tareas(tarea)
        
        



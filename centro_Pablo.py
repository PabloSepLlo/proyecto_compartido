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
    
    #habría que hacer a lo mejor una lista en clientes también para las reservas que puedan tener
    
    '''def añadir_cliente():
        nombre = str(input("Escriba su nombre: "))
        apellido = str(input("Escriba su apellido: "))
        telefono = int(input("Escriba su telefono: "))
        identificador = int(input("Escriba su identificador: "))
        saldo = int(input("Escriba el dinero que va introducir como saldo inicial: "))
        cliente = Clientes(nombre, apellido, telefono, identificador, saldo) 
        Clientes.agregar_cliente_lista_centro(cliente, Centro.lista_clientes)'''
        
    def añadir_cancha():
        num_cancha = int(input("Escriba el numero de la cancha: "))
        deporte = str(input("Escriba el deporte que se prectica en la cancha: "))
        precio = int(input("Escriba el precio que cuesta usar la cancha: "))
        cancha = Cancha(num_cancha, deporte, precio)
        Cancha.agregar_cancha_a_centro(cancha, Centro.lista_canchas)
    
    def mostrar_cancha():
        for indice, cancha in enumerate(Centro.lista_canchas):
            print(f"{indice}: {cancha}")
    
    def mostrar_cliente():
        for indice, cliente in enumerate(Centro.lista_clientes):
            print(f"{indice}: {cliente}")

    def eliminar_cancha():
        Centro.mostrar_cancha()
        seleccion = int(input("Indique el numero (indice) de la cancha que quiere eliminar: "))
        Cancha.quitar_cancha(Centro.lista_cancha[seleccion]) #quitada la lista
    
    def eliminar_cliente():
        Centro.mostrar_cliente()
        seleccion = int(input("Indique el numero (indice) del cliente que quiere eliminar: ")) #no quitada la lista
        Clientes.quitar_cliente(Centro.lista_clientes[seleccion], Centro.lista_clientes)
    
    def consultar_disponibilidad_cancha_por_deporte():
        seleccion = str(input("Indique qué deporte quiere practicar para consultar si hay canchas disponibles: "))
        Cancha.listar_canchas_por_deporte(seleccion)
    
    def reservar_cancha():
        print("CANCHAS:")
        Centro.mostrar_cancha()
        print("CLIENTES:")
        
    def mostrar_reservas_cliente():
        Centro.mostrar_cliente_cliente()
        seleccion = int(input("Indique el numero (indice) del cliente del que quiere consultar las reservas: "))
        
        
        



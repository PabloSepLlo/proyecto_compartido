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
    @staticmethod
    def añadir_cliente():
        try:
            nombre = str(input("Escriba su nombre: "))
            apellido = str(input("Escriba su apellido: "))
            telefono = int(input("Escriba su telefono: "))
            identificador = int(input("Escriba su identificador: "))
            saldo = int(input("Escriba el dinero que va introducir como saldo inicial: "))
        except ValueError as err:
            print("Alguno de los datos de cliente introducidos no es del tipo correcto")
            print("Mensaje: ", err)
        else:
            cliente = Clientes(nombre, apellido, telefono, identificador, saldo) 
            cliente.agregar_cliente_lista_centro(Centro.lista_clientes)
            print(f"El cliente {nombre} {apellido} se ha registrado con exito")
        
    @staticmethod
    def añadir_empleado():
        try:
            nombre = str(input("Escriba su nombre: "))
            apellido = str(input("Escriba su apellido: "))
            desocupado = "Desocupado"
            empleado = Empleados(nombre, apellido, desocupado)
        except ValueError as err:
            print("Alguno de los datos de empleado introducidos no es del tipo correcto")
            print("Mensaje: ", err)
        else:
            empleado.añadir_empleado(Centro.lista_empleados)
            print(f"El empleado {nombre} {apellido} se ha registrado con exito")
    
    @staticmethod
    def añadir_cancha():
        try:
            num_cancha = int(input("Escriba el numero de la cancha: "))
            deporte = str(input("Escriba el deporte que se prectica en la cancha: "))
            precio = int(input("Escriba el precio que cuesta usar la cancha: "))
            habilitada = "True"
        except ValueError as err:
            print("Alguno de los datos de cancha introducidos no es del tipo correcto")
            print("Mensaje: ", err)
        else:
            cancha = Cancha(num_cancha, deporte, precio, habilitada)
            cancha.agregar_cancha_a_centro(Centro.lista_canchas)
            print(f"La cancha {num_cancha} se ha registrado con exito")
    
    @staticmethod
    def mostrar_cancha():
        for indice, cancha in enumerate(Centro.lista_canchas):
            print(f"{indice}: {cancha}")
    
    @staticmethod
    def mostrar_cliente():
        for indice, cliente in enumerate(Centro.lista_clientes):
            print(f"{indice}: {cliente}")

    @staticmethod
    def mostrar_empleados():
        for indice, empleado in enumerate(Centro.lista_empleados):
            print(f"{indice}: {empleado}")
            
    @staticmethod
    def eliminar_cancha():
        Centro.mostrar_cancha()
        try:
            seleccion = int(input("Indique el numero (indice) de la cancha que quiere eliminar: "))
        except ValueError as err:
            print("El indice de la cancha debe ser un entero")
            print("Mensaje: ", err)
        else:
            Centro.lista_canchas[seleccion].quitar_cancha(Centro.lista_canchas)
                
    @staticmethod
    def eliminar_cliente():
        Centro.mostrar_cliente()
        try:
            seleccion = int(input("Indique el numero (indice) del cliente que quiere eliminar: "))
        except ValueError as err:
            print("El indice del cliente debe ser un entero")
            print("Mensaje: ", err)
        else:
            Centro.lista_clientes[seleccion].quitar_cliente(Centro.lista_clientes)

    @staticmethod
    def consultar_disponibilidad_cancha_por_deporte():
        seleccion = str(input("Indique qué deporte quiere practicar para consultar si hay canchas disponibles: "))
        Cancha.listar_canchas_por_deporte(seleccion, Centro.lista_canchas)
    
    @staticmethod
    def reservar_cancha():
        print("CANCHAS:")
        Centro.mostrar_cancha()
        print("CLIENTES:")
        Centro.mostrar_cliente()
        try:
            num_cancha = int(input("Seleccione el número de la cancha que quiere reservar: "))
            num_cliente = int(input("Seleccione el número del cliente que quiere hacer la reserva: "))
            num_reserva = int(input("Escriba el numero de reserva: "))
            fecha = str(input("Indique la fecha de la reserva: "))
        except ValueError as err:
            print("El tipo (o tipos) de dato introducido para realizar una reserva debe ser entero (menos en el caso de la fecha)")
            print("Mensaje: ", err)
        else:
            reserva = Reserva(num_reserva, fecha, Centro.lista_clientes[num_cliente], Centro.lista_canchas[num_cancha])
            if reserva.pagar_cancha(Centro.lista_clientes[num_cliente], Centro.lista_canchas[num_cancha], Centro.saldo):
                Centro.lista_reservas.append(reserva)
                Centro.lista_clientes[num_cliente].lista_reservas.append(reserva)
                Centro.lista_canchas[num_cancha].lista_reservas.append(reserva)
            print(f"{Centro.lista_clientes[num_cliente].nombre} ha realizado una reserva para jugar al {Centro.lista_canchas[num_cancha].deporte}")
    
    @staticmethod
    def mostrar_clientes_morosos():
        for cliente in Centro.lista_clientes:
            if cliente.saldo < 0:
                print(f"{cliente.nombre} tiene un saldo negativo.")
                
    @staticmethod
    def mostrar_reservas_cliente():
        Centro.mostrar_cliente()
        try:
            seleccion = int(input("Indique el numero (indice) del cliente del que quiere consultar las reservas: "))
        except ValueError as err:
            print("El indice del cliente debe ser un entero")
            print("Mensaje: ", err)
        else:
            print(f"{Centro.lista_clientes[seleccion].nombre} tiene las siguientes reservas: ")
            Clientes.listar_reservas_cliente(Centro.lista_clientes[seleccion], Centro.lista_clientes)
    
    @staticmethod
    def asignar_tarea_empleado():
        Centro.mostrar_empleados()
        try:
            seleccion = int(input("Indique el numero (indice) del empleado al que quiere asignar una tarea: "))
            tarea = str(input("Indique la tarea que quiere asignar: "))
        except ValueError as err:
            print("El indice del empleado debe ser un numero entero")
            print("Mensaje: ", err)
        else:
            Centro.lista_empleados[seleccion].agregar_tareas(tarea)
            Centro.lista_empleados[seleccion].desocupado = "Ocupado"
        
    @staticmethod
    def quitar_tarea_empleado():
        Centro.mostrar_empleados()
        try:
            seleccion = int(input("Indique el numero (indice) del empleado al que quiere quitar una tarea: "))
        except ValueError as err:
            print("El indice del empleado debe ser un numero entero")
            print("Mensaje: ", err)
        else:
            if Centro.lista_empleados[seleccion].desocupado == "Ocupado":
                print("Las tareas de este empleado son:")
                for indice, tarea in enumerate(Centro.lista_empleados[seleccion].lista_tareas):
                    print(f"{indice}: {tarea}")
                try:
                    tarea_que_quitar = int(input("Escriba el indice de la tarea que quiere retirar: "))
                except ValueError as err:
                    print("El indice de la tarea debe ser un numero entero")
                    print("Mensaje: ", err)
                else:
                    Centro.lista_empleados[seleccion].quitar_tareas(Centro.lista_empleados[seleccion].lista_tareas[tarea_que_quitar])                    
            else:
                print("Este empleado no tiene tareas asignadas")
            if len(Centro.lista_empleados[seleccion].lista_tareas)== 0:
                Centro.lista_empleados[seleccion].desocupado = "Desocupado"
                print("Este empleado esta ahora desocupado")
    
    @staticmethod
    def mostrar_empleados_desocupados():
        desocupados = False
        for empleado in Centro.lista_empleados:
            if empleado.desocupado == "Desocupado":
                print(f"{empleado.nombre} no tiene tareas asignadas.")
                desocupados = True
        if desocupados == False:
            print("Todos lo empleados están ocupados")
                
    @staticmethod
    def asignar_cancha_a_empleado():
        print("CANCHAS:")
        Centro.mostrar_cancha()
        print("EMPLEADOS:")
        Centro.mostrar_empleados()
        try:
            num_cancha = int(input("Seleccione el número de la cancha a la que quiere asignar un empleado: "))
            num_empleado = int(input("Seleccione el número de empleado que quiere asignar: "))
        except ValueError as err:
            print("Tanto como el numero de cancha como el de empleado deben ser enteros")
            print("Mensaje: ", err)
        else:
            Centro.lista_canchas[num_cancha].registrar_empleado_cancha(Centro.lista_empleados[num_empleado])
    
    @staticmethod
    def quitar_empleado_cancha():
        print("CANCHAS:")
        Centro.mostrar_cancha()
        try:
            num_cancha = int(input("Seleccione el número de la cancha de la que quiere quitar un empleado: "))
        except ValueError as err:
            print("El indice de la cancha debe ser un numero entero")
            print("Mensaje: ", err)
        else:
            if len(Centro.lista_canchas[num_cancha].lista_empleados) > 0:
                for index, empleado in enumerate(Centro.lista_canchas[num_cancha].lista_empleados):
                    print(f"{index}: {empleado.nombre}")
                try:
                    num_empleado = int(input("Seleccione el número de empleado que quiere quitar de la cancha: "))
                except ValueError as err:
                    print("El indice del empleado debe ser un numero entero")
                    print("Mensaje: ", err)
                else:
                    print(f"{Centro.lista_canchas[num_cancha].lista_empleados[num_empleado].nombre} se ha quitado de la cancha")
                    Centro.lista_canchas[num_cancha].quitar_empleado_de_cancha(Centro.lista_canchas[num_cancha].lista_empleados[num_empleado])

            else: 
                print("La cancha no tiene empleados asignados")
        
    def run():
        while True:
            print("OPCIONES DISPONIBLES")
            print("1. Operaciones sobre clientes.")
            print("2. Operaciones sobre empleados.")
            print("3. Operaciones sobre canchas.")
            print("4. Salir")
            try:
                seleccion = int(input("Seleccione sobre qué quiere realizar operaciones: "))
            except ValueError as err:
                print("La seleccion debe ser un numero entero")
                print("Mensaje: ", err)
            else:
                match seleccion:
                    case 1:
                        print("OPERACIONES CLIENTE")
                        print("1. Añadir cliente.")
                        print("2. Mostrar reservas cliente.")
                        print("3. Mostrar lista clientes morosos")
                        print("4. Eliminar cliente.")
                        print("5. Volver al menu principal.")
                        try:
                            seleccion = int(input("Seleccione sobre qué quiere realizar operaciones: "))
                        except ValueError as err:
                            print("La seleccion debe ser un numero entero")
                            print("Mensaje: ", err)
                        else:
                            match seleccion:
                                case 1:
                                    Centro.añadir_cliente()
                                case 2:
                                    Centro.mostrar_reservas_cliente()
                                case 3:
                                    Centro.mostrar_clientes_morosos()
                                case 4:
                                    Centro.eliminar_cliente()
                                case 5:
                                    pass
                                case _:
                                    print("Esta opcion de cliente no está contemplada")
                    case 2:
                        print("OPERACIONES EMPLEADO")
                        print("1. Añadir empleado.")
                        print("2. Asignar tarea a empleado.")
                        print("3. Quitar tarea empleado")
                        print("4. Mostrar empleados desocupados.")
                        print("5. Asignar a un empleado a una cancha.")
                        print("6. Quitar empleado de una cancha.")
                        print("7. Volver al menu pricipal.")
                        try:
                            seleccion = int(input("Seleccione sobre qué quiere realizar operaciones: "))
                        except ValueError as err:
                            print("La seleccion debe ser un numero entero")
                            print("Mensaje: ", err)
                        else:
                            match seleccion:
                                case 1:
                                    Centro.añadir_empleado()
                                case 2:
                                    Centro.asignar_tarea_empleado()
                                case 3:
                                    Centro.quitar_tarea_empleado()
                                case 4:
                                    Centro.mostrar_empleados_desocupados()
                                case 5:
                                    Centro.asignar_cancha_a_empleado()
                                case 6:
                                    Centro.quitar_empleado_cancha()
                                case 7:
                                    pass
                                case _:
                                    print("Esta opcion de empleado no está contemplada")
                    case 3:
                        print("OPERACIONES CANCHA")
                        print("1. Añadir cancha.")
                        print("2. Eliminar cancha.")
                        print("3. Consultar disponibilidad de canchas por deporte.")
                        print("4. Reservar cancha.")
                        print("5. Volver al menu pricipal.")
                        try:
                            seleccion = int(input("Seleccione sobre qué quiere realizar operaciones: "))
                        except ValueError as err:
                            print("La seleccion debe ser un numero entero")
                            print("Mensaje: ", err)
                        else:
                            match seleccion:
                                case 1:
                                    Centro.añadir_cancha()
                                case 2:
                                    Centro.eliminar_cancha()
                                case 3:
                                    Centro.consultar_disponibilidad_cancha_por_deporte()
                                case 4:
                                    Centro.reservar_cancha()
                                case 5:
                                    pass
                                case _:
                                    print("Esta opcion de canchas no está contemplada")
                    case 4:
                        break
                    case _:
                        print("La opcion no está disponible")
Centro.run()
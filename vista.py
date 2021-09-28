import controlador
import os
import pyfiglet
import re

regex = r"^[0-9]+$"


def inicio():
    limpiar_terminal()
    hay_tiempo = True
    while hay_tiempo:
        print("\n")
        print("──────────────▄▀█▀█▀▄")
        print("─────────────▀▀▀▀▀▀▀▀▀ ")
        print("─────────────▄─░░░░░▄")
        print("───█──▄─▄───▐▌▌░░░░░▌▌")
        print("▌▄█▐▌▐█▐▐▌█▌█▌█░░░░░▌▌")

        titulo = pyfiglet.figlet_format("Dia del juicio final")
        print(titulo)

        print(
            "Tienes solo unos minutos para prepararte, antes de una invasión alienígena."
        )
        print("Te hemos asignado una bóveda para guardar tus elementos personales.")
        print("Un Bot te ayudara a continuar.\n")

        print("Mensaje del bot---------->\n")
        print("Para acceder a tu bóveda, presiona 1.")
        print("Si no quieres acceder a tu bóveda, presiona 2.")
        print("Para salir, presiona 3.\n")

        respuesta = input("Su respuesta: ")
        ejercutar_seleccion_inicio(respuesta)


def mostrar_bot_error_id():
    print("Mensaje del bot---------->")
    mensaje_error = pyfiglet.figlet_format("ERROR")
    print(mensaje_error)
    print("Porfavor ingrese un ID valido\n")
    print("░░░░░░░▄█▄▄▄█▄")
    print("▄▀░░░░▄▌─▄─▄─▐▄░░░░▀▄")
    print("█▄▄█░░▀▌─▀─▀─▐▀░░█▄▄█")
    print("░▐▌░░░░▀▀███▀▀░░░░▐▌")
    print("████░▄█████████▄░████")


def mostrar_bot_con_error():
    mensaje_error = pyfiglet.figlet_format("ERROR")
    print(mensaje_error)
    print("\nNo has ingresado una opcion valida\n")
    print("░░░░░░░▄█▄▄▄█▄")
    print("▄▀░░░░▄▌─▄─▄─▐▄░░░░▀▄")
    print("█▄▄█░░▀▌─▀─▀─▐▀░░█▄▄█")
    print("░▐▌░░░░▀▀███▀▀░░░░▐▌")
    print("████░▄█████████▄░████")


def mostrar_calavera():
    print("Tenías solo dos opciones disponibles!\n")
    print("Has colmado la paciencia del bot, y quedaste a merced de los alienigenas.\n")
    print("──▄────▄▄▄▄▄▄▄────▄───")
    print("─▀▀▄─▄█████████▄─▄▀▀──")
    print("─────██─▀███▀─██──────")
    print("───▄─▀████▀████▀─▄────")
    print("─▀█────██▀█▀██────█▀──")
    print("Los alienígenas te han asesinado.\n")

    respuesta = input("Presiona una tecla para salir")
    exit()


def ejercutar_seleccion_inicio(respuesta):
    if re.match(regex, respuesta):
        if respuesta == "1":
            acceder_a_menu_de_boveda()
        elif respuesta == "2":
            mostrar_mensaje_final()
        elif respuesta == "3":
            exit()
        else:
            mostrar_rta_mal_elegida_menu_inicial()
            respuesta = input("Su respuesta: ")
            limpiar_terminal()
            ejercutar_seleccion_inicio(respuesta)
    else:
        mostrar_rta_mal_elegida_menu_inicial()
        respuesta = input("Su respuesta: ")
        limpiar_terminal()
        ejercutar_seleccion_inicio(respuesta)


def mostrar_rta_mal_elegida_menu_inicial():
    mostrar_bot_con_error()
    print("\nVolveremos a empezar:\n")
    print("Mensaje del bot---------->\n")
    print("Para acceder a tu bóveda, presiona 1.")
    print("Si no quieres acceder a tu bóveda, presiona 2.")
    print("Para salir, presiona 3.\n")


def mostrar_mensaje_final():
    limpiar_terminal()
    print("Oh no! Has sido interceptado por un alienígena!")
    print("Mensaje de alienígena---------->")
    mensaje = pyfiglet.figlet_format("...este humano vendra con nosotros...")
    print(mensaje)
    print("▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒")
    print("▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒")
    print("▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒")
    print("▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒")
    print("▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒")

    print("\nEl bot te ayudará, no te preocupes!")
    print("Mensaje del bot---------->")
    print("\nVolveremos a empezar:\n")
    print("Para acceder a tu bóveda, presiona 1.")
    print("Para salir, presiona 2.\n")

    respuesta = input("Su respuesta: ")
    limpiar_terminal()

    if re.match(regex, respuesta):
        if respuesta == "1":
            acceder_a_menu_de_boveda()
        elif respuesta == "2":
            exit()
        else:
            mostrar_calavera()
    else:
        mostrar_calavera()


def acceder_a_menu_de_boveda():
    limpiar_terminal()
    mensaje = pyfiglet.figlet_format("BOVEDA")
    print(mensaje)
    print("Mensaje del bot---------->")
    print("Has accedido a la boveda BÓVEDA, que quieres hacer?")
    mostrar_menu_principal()
    ejecutar_seleccion_menu()


def limpiar_terminal():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)


def mostrar_mensaje_despedida():
    print("Usted y su boveda llegarán seguros a un nuevo mundo!\n")
    print("Por favor, aborde la nave para escapar.\n")

    print("──────────▄")
    print("────────▄██")
    print("─▄▀██▀█▀█▀███▀")
    print("▀▀▀▀▀████▀▀▀─")
    print("──────▀██")

    print("\nMensaje del bot---------->\n")
    respuesta = input("Gracias por utilizar mis servicios")
    exit()


def mostrar_menu_principal():
    print("1.   Buscar elemento particular")
    print("2.   Guardar un elemento")
    print("3.   Modificar un elemento")
    print("4.   Quitar un elemento")
    print("5.   Chequear que hay en la bóveda ahora")
    print("6.   Cerrar bóveda\n")


def mostrar_rta_mal_elegida_menu_principal():
    mostrar_bot_con_error()
    print("\nMensaje del bot---------->")
    print("\nVolveremos a empezar, este es el menu principal de tu bóveda:\n")
    mostrar_menu_principal()


def ejecutar_seleccion_menu():
    print("Mensaje del bot---------->")
    opcion_elegida = input("Elija una opción: ")
    limpiar_terminal()
    if opcion_elegida == "1":
        buscar_elemento()
    elif opcion_elegida == "2":
        cargar_elemento()
    elif opcion_elegida == "3":
        modificar_elemento()
    elif opcion_elegida == "4":
        eliminar_elemento()
    elif opcion_elegida == "5":
        imprimir_tabla_de_elementos()
        print("Que desea hacer ahora?\n")
        mostrar_menu_principal()
        ejecutar_seleccion_menu()
    elif opcion_elegida == "6":
        mostrar_mensaje_despedida()
    else:
        mostrar_rta_mal_elegida_menu_principal()
        ejecutar_seleccion_menu()


def buscar_elemento():
    if controlador.obtener_todos_los_elementos() != []:
        print("Mensaje del bot---------->\n")
        print("Como quiere que busqur su elemento?")
        print("Para que lo busque por ID, seleccione 1.")
        print("Para que lo busque por NOMBRE, seleccione 2")
        print("Para volver al menú anterior, presione 3\n")

        entrada_valida = False
        opcion_elegida = input("Elija una opción: ")
        while not entrada_valida:
            if opcion_elegida == "1":
                try:
                    id = input("El ID es: ")
                    limpiar_terminal()
                    elemento = controlador.buscar_elemento_por_id(id)
                    mostrar_elemento(elemento)
                    entrada_valida = True
                except TypeError:
                    mostrar_bot_error_id()
                    buscar_elemento()
            elif opcion_elegida == "2":
                try:
                    nombre = input("El NOMBRE es: ")
                    limpiar_terminal()
                    elemento = controlador.buscar_elemento_por_nombre(nombre)
                    mostrar_elemento(elemento)
                    entrada_valida = True
                except TypeError:
                    print("Mensaje del bot---------->")
                    mensaje_error = pyfiglet.figlet_format("ERROR")
                    print(mensaje_error)
                    print("Porfavor ingrese un NOMBRE valido\n")
                    print("░░░░░░░▄█▄▄▄█▄")
                    print("▄▀░░░░▄▌─▄─▄─▐▄░░░░▀▄")
                    print("█▄▄█░░▀▌─▀─▀─▐▀░░█▄▄█")
                    print("░▐▌░░░░▀▀███▀▀░░░░▐▌")
                    print("████░▄█████████▄░████")
                    buscar_elemento()
            elif opcion_elegida == "3":
                limpiar_terminal()
                mostrar_menu_principal()
                ejecutar_seleccion_menu()
            else:
                limpiar_terminal()
                mostrar_bot_con_error()
                buscar_elemento()
    else:
        limpiar_terminal()
        print("Mensaje del bot---------->")
        print("No puedo buscar un elemento que no está en la bóveda\n")
    print("\nQue desea hacer ahora?\n")
    mostrar_menu_principal()
    ejecutar_seleccion_menu()


def cargar_elemento():
    print("Mensaje del bot---------->")
    print("Insertaré nuevo elemento en la bóveda\n")
    id, nombre, descripcion = obtener_datos_del_elemento()
    controlador.cargar_elemento(id, nombre, descripcion)
    print("\nMensaje del bot---------->")
    print("He insertado un nuevo elemento en la bóveda exitosamente\n")
    print("Que desea hacer ahora?\n")
    mostrar_menu_principal()
    ejecutar_seleccion_menu()


def obtener_datos_del_elemento():
    print("Mensaje del bot---------->\n")
    id = input("Escriba aquí el id: ")
    nombre = input("Escriba aquí el nombre: ")
    descripcion = input("Escriba aquí una descripcion: ")
    return id, nombre, descripcion


def obtener_id_del_elemento():
    print("Mensaje del bot---------->\n")
    id = input("Escriba aquí el id: ")
    return id


def obtener_actualizacion_para_el_elemento():
    print("Si no quiere moficar nada, presione ENTER en cada atributo!\n")
    nombre = input("El nuevo nombre será: ")
    descripcion = input("La nueva descripcion será: ")
    return nombre, descripcion


def modificar_elemento():
    entrada_valida = False
    while not entrada_valida:
        if controlador.obtener_todos_los_elementos() != []:
            imprimir_tabla_de_elementos()
            try:
                id = obtener_id_del_elemento()
                elemento = controlador.buscar_elemento_por_id(id)
                print("Mensaje del bot---------->")
                print(
                    "Actualizare un elemento, por favor ingrese las modificaciones que quiere:"
                )
                nombre, descripcion = obtener_actualizacion_para_el_elemento()
                controlador.actualizar_elemento(id, nombre, descripcion)
                limpiar_terminal()
                print("\nMensaje del bot---------->")
                print("Se ha cargado un elemento correctamente\n")
                print("Que desea hacer ahora?\n")
                entrada_valida = True
            except TypeError:
                limpiar_terminal()
                mostrar_bot_error_id()
        else:
            limpiar_terminal()
            print("Mensaje del bot---------->")
            print("No puedo modificar un elemento que no está en la bóveda\n")
            print("Que desea hacer ahora?\n")
            entrada_valida = True
    mostrar_menu_principal()
    ejecutar_seleccion_menu()


def eliminar_elemento():
    if controlador.obtener_todos_los_elementos() != []:
        imprimir_tabla_de_elementos()

        print("Mensaje del bot---------->\n")
        print("Para que lo borre el elemento por ID, seleccione 1.")
        print("Para volver al menu anterior, seleccione 2.")
        opcion = input("Opción: ")
        if opcion == "1":
            try:
                id = input("El ID es: ")
                controlador.eliminar_elemento(id)
                limpiar_terminal()
                print("Mensaje del bot---------->")
                print("Se ha eliminado el elemento correctamente\n")
            except TypeError:
                limpiar_terminal()
                mostrar_bot_error_id()
                eliminar_elemento()
        elif opcion == "2":
            limpiar_terminal()
            mostrar_menu_principal()
            ejecutar_seleccion_menu()
        else:
            limpiar_terminal()
            mostrar_bot_con_error()
            eliminar_elemento()
    else:
        limpiar_terminal()
        print("Mensaje del bot---------->")
        print("No puedo eliminar a un elemento que no está en la bóveda\n")
    print("Que desea hacer ahora?\n")
    mostrar_menu_principal()
    ejecutar_seleccion_menu()


def imprimir_tabla_de_elementos():
    elementos = controlador.obtener_todos_los_elementos()
    print("Mensaje del bot---------->")
    if elementos == []:
        mensaje_error = pyfiglet.figlet_format("La boveda esta vacia")
        print(mensaje_error)
    else:
        print("Estos son los elementos que estan actualmente en la bóveda:\n")
        print("************************************************************")
        for elemento in elementos:
            mostrar_elemento(elemento)
        print("************************************************************")
        print("**********Esos son todos los elementos disponibles!*********\n")


def mostrar_elemento(elemento):
    print(f"Id: {elemento.id}")
    print(f"Nombre: {elemento.nombre}")
    print(f"Descripcion: {elemento.descripcion}")

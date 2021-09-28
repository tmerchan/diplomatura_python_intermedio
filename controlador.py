import modelo
import vista


def actualizar_elemento(id, nombre, descripcion):
    elemento = modelo.Elemento.obtener_elemento_por_id(id)
    elemento.actualizar_elemento(nombre, descripcion)


def eliminar_elemento(id):
    elemento = modelo.Elemento.obtener_elemento_por_id(id)
    elemento.borrar_elemento()


def obtener_todos_los_elementos():
    elementos = modelo.Elemento.obtener_todos_los_elementos()
    return elementos


def crear_tabla_db():
    modelo.Elemento.crear_tabla()


def buscar_elemento_por_id(id):
    elemento = modelo.Elemento.obtener_elemento_por_id(id)
    return elemento


def buscar_elemento_por_nombre(nombre):
    elemento = modelo.Elemento.obtener_elemento_por_nombre(nombre)
    return elemento


def cargar_elemento(id, nombre, descripcion):
    elemento = modelo.Elemento(id, nombre, descripcion)
    elemento.guardar_elemento()


if __name__ == "__main__":
    crear_tabla_db()
    vista.inicio()

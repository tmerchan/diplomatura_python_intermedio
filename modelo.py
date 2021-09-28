import database


class Elemento:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def crear_tabla():
        database.cursor.execute(
            "CREATE TABLE IF NOT EXISTS elementos(id text, nombre text, descripcion text)"
        )
        database.connection.commit()

    def borrar_elemento(self):
        database.cursor.execute(f"DELETE FROM elementos WHERE id = '{self.id}'")
        database.connection.commit()

    def guardar_elemento(self):
        database.cursor.execute(
            f'INSERT INTO elementos(id, nombre, descripcion) VALUES("{self.id}", "{self.nombre}", "{self.descripcion}")'
        )
        database.connection.commit()

    def actualizar_elemento(self, nombre, descripcion):
        modificacion_de_campos = ""
        if nombre and not descripcion:
            modificacion_de_campos = f"nombre = '{nombre}'"
            self.nombre = nombre
        elif descripcion and not nombre:
            modificacion_de_campos = f"descripcion = '{descripcion}'"
            self.descripcion = descripcion
        elif nombre and descripcion:
            modificacion_de_campos = (
                f"nombre = '{nombre}', descripcion = '{descripcion}'"
            )
            self.nombre = nombre
            self.descripcion = descripcion
        if modificacion_de_campos:
            query = f"""UPDATE elementos
                        SET {modificacion_de_campos} 
                        WHERE id = '{self.id}' """
            database.cursor.execute(query)
            database.connection.commit()

    @classmethod
    def obtener_elemento_por_id(cls, id):
        database.cursor.execute(f"SELECT * FROM elementos WHERE id = '{id}'")
        row = database.cursor.fetchone()
        id = row[0]
        nombre = row[1]
        descripcion = row[2]
        elemento = cls(id, nombre, descripcion)
        return elemento

    @classmethod
    def obtener_elemento_por_nombre(cls, nombre):
        database.cursor.execute(
            f"SELECT * FROM elementos WHERE nombre = '{nombre}' COLLATE NOCASE"
        )
        row = database.cursor.fetchone()
        id = row[0]
        nombre = row[1]
        descripcion = row[2]
        elemento = cls(id, nombre, descripcion)
        return elemento

    @classmethod
    def obtener_todos_los_elementos(cls):
        rows = database.cursor.execute(f"SELECT * FROM elementos").fetchall()
        lista_de_elementos = []
        for row in rows:
            id = row[0]
            nombre = row[1]
            descripcion = row[2]
            elemento = cls(id, nombre, descripcion)
            lista_de_elementos.append(elemento)
        return lista_de_elementos

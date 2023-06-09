import mysql.connector

class Normativa:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bd_trabajofinal'
        )
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def insert_normativa(self, num_normativa, nombre, descripcion, fecha, organo_legislativo, palabra_clave, id_jurisdiccion, id_tipo_normativa, id_categoria):
        query = "INSERT INTO normativa (num_normativa, nombre, descripcion, fecha, organo_legislativo, palabra_clave, id_jurisdiccion, id_tipo_normativa, id_categoria) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (num_normativa, nombre, descripcion, fecha, organo_legislativo, palabra_clave, id_jurisdiccion, id_tipo_normativa, id_categoria)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Normativa insertada exitosamente.")

    def select_normativa_by_numero(self, num_normativa):
        query = "SELECT nombre, descripcion FROM normativa WHERE num_normativa = %s"
        values = (num_normativa,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            print("\n")
            print("Nombre:", result[0])
            print("Descripción:", result[1])
            print ("\n")
        else:
            print("\n")
            print("Normativa no encontrada.")

    def update_normativa_nombre(self, num_normativa, nuevo_nombre):
        query = "UPDATE normativa SET nombre = %s WHERE num_normativa = %s"
        values = (nuevo_nombre, num_normativa)
        self.cursor.execute(query, values)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print ("\n")
            print("Normativa actualizada exitosamente.")
        else:
            print ("\n")
            print("Normativa no encontrada.")

    def delete_normativa(self, num_normativa):
        query = "DELETE FROM normativa WHERE num_normativa = %s"
        values = (num_normativa,)
        self.cursor.execute(query, values)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("\n")
            print("Normativa eliminada exitosamente.")
        else:
            print ("\n")
            print("Normativa no encontrada.")

class Programa:
    def __init__(self):
        self.normativa = Normativa()

    def ejecutar(self):
        while True:
            print ("\n")
            print("-------- Menú de Opciones --------")
            print("1. Insertar Normativa")
            print("2. Consultar Normativa por Número")
            print("3. Actualizar Nombre de Normativa")
            print("4. Eliminar Normativa")
            print("5. Salir")
            opcion = input("Seleccione una opcion: ")

            if opcion == '1':
                num_normativa = int(input("Ingrese el número de la normativa: "))
                nombre = input("Ingrese el nombre de la normativa: ")
                descripcion = input("Ingrese la descripción de la normativa: ")
                fecha = input("Ingrese la fecha de la normativa (YYYY-MM-DD): ")
                organo_legislativo = input("Ingrese el órgano legislativo de la normativa: ")
                palabra_clave = input("Ingrese la palabra clave de la normativa: ")
                id_jurisdiccion = int(input("Ingrese el ID de la jurisdicción: "))
                id_tipo_normativa = int(input("Ingrese el ID del tipo de normativa: "))
                id_categoria = int(input("Ingrese el ID de la categoría: "))
                self.normativa.insert_normativa(num_normativa, nombre, descripcion, fecha, organo_legislativo, palabra_clave, id_jurisdiccion, id_tipo_normativa, id_categoria)

            elif opcion == '2':
                num_normativa = int(input("Ingrese el número de la normativa: "))
                self.normativa.select_normativa_by_numero(num_normativa)

            elif opcion == '3':
                num_normativa = int(input("Ingrese el número de la normativa a actualizar: "))
                nuevo_nombre = input("Ingrese el nuevo nombre de la normativa: ")
                self.normativa.update_normativa_nombre(num_normativa, nuevo_nombre)

            elif opcion == '4':
                num_normativa = int(input("Ingrese el número de la normativa a eliminar: "))
                self.normativa.delete_normativa(num_normativa)

            elif opcion == '5':
                break

            else:
                print("\n")
                print("Opción inválida. Por favor, seleccione una opción válida.")
                print("\n")
if __name__ == "__main__":
    programa = Programa()
    programa.ejecutar()

import mysql.connector

class Normativa:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Mysql555',
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
        query = "SELECT nombre, descripcion, fecha, organo_legislativo FROM normativa WHERE num_normativa = %s"
        values = (num_normativa,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            print("Nombre:", result[0])
            print("Descripción:") 
            print(result[1])
            print("Fecha:", result[2])
            print("Organo lesgilativo:", result[3])
        else:
            print("Normativa no encontrada.")
#--------------Select normativa por palabra clave----------------------------
    def select_normativa_by_palabra_clave(self, palabra_clave):
        query = "SELECT num_normatica, nombre, descripcion, fecha, organo_legislativo FROM normativa WHERE palabra_clave = %s"
        values = (palabra_clave,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            print("Número de Normativa:", result[0])
            print("Nombre:", result[1])
            print("Descripción:")
            print(result[2])
            print("fecha:", result[3])
            print("organo_legislativo:", result[4])
        else:
            print("Normativa no encontrada.")
#------------------------------------------------------------------------

    def update_normativa_nombre(self, num_normativa, nuevo_nombre):
        query = "UPDATE normativa SET nombre = %s WHERE num_normativa = %s"
        values = (nuevo_nombre, num_normativa)
        self.cursor.execute(query, values)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Normativa actualizada exitosamente.")
        else:
            print("Normativa no encontrada.")

    def delete_normativa(self, num_normativa):
        query = "DELETE FROM normativa WHERE num_normativa = %s"
        values = (num_normativa,)
        self.cursor.execute(query, values)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("Normativa eliminada exitosamente.")
        else:
            print("Normativa no encontrada.")

class Programa:
    def __init__(self):
        self.normativa = Normativa()

    def ejecutar(self):
        while True:
            print("-------- Menú de Opciones --------" '\n \n' )
            print("1. Insertar Normativa"'\n \n' )
            print("2. Consultar Normativa por Número"'\n \n' )
            print("3. Actualizar Nombre de Normativa"'\n \n' )
            print("4. Eliminar Normativa" '\n \n' )
            print("5. Salir" '\n \n' )

            opcion = input("Seleccione una opción: ")

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
                import time
                import sys
                print("Muchas gracias por utilizar nuestro servicio.")
                time.sleep(3)
                sys.exit()

            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    programa = Programa()
    programa.ejecutar()

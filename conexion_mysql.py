import mysql.connector

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Orionz',  
            database='tienda' 
        )
        print("Conexión exitosa a MySQL")
        return connection
    except mysql.connector.Error as err:
        print("Error de conexión:", err)
        return None

def agregar_producto(nombre, precio, categoria_id):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        
        query = "INSERT INTO productos (nombre, precio, categoria_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (nombre, precio, categoria_id))
        connection.commit() 
        print(f"Producto '{nombre}' agregado con éxito.")
        cursor.close()
        connection.close()

def ver_productos():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        print("Lista de productos:")
        for producto in productos:
            print(producto)
        cursor.close()
        connection.close()


if __name__ == "__main__":
    agregar_producto("Polera", 15.50, 1)  
    agregar_producto("Laptop", 1000.99, 2)  
    agregar_producto("Zapatillas", 60.75, 1) 
    agregar_producto("Audifonos", 120.99, 2) 
    agregar_producto("Silla gamer", 150.25, 3)  
    agregar_producto("Mesa de comedor", 250.00, 3) 
    agregar_producto("Celular", 500.00, 2)  
    agregar_producto("Pantalón", 45.00, 1) 
    agregar_producto("Monitor",180.99, 2) 
    agregar_producto("Cargador portátil", 30.99, 2)
    ver_productos()
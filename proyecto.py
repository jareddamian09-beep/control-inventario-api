from fastapi import FastAPI        
# Se importa  la librería fastapi para usar la clase FastAPI, la cual sirve para crear la API web y realizar operaciones HTTP (GET, POST, PUT y DELETE)

from pymongo import MongoClient
# Se importa la librería pymongo para usar la clase MongoClient, la cual sirve para conectarse a MongoDB.


app = FastAPI()
# Se crea un objeto nuevo de la clase FastAPI y esta se guarda en la variable app para poder definir rutas y manejar peticiones HTTP. 
    
cliente = MongoClient("mongodb://localhost:27017/")
# Conecta Python con MongoDB en nuestro localhost 

db = cliente["control_ventas"]
# Selecciona o crea la base de datos “control_ventas”

productos = db["productos"]
proveedores = db["proveedores"]
clientes = db["clientes"]
sucursales = db["sucursales"]
ventas = db["ventas"]
# Se crean las colecciones que vamos a usar en la base de datos, guardando cada una en una variable. 


@app.get("/")    # Decorador que muestra el objeto, el método y la ruta que va a utilizar.(GET)
def inicio():    # Función inicio
    return {"Mensaje": "API de control de ventas funcionando"}      # Devuelve un diccionario
# Un decorador modifica o agrega comportamiento a una función. 
# Significa: Esta función debe ejecutarse cuando llegue una petición a cierta ruta.  
# Los decoradores se usan para conectar funciones con rutas y métodos HTTP dentro de la API.


@app.post("/productos")                  # Decorador que muestra el objeto, el método y la ruta.(POST)
def agregar_producto(producto: dict):    # Función agregar_producto que espera que la variable producto sea en forma de diccionario. 
 
    productos.insert_one(producto)       # Insertar un documento

    return {"Mensaje": "Producto agregado correctamente"}    # Devuelve un mensaje para verificar que la operación se llevo a cabo con éxito. 


@app.get("/productos")     # Decorador que muestra el objeto, el método y la ruta.(GET)
def obtener_productos():   # Función obtener_productos (No necesita una variable)
    lista = [ ]            # Se crea una lista vacía, ya que ahí se van a guardar los productos.

    for producto in productos.find():            # Busca todos los documentos en la colección productos y recorriendolo uno por uno. 

        producto["_id"] = str(producto["_id"])   # Convierte el "_id" del producto a cadena de texto, ya que la API no puede enviarlo directamente en formato JSON porque MongoDB lo maneja como ObjectId.

        lista.append(producto)                   # Agrega el elemento al final de la lista.

    return lista   # Devuelve toda la lista (productos) en formato JSON.


@app.put("/productos")                                     # Decorador que muestra el objeto, el método y la ruta.(PUT) 
def actualizar_producto(producto_actualizado: dict):       # Función actualizar_producto con la nueva variable producto_actualizado que la espera en forma de diccionario. 

    productos.update_one(                                         # Actualizar un documento 
        {"ID_Producto": producto_actualizado["ID_Producto"]},     # Filtro de búsqueda, en el cual se le indica que producto debe encontrar y actualizar dentro de la colección. 
        {"$set": {                                                # Set sirve para modificar campos específicos (Nombre, Precio y Cantidad).
            "Nombre": producto_actualizado["Nombre"],             # Actualiza el campo Nombre.
            "Precio": producto_actualizado["Precio"],             # Actualiza el campo Producto.
            "Cantidad" : producto_actualizado["Cantidad"]         # Actualiza el campo Cantidad.
        }}
    )
    return {"Mensaje" : "Producto actualizado correctamente"}     # Devuelve un diccionario para verificar que la operación se llevo a cabo con éxito.


@app.delete("/productos")                   # Decorador que muestra el objecto, el metodo y la ruta.(DELETE)
def eliminar_producto(producto: dict):      # Funcion eliminar_producto
    
    productos.delete_one(                          # Eliminar un documento
        {"ID_Producto": producto["ID_Producto"]}   # Filtro de busqueda
    )
    return {"Mensaje" : "Producto eliminado correctamente"}   #Devuelve un diccionario para verificar que la operaacion se llevo a cabo con exito.


@app.post("/proveedores")                 # Decorador que muestra el objeto, el método y la ruta.(POST)
def agregar_proveedor(proveedor: dict):   # Función agregar_proveedor que espera que la variable proveedor sea en forma de diccionario. 
 
    proveedores.insert_one(proveedor)     # Insertar un documento

    return {"Mensaje": "Proveedor agregado correctamente"}   # Devuelve un mensaje para verificar que la operación se llevo a cabo con éxito. 

 
@app.get("/proveedores")        # Decorador que muestra el objeto, el método y la ruta.(GET)
def obtener_proveedores():      # Función obtener_productos (No se necesita una variable)
    lista = [ ]                 # Se crea una lista vacía, porque ahí se van a guardar los productos.

    for proveedor in proveedores.find():           # Busca todos los documentos en la colección proveedores, recorriendolos uno por uno. 

        proveedor["_id"] = str(proveedor["_id"])   # Convierte el "_id" del proveedor a cadena de texto, ya que la API no puede enviarlo directamente en formato JSON, porque MongoDB lo maneja como ObjectId.

        lista.append(proveedor)                    # Agrega el elemento al final de la lista. 

    return lista   # Devuelve toda la lista (proveedores) en formato JSON.


@app.put("/proveedores")                                   # Decorador que muestra el objeto, el método y la ruta.(PUT) 
def actualizar_proveedor(proveedor_actualizado: dict):     # Función actualizar_proveedor con la nueva variable proveedor_actualizado que la espera en forma de diccionario. 

    proveedores.update_one(                                         # Actualizar un documento. 
        {"ID_Proveedor": proveedor_actualizado["ID_Proveedor"]},    # Filtro de búsqueda, en el cual se le indica que proveedor debe encontrar y actualizar dentro de la colección. 
        {"$set": {                                                  # Set sirve para modificar campos específicos (Nombre, Telefono y Correo).
            "Nombre": proveedor_actualizado["Nombre"],              # Actualiza el campo Nombre.
            "Telefono": proveedor_actualizado["Telefono"],          # Actualiza el campo Telefono.
            "Correo" : proveedor_actualizado["Correo"]              # Actualiza el campo Correo.
        }}
    )
    return {"Mensaje" : "Proveedor actualizado correctamente"}     # Devuelve un diccionario para verificar que la operación se llevo a cabo con éxito.


@app.delete("/proveedores")                      # Decorador que muestra el objecto, el metodo y la ruta. (DELETE)
def eliminar_proveedor(proveedor: dict):         # Funcion eliminar_proveedor
    
    proveedores.delete_one(                            # Eliminar un documento
        {"ID_Proveedor": proveedor["ID_Proveedor"]}    # Filtro de busqueda
    )
    return {"Mensaje" : "Proveedor eliminado correctamente"}    #Devuelve un diccionario para verificar que la operaacion se llevo a cabo con exito.


@app.post("/clientes")                 # Decorador que muestra el objeto, el método y la ruta.(POST)
def agregar_cliente(cliente: dict):    # Función agregar_cliente que espera que la variable cliente sea en forma de diccionario. 
 
    clientes.insert_one(cliente)       # Insertar un documento

    return {"Mensaje": "Cliente agregado correctamente"}    # Devuelve un diccionario para verificar que la operación se llevo a cabo con éxito. 


@app.get("/clientes")     # Decorador que muestra el objeto, el método y la ruta.(GET)
def obtener_clientes():   # Función obtener_clientes
    lista = [ ]           # Se crea una lista vacía, porque ahí se van a guardar los productos.

    for cliente in clientes.find():            # Busca todos los documentos en la colección clientes, recorriendolos uno por uno. 

        cliente["_id"] = str(cliente["_id"])   # Convierte el "_id" del cliente a cadena de texto, ya que la API no puede enviarlo directamente en formato JSON porque MongoDB lo maneja como ObjectId.

        lista.append(cliente)   # Agrega el elemento al final de la lista.

    return lista   # Devuelve toda la lista (clientes) en formato JSON.


@app.put("/clientes")                                    # Decorador que muestra el objeto, el método y la ruta.(PUT) 
def actualizar_cliente(cliente_actualizado: dict):       # Función actualizar_cliente con la nueva variable cliente_actualizado que la espera en forma de diccionario. 

    clientes.update_one(                                           # Actualizar un documento 
        {"ID_Cliente": cliente_actualizado["ID_Cliente"]},         # Filtro de búsqueda, en el cual se le indica que cliente debe encontrar y actualizar dentro de la colección. 
        {"$set": {                                                 # Set sirve para modificar campos específicos (Nombre, Telefono, Correo y Tipo_Usuaraio).
            "Nombre": cliente_actualizado["Nombre"],               # Actualiza el campo Nombre
            "Telefono": cliente_actualizado["Telefono"],           # Actualiza el campo Telefono
            "Correo" : cliente_actualizado["Correo"],              # Actualiza el campo Cantidad
            "Tipo_Usuario" : cliente_actualizado["Tipo_Usuario"]   # Actualiza el campo Tipo_Usuario
        }}
    )
    return {"Mensaje" : "Cliente actualizado correctamente"}       # Devuelve un diccionario para verificar que la operación se llevo a cabo con éxito.


@app.delete("/clientes")                    # Decorador que muestra el objecto, el método y la ruta.(DELETE)
def eliminar_cliente(cliente : dict):       # Funcion eliminar_cliente
    
    clientes.delete_one(                         # Eliminar un documento
        {"ID_Cliente": cliente["ID_Cliente"]}    # Filtro de busqueda
    )
    return {"Mensaje" : "Cliente eliminado correctamente"}   # Devuelve un diccionario para verificar que la operaacion se llevo a cabo con exito.


@app.post("/sucursales")                  # Decorador que muestra el objeto, el método y la ruta.(POST)
def agregar_sucursal(sucursal: dict):     # Función agregar_sucursal que espera que la variable sucursal sea en forma de diccionario. 
 
    sucursales.insert_one(sucursal)       # Insertar un documento

    return {"Mensaje": "Sucursal agregada correctamente"}  # Devuelve un mensaje para verificar que la operación se llevo a cabo con éxito. 


@app.get("/sucursales")     # Decorador que muestra el objeto, el método y la ruta.(GET)
def obtener_sucursales():   # Función obtener_ sucursales (No necesita variable)
    lista = [ ]             # Se crea una lista vacía, porque ahí se van a guardar los productos.

    for sucursal in sucursales.find():           # Busca todos los documentos en la colección sucursal, recorriendolos uno por uno. 

        sucursal["_id"] = str(sucursal["_id"])   # Convierte el "_id" de la sucursal a cadena de texto, ya que la API no puede enviarlo directamente en formato JSON porque MongoDB lo maneja como ObjectId.

        lista.append(sucursal)                   # Agrega el elemento al final de la lista. 
    return lista                                 # Devuelve toda la lista (sucursales) en formato JSON.


@app.put("/sucursales")                                     # Decorador que muestra el objeto, el método y la ruta.(PUT) 
def actualizar_sucursal(sucursal_actualizada: dict):        # Función actualizar_sucursal con la nueva variable sucursal_actualizada que la espera en forma de diccionario. 

    sucursales.update_one(                                          # Actualizar un documento 
        {"ID_Sucursal": sucursal_actualizada["ID_Sucursal"]},       # Filtro de búsqueda, en el cual se le indica que producto debe encontrar y actualizar dentro de la colección. 
        {"$set": {                                                  # Set sirve para modificar campos específicos (Nombre, Dirección y Telefono)
            "Nombre": sucursal_actualizada["Nombre"],               # Actualiza el campo Nombre
            "Direccion": sucursal_actualizada["Direccion"],         # Actualiza el campo Dirección
            "Telefono" : sucursal_actualizada["Telefono"],          # Actualiza el campo Telefono
        }}
    )
    return {"Mensaje" : "Sucursal actualizada correctamente"}       # Devuelve un diccionario para verificar que la operación se llevo a cabo con éxito.


@app.delete("/sucursales")                 # Decorador que muestra el objecto, el metodo y la ruta.(DELETE)
def eliminar_sucursal(sucursal: dict):    # Funcion eliminar_sucursal.
    
    sucursales.delete_one(                          # Eliminar un documento
        {"ID_Sucursal": sucursal["ID_Sucursal"]}    # Filtro de busqueda
    )
    return {"Mensaje" : "Sucursal eliminada correctamente"}     # Devuelve un diccionario para verificar que la operaacion se llevo a cabo con exito.


@app.post("/ventas")               # Decorador que muestra el objeto, el método y la ruta.(POST)
def agregar_venta(venta: dict):    # Función agregar_venta que espera que la variable venta sea en forma de diccionario. 
 
    ventas.insert_one(venta)       # Insertar un documento

    return {"Mensaje": "Venta agregada correctamente"}    # Devuelve un mensaje para verificar que la operación se llevo a cabo con éxito. 


@app.get("/ventas")     # Decorador que muestra el objeto, el método y la ruta.(GET)
def obtener_ventas():   # Función obtener_ventas (No necesita variable)
    lista = [ ]         # Se crea una lista vacía, porque ahí se van a guardar los productos.

    for venta in ventas.find():            # Busca todos los documentos en la colección ventas, recorriendolos uno por uno. 

        venta["_id"] = str(venta["_id"])   # Convierte el "_id" de la venta a cadena de texto, ya que la API no puede enviarlo directamente en formato JSON porque MongoDB lo maneja como ObjectId.

        lista.append(venta)                # Agrega el elemento al final de la lista. 
    return lista                           # Devuelve toda la lista (ventas) en formato JSON.


@app.put("/ventas")                                # Decorador que muestra el objeto, el método y la ruta.(PUT) 
def actualizar_venta(venta_actualizada: dict):     # Función actualizar_venta con la nueva variable venta_actualizada que la espera en forma de diccionario. 

    ventas.update_one(                                      # Actualizar un documento 
        {"ID_Venta": venta_actualizada["ID_Venta"]},        # Filtro de búsqueda, en el cual se le indica que venta debe encontrar y actualizar dentro de la colección 
        {"$set": {                                          # Set sirve para modificar campos específicos (ID_Cliente, ID_Producto, ID_Sucursal, Fecha_Venta, Total y Estado)
            "ID_Cliente": venta_actualizada["ID_Cliente"],           # Actualiza el campo ID_Cliente
            "ID_Producto": venta_actualizada["ID_Producto"],         # Actualiza el campo ID_Producto
            "ID_Sucursal" : venta_actualizada["ID_Sucursal"],        # Actualiza el campo ID_Sucursal
            "Fecha_Venta" : venta_actualizada["Fecha_Venta"],        # Actualiza el campo Fecha_Venta
            "Total" : venta_actualizada["Total"],                    # Actualiza el campo Total
            "Estado" : venta_actualizada["Estado"]                   # Actualiza el campo Estado
        }}
    )
    return {"Mensaje" : "Venta actualizada correctamente"}           # Devuelve un diccionario para verificar que la operación se llevo a cabo con éxito.


@app.delete("/ventas")              # Decorador que muestra el objecto, el metodo y la ruta.(DELETE)
def eliminar_venta(venta: dict):    # Funcion eliminar_venta
    
    ventas.delete_one(                         # Eliminar un documento
        {"ID_Venta": venta["ID_Venta"]}        # Filtro de busqueda
    )
    return {"Mensaje" : "Venta eliminada correctamente"}    # Devuelve un diccionario para verificar que la operacion se llevo a cabo con exito.
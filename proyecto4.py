from fastapi import FastAPI        
# Se importa  la librería fastapi para usar la clase FastAPI, la cual sirve para crear la API web y realizar operaciones HTTP (GET, POST, PUT y DELETE)

from pymongo import MongoClient
# Se importa la librería pymongo para usar la clase MongoClient, la cual sirve para conectarse a MongoDB.


app = FastAPI()
# Se crea un objeto nuevo de la clase FastAPI y esta se guarda en la variable app para poder definir rutas y manejar peticiones HTTP. 
    
cliente = MongoClient("mongodb://localhost:27017/")
# Conecta Python con MongoDB en nuestro localhost 

db = cliente["control_administrativo"]
# Selecciona o crea la base de datos “control_administrativo”

productos = db["productos"]
proveedores = db["proveedores"]
usuarios = db["usuarios"]
sucursales = db["sucursales"]
# Se crean las colecciones que vamos a usar en la base de datos, guardando cada una en una variable. 


@app.get("/")    # Decorador que muestra el objeto, el método y la ruta que va a utilizar.(GET)
def inicio():    # Función inicio
    return {"Mensaje": "API de control administrativo funcionando"}      # Devuelve un diccionario
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


@app.post("/usuarios")                 # Decorador que muestra el objeto, el método y la ruta.(POST)
def agregar_usuario(usuario: dict):    # Función agregar_cliente que espera que la variable cliente sea en forma de diccionario. 
 
    usuarios.insert_one(usuario)       # Insertar un documento

    return {"Mensaje": "Usuario agregado correctamente"}    # Devuelve un diccionario para verificar que la operación se llevo a cabo con éxito. 


@app.get("/usuarios")     # Decorador que muestra el objeto, el método y la ruta.(GET)
def obtener_usuarios():   # Función obtener_clientes
    lista = [ ]           # Se crea una lista vacía, porque ahí se van a guardar los productos.

    for usuario in usuarios.find():            # Busca todos los documentos en la colección clientes, recorriendolos uno por uno. 

        usuario["_id"] = str(usuario["_id"])   # Convierte el "_id" del cliente a cadena de texto, ya que la API no puede enviarlo directamente en formato JSON porque MongoDB lo maneja como ObjectId.

        lista.append(usuario)   # Agrega el elemento al final de la lista.

    return lista   # Devuelve toda la lista (clientes) en formato JSON.


@app.put("/usuarios")                                    # Decorador que muestra el objeto, el método y la ruta.(PUT) 
def actualizar_usuario(usuario_actualizado: dict):       # Función actualizar_cliente con la nueva variable cliente_actualizado que la espera en forma de diccionario. 

    usuarios.update_one(                                           # Actualizar un documento 
        {"ID_Cliente": usuario_actualizado["ID_Cliente"]},         # Filtro de búsqueda, en el cual se le indica que cliente debe encontrar y actualizar dentro de la colección. 
        {"$set": {                                                 # Set sirve para modificar campos específicos (Nombre, Telefono, Correo y Tipo_Usuaraio).
            "Nombre": usuario_actualizado["Nombre"],               # Actualiza el campo Nombre
            "Telefono": usuario_actualizado["Telefono"],           # Actualiza el campo Telefono
            "Correo" : usuario_actualizado["Correo"],              # Actualiza el campo Cantidad
    }}
    )
    return {"Mensaje" : "Usuario actualizado correctamente"}       # Devuelve un diccionario para verificar que la operación se llevo a cabo con éxito.


@app.delete("/usuarios")                    # Decorador que muestra el objecto, el método y la ruta.(DELETE)
def eliminar_usuario(usuario : dict):       # Funcion eliminar_cliente
    
    usuarios.delete_one(                         # Eliminar un documento
        {"ID_Cliente": cliente["ID_Cliente"]}    # Filtro de busqueda
    )
    return {"Mensaje" : "Usuario eliminado correctamente"}   # Devuelve un diccionario para verificar que la operaacion se llevo a cabo con exito.


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
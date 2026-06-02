from fastapi import FastAPI
from pymongo import MongoClient
from bson.objectid import ObjectId

app = FastAPI()

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["control_inventario"]

productos = db["productos"]
proveedores = db["proveedores"]
usuarios = db["usuarios"]
sucursales = db["sucursales"]


@app.get("/")
def inicio():
    return { "Mensaje": "API de control administrativo funcionando"}


@app.post("/productos")
def agregar_producto(producto: dict):
    productos.insert_one(producto)
    return { "Mensaje": "Producto agregado correctamente" }


@app.get("/productos")
def obtener_productos():
    lista = []
    for producto in productos.find():
        producto["_id"] = str(producto["_id"])
        lista.append(producto)
    return lista


@app.get("/productos/buscar/{nombre}")
def buscar_producto(nombre: str):
    lista = []
    for producto in productos.find({
        "Nombre": {
            "$regex": nombre,
            "$options": "i"} }):
        producto["_id"] = str(producto["_id"])
        lista.append(producto)
    return lista


@app.put("/productos/{id}")
def actualizar_producto(id: str, producto_actualizado: dict):
    productos.update_one(
        {"_id": ObjectId(id)},
        { "$set": {
                "Nombre": producto_actualizado["Nombre"],
                "Precio": producto_actualizado["Precio"],
                "Cantidad_Disponible": producto_actualizado["Cantidad_Disponible"],
                "Descripcion": producto_actualizado["Descripcion"] } } )
    return { "Mensaje": "Producto actualizado correctamente" }


@app.delete("/productos/{id}")
def eliminar_producto(id: str):
    productos.delete_one(
        {"_id": ObjectId(id)} )
    return { "Mensaje": "Producto eliminado correctamente" }


@app.post("/proveedores")
def agregar_proveedor(proveedor: dict):
    proveedores.insert_one(proveedor)
    return { "Mensaje": "Proveedor agregado correctamente" }


@app.get("/proveedores")
def obtener_proveedores():
    lista = []
    for proveedor in proveedores.find():
        proveedor["_id"] = str(proveedor["_id"])
        lista.append(proveedor)
    return lista


@app.get("/proveedores/buscar/{nombre}")
def buscar_proveedor(nombre: str):
    lista = []
    for proveedor in proveedores.find({
        "Nombre": {
            "$regex": nombre,
            "$options": "i" } }):
        proveedor["_id"] = str(proveedor["_id"])
        lista.append(proveedor)
    return lista


@app.put("/proveedores/{id}")
def actualizar_proveedor(id: str, proveedor_actualizado: dict):
    proveedores.update_one(
        {"_id": ObjectId(id)},
        { "$set": {
                "Nombre": proveedor_actualizado["Nombre"],
                "Telefono": proveedor_actualizado["Telefono"],
                "Correo": proveedor_actualizado["Correo"] } } )
    return { "Mensaje": "Proveedor actualizado correctamente" }


@app.delete("/proveedores/{id}")
def eliminar_proveedor(id: str):
    proveedores.delete_one(
        {"_id": ObjectId(id)} )
    return { "Mensaje": "Proveedor eliminado correctamente" }


@app.post("/usuarios")
def agregar_usuario(usuario: dict):
    usuarios.insert_one(usuario)
    return { "Mensaje": "Usuario agregado correctamente" }


@app.get("/usuarios")
def obtener_usuarios():
    lista = []
    for usuario in usuarios.find():
        usuario["_id"] = str(usuario["_id"])
        lista.append(usuario)
    return lista


@app.get("/usuarios/buscar/{nombre}")
def buscar_usuario(nombre: str):
    lista = []
    for usuario in usuarios.find({
        "Nombre": {
            "$regex": nombre,
            "$options": "i" } }):
        usuario["_id"] = str(usuario["_id"]) 
        lista.append(usuario)
    return lista


@app.put("/usuarios/{id}")
def actualizar_usuario(id: str, usuario_actualizado: dict):
    usuarios.update_one(
        {"_id": ObjectId(id)},
        { "$set": {
                "Nombre": usuario_actualizado["Nombre"],
                "Correo": usuario_actualizado["Correo"],
                "Telefono": usuario_actualizado["Telefono"],
                "Password": usuario_actualizado["Password"] } } )
    return { "Mensaje": "Usuario actualizado correctamente" }


@app.delete("/usuarios/{id}")
def eliminar_usuario(id: str):
    usuarios.delete_one(
        {"_id": ObjectId(id)} )
    return { "Mensaje": "Usuario eliminado correctamente" }


@app.post("/sucursales")
def agregar_sucursal(sucursal: dict):
    sucursales.insert_one(sucursal)
    return { "Mensaje": "Sucursal agregada correctamente" }


@app.get("/sucursales")
def obtener_sucursales(): 
    lista = []
    for sucursal in sucursales.find():
        sucursal["_id"] = str(sucursal["_id"])
        lista.append(sucursal)
    return lista


@app.get("/sucursales/buscar/{nombre}")
def buscar_sucursal(nombre: str):
    lista = []
    for sucursal in sucursales.find({
        "Nombre": {
            "$regex": nombre,
            "$options": "i" } }):
        sucursal["_id"] = str(sucursal["_id"])
        lista.append(sucursal)
    return lista


@app.put("/sucursales/{id}")
def actualizar_sucursal(id: str, sucursal_actualizada: dict):
    sucursales.update_one(
        {"_id": ObjectId(id)},
        { "$set": {
                "Nombre": sucursal_actualizada["Nombre"],
                "Direccion": sucursal_actualizada["Direccion"],
                "Telefono": sucursal_actualizada["Telefono"] } } )
    return { "Mensaje": "Sucursal actualizada correctamente" }


@app.delete("/sucursales/{id}")
def eliminar_sucursal(id: str):
    sucursales.delete_one(
        {"_id": ObjectId(id)} )
    return { "Mensaje": "Sucursal eliminada correctamente"}
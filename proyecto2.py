from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["control_administrativo"]

productos = db["productos"]
proveedores = db["proveedores"]
usuarios = db["usuarios"]
sucursales = db["sucursales"]


@app.get("/")
def inicio():
    return {"Mensaje": "API de control administrativo funcionando"}


# PRODUCTOS
@app.post("/productos")
def agregar_producto(producto: dict):
    productos.insert_one(producto)
    return {"Mensaje": "Producto agregado correctamente"}


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
    for producto in productos.find(
        {"Nombre": {"$regex": nombre, "$options": "i"}} ):
        producto["_id"] = str(producto["_id"])
        lista.append(producto)
    return lista


@app.put("/productos/{id_producto}")
def actualizar_producto(id_producto: str, producto_actualizado: dict):
    resultado = productos.update_one(
        {"_id": ObjectId(id_producto)},
        {"$set": producto_actualizado} )
    if resultado.matched_count == 0:
        return {"Mensaje": "Producto no encontrado"}
    return {"Mensaje": "Producto actualizado correctamente"}


@app.delete("/productos/{id_producto}")
def eliminar_producto(id_producto: str):
    resultado = productos.delete_one(
        {"_id": ObjectId(id_producto)} )
    if resultado.deleted_count == 0:
        return {"Mensaje": "Producto no encontrado"}
    return {"Mensaje": "Producto eliminado correctamente"}



# PROVEEDORES
@app.post("/proveedores")
def agregar_proveedor(proveedor: dict): 
    proveedores.insert_one(proveedor)
    return {"Mensaje": "Proveedor agregado correctamente"}


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
    for proveedor in proveedores.find(
            {"Nombre": {"$regex": nombre, "$options": "i"}}):
            proveedor["_id"] = str(proveedor["_id"])
            lista.append(proveedor)
    return lista


@app.put("/proveedores/{id_proveedor}")
def actualizar_proveedor(id_proveedor: str, proveedor_actualizado: dict):
    resultado = proveedores.update_one(
        {"_id": ObjectId(id_proveedor)},
        {"$set": proveedor_actualizado} )
    if resultado.matched_count == 0:
        return {"Mensaje": "Proveedor no encontrado"}
    return {"Mensaje": "Proveedor actualizado correctamente"}


@app.delete("/proveedores/{id_proveedor}")
def eliminar_proveedor(id_proveedor: str):
    resultado = proveedores.delete_one(
        {"_id": ObjectId(id_proveedor)} )
    if resultado.deleted_count == 0: 
        return {"Mensaje": "Proveedor no encontrado"}
    return {"Mensaje": "Proveedor eliminado correctamente"}


# USUARIOS
@app.post("/usuarios")
def agregar_usuario(usuario: dict):
    usuarios.insert_one(usuario)
    return {"Mensaje": "Usuario agregado correctamente"}


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
    for usuario in usuarios.find(
        {"Nombre": {"$regex": nombre, "$options": "i"}} ):
        usuario["_id"] = str(usuario["_id"])
        lista.append(usuario)
    return lista


@app.put("/usuarios/{id_usuario}")
def actualizar_usuario(id_usuario: str, usuario_actualizado: dict):
    resultado = usuarios.update_one(
        {"_id": ObjectId(id_usuario)},
        {"$set": usuario_actualizado} )
    if resultado.matched_count == 0:
        return {"Mensaje": "Usuario no encontrado"}
    return {"Mensaje": "Usuario actualizado correctamente"}


@app.delete("/usuarios/{id_usuario}")
def eliminar_usuario(id_usuario: str):
    resultado = usuarios.delete_one(
        {"_id": ObjectId(id_usuario)} )
    if resultado.deleted_count == 0:
        return {"Mensaje": "Usuario no encontrado"}
    return {"Mensaje": "Usuario eliminado correctamente"}


# SUCURSALES
@app.post("/sucursales")
def agregar_sucursal(sucursal: dict):
    sucursales.insert_one(sucursal)
    return {"Mensaje": "Sucursal agregada correctamente"}


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
    for sucursal in sucursales.find(
        {"Nombre": {"$regex": nombre, "$options": "i"}} ):
        sucursal["_id"] = str(sucursal["_id"])
        lista.append(sucursal)
    return lista


@app.put("/sucursales/{id_sucursal}")
def actualizar_sucursal(id_sucursal: str, sucursal_actualizada: dict):
    resultado = sucursales.update_one(
        {"_id": ObjectId(id_sucursal)},
        {"$set": sucursal_actualizada} )
    if resultado.matched_count == 0:
        return {"Mensaje": "Sucursal no encontrada"}
    return {"Mensaje": "Sucursal actualizada correctamente"}


@app.delete("/sucursales/{id_sucursal}")
def eliminar_sucursal(id_sucursal: str):
    resultado = sucursales.delete_one(
        {"_id": ObjectId(id_sucursal)} )
    if resultado.deleted_count == 0:
        return {"Mensaje": "Sucursal no encontrada"}
    return {"Mensaje": "Sucursal eliminada correctamente"}
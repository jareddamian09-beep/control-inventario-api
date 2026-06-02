from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
import uvicorn

app = FastAPI()

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["control_inventario"]

productos = db["productos"]
proveedores = db["proveedores"]
usuarios = db["usuarios"]
sucursales = db["sucursales"]

class Producto(BaseModel):
    Nombre: str
    Precio: float
    Cantidad_disponible: int
    Descripcion: str


class Usuario(BaseModel):
    Nombre: str
    Telefono: str
    Correo: str


class Sucursal(BaseModel):
    Nombre: str
    Direccion: str
    Telefono: str


class Proveedor(BaseModel):
    Nombre: str
    Telefono: str
    Correo: str


@app.get("/")
def inicio():
    return {"Mensaje": "API de control administrativo funcionando"}

@app.post("/productos")
def agregar_producto(producto: Producto):
    
    if producto.Nombre == "":
        raise HTTPException(
            status_code=400,
            detail="Ingrese de nuevo el nombre")

    if producto.Precio <= 0:
        raise HTTPException(
            status_code=400,
            detail="Ingrese de nuevo el precio"
        )

    if producto.Cantidad_disponible < 0:
        raise HTTPException(
            status_code=400,
            detail="Ingrese de nuevo la cantidad"
        )

    productos.insert_one(producto.dict())
    return {"Mensaje": "Producto agregado correctamente"}


@app.get("/productos")
def obtener_productos():
    lista = []
    for producto in productos.find():
        producto["_id"] = str(producto["_id"])
        lista.append(producto)

    if len(lista) == 0:
        raise HTTPException(
            status_code=404,
            detail="No hay productos")
    return lista


@app.put("/productos/{nombre}")
def actualizar_producto(nombre: str, producto_actualizado: Producto):

    resultado = productos.update_one(
        {"Nombre": nombre},
        {"$set": {
            "Nombre": producto_actualizado.Nombre,
            "Precio": producto_actualizado.Precio,
            "Cantidad_disponible": producto_actualizado.Cantidad_disponible,
            "Descripcion": producto_actualizado.Descripcion }} )

    if resultado.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado" )

    return {"Mensaje": "Producto actualizado correctamente"}


@app.delete("/productos/{nombre}")
def eliminar_producto(nombre: str):

    resultado = productos.delete_one(
        {"Nombre": nombre} )

    if resultado.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado" )

    return {"Mensaje": "Producto eliminado correctamente"}


@app.post("/proveedores")
def agregar_proveedor(proveedor: Proveedor):

    if proveedor.Nombre == "":
        raise HTTPException(
            status_code=400,
            detail="Esta mal el nombre" )

    proveedores.insert_one(proveedor.dict())
    return {"Mensaje": "Proveedor agregado correctamente"}


@app.get("/proveedores")
def obtener_proveedores():
    lista = []
    for proveedor in proveedores.find():
        proveedor["_id"] = str(proveedor["_id"])
        lista.append(proveedor)

    if len(lista) == 0:
        raise HTTPException(
            status_code=404,
            detail="No hay proveedores" )
    return lista


@app.put("/proveedores/{nombre}")
def actualizar_proveedor(nombre: str, proveedor_actualizado: Proveedor):

    resultado = proveedores.update_one(
        {"Nombre": nombre},
        {"$set": {
            "Nombre": proveedor_actualizado.Nombre,
            "Telefono": proveedor_actualizado.Telefono,
            "Correo": proveedor_actualizado.Correo }} )

    if resultado.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Proveedor no encontrado" )

    return {"Mensaje": "Proveedor actualizado correctamente"}


@app.delete("/proveedores/{nombre}")
def eliminar_proveedor(nombre: str):

    resultado = proveedores.delete_one(
        {"Nombre": nombre} )

    if resultado.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Proveedor no encontrado" )

    return {"Mensaje": "Proveedor eliminado correctamente"}



@app.post("/usuarios")
def agregar_usuarios(usuario: Usuario):

    if usuario.Nombre == "":
        raise HTTPException(
            status_code=400,
            detail="Esta mal el nombre" )

    usuarios.insert_one(usuario.dict())
    return {"Mensaje": "Usuario agregado correctamente"}


@app.get("/usuarios")
def obtener_usuarios():
    lista = []
    for usuario in usuarios.find():
        usuario["_id"] = str(usuario["_id"])
        lista.append(usuario)

    if len(lista) == 0:
        raise HTTPException(
            status_code=404,
            detail="No hay usuarios")

    return lista


@app.put("/usuarios/{nombre}")
def actualizar_usuarios(nombre: str, usuario_actualizado: Usuario):
    resultado = usuarios.update_one(
        {"Nombre": nombre},
        {"$set": {
            "Nombre": usuario_actualizado.Nombre,
            "Telefono": usuario_actualizado.Telefono,
            "Correo": usuario_actualizado.Correo }} )

    if resultado.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado" )

    return {"Mensaje": "Usuario actualizado correctamente"}


@app.delete("/usuarios/{nombre}")
def eliminar_usuarios(nombre: str):

    resultado = usuarios.delete_one(
        {"Nombre": nombre} )

    if resultado.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado" )

    return {"Mensaje": "Usuario eliminado correctamente"}



@app.post("/sucursales")
def agregar_sucursal(sucursal: Sucursal):

    if sucursal.Nombre == "":
        raise HTTPException(
            status_code=400,
            detail="Esta mal el nombre" )

    sucursales.insert_one(sucursal.dict())
    return {"Mensaje": "Sucursal agregada correctamente"}


@app.get("/sucursales")
def obtener_sucursales():
    lista = []
    for sucursal in sucursales.find():
        sucursal["_id"] = str(sucursal["_id"])
        lista.append(sucursal)

    if len(lista) == 0:
        raise HTTPException(
            status_code=404,
            detail="No hay sucursales" )
    return lista


@app.put("/sucursales/{nombre}")
def actualizar_sucursal(nombre: str, sucursal_actualizada: Sucursal):
    resultado = sucursales.update_one(
        {"Nombre": nombre},
        {"$set": {
            "Nombre": sucursal_actualizada.Nombre,
            "Direccion": sucursal_actualizada.Direccion,
            "Telefono": sucursal_actualizada.Telefono }} )

    if resultado.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Sucursal no encontrada" )

    return {"Mensaje": "Sucursal actualizada correctamente"}


@app.delete("/sucursales/{nombre}")
def eliminar_sucursal(nombre: str):
    resultado = sucursales.delete_one(
        {"Nombre": nombre} )

    if resultado.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Sucursal no encontrada" )

    return {"Mensaje": "Sucursal eliminada correctamente"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
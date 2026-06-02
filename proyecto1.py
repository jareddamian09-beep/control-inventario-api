from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId

# =====================================================
# CREAR API
# =====================================================

app = FastAPI()

# =====================================================
# CONEXION A MONGODB
# =====================================================

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["control_ventas"]

# =====================================================
# COLECCIONES
# =====================================================

productos = db["productos"]
proveedores = db["proveedores"]
clientes = db["clientes"]
sucursales = db["sucursales"]
ventas = db["ventas"]

# =====================================================
# RUTA PRINCIPAL
# =====================================================

@app.get("/")
def inicio():

    return {
        "Mensaje": "API de control de ventas funcionando correctamente"
    }

# =====================================================
# FUNCION PARA CONVERTIR OBJECTID A STRING
# =====================================================

def convertir_id(documento):

    documento["_id"] = str(documento["_id"])

    return documento

# =====================================================
# PRODUCTOS
# =====================================================

@app.post("/productos")
def agregar_producto(producto: dict):

    resultado = productos.insert_one(producto)

    return {

        "Mensaje": "Producto agregado correctamente",

        "ID_Generado": str(resultado.inserted_id)
    }


@app.get("/productos")
def obtener_productos():

    lista = []

    for producto in productos.find():

        lista.append(convertir_id(producto))

    return lista


@app.put("/productos/{id}")
def actualizar_producto(id: str, producto_actualizado: dict):

    try:

        id_producto = ObjectId(id)

    except InvalidId:

        return {"Error": "ID inválido"}

    producto_encontrado = productos.find_one(
        {
            "_id": id_producto
        }
    )

    if not producto_encontrado:

        return {"Error": "Producto no encontrado"}

    productos.update_one(

        {
            "_id": id_producto
        },

        {
            "$set": {

                "Nombre": producto_actualizado["Nombre"],
                "Precio": producto_actualizado["Precio"],
                "Cantidad": producto_actualizado["Cantidad"]

            }
        }
    )

    return {"Mensaje": "Producto actualizado correctamente"}


@app.delete("/productos/{id}")
def eliminar_producto(id: str):

    try:

        id_producto = ObjectId(id)

    except InvalidId:

        return {"Error": "ID inválido"}

    producto_encontrado = productos.find_one(
        {
            "_id": id_producto
        }
    )

    if not producto_encontrado:

        return {"Error": "Producto no encontrado"}

    productos.delete_one(
        {
            "_id": id_producto
        }
    )

    return {"Mensaje": "Producto eliminado correctamente"}

# =====================================================
# PROVEEDORES
# =====================================================

@app.post("/proveedores")
def agregar_proveedor(proveedor: dict):

    resultado = proveedores.insert_one(proveedor)

    return {

        "Mensaje": "Proveedor agregado correctamente",

        "ID_Generado": str(resultado.inserted_id)
    }


@app.get("/proveedores")
def obtener_proveedores():

    lista = []

    for proveedor in proveedores.find():

        lista.append(convertir_id(proveedor))

    return lista


@app.put("/proveedores/{id}")
def actualizar_proveedor(id: str, proveedor_actualizado: dict):

    try:

        id_proveedor = ObjectId(id)

    except InvalidId:

        return {"Error": "ID inválido"}

    proveedor_encontrado = proveedores.find_one(
        {
            "_id": id_proveedor
        }
    )

    if not proveedor_encontrado:

        return {"Error": "Proveedor no encontrado"}

    proveedores.update_one(

        {
            "_id": id_proveedor
        },

        {
            "$set": {

                "Nombre": proveedor_actualizado["Nombre"],
                "Telefono": proveedor_actualizado["Telefono"],
                "Correo": proveedor_actualizado["Correo"]

            }
        }
    )

    return {"Mensaje": "Proveedor actualizado correctamente"}


@app.delete("/proveedores/{id}")
def eliminar_proveedor(id: str):

    try:

        id_proveedor = ObjectId(id)

    except InvalidId:

        return {"Error": "ID inválido"}

    proveedor_encontrado = proveedores.find_one(
        {
            "_id": id_proveedor
        }
    )

    if not proveedor_encontrado:

        return {"Error": "Proveedor no encontrado"}

    proveedores.delete_one(
        {
            "_id": id_proveedor
        }
    )

    return {"Mensaje": "Proveedor eliminado correctamente"}

# =====================================================
# CLIENTES
# =====================================================

@app.post("/clientes")
def agregar_cliente(cliente: dict):

    resultado = clientes.insert_one(cliente)

    return {

        "Mensaje": "Cliente agregado correctamente",

        "ID_Generado": str(resultado.inserted_id)
    }


@app.get("/clientes")
def obtener_clientes():

    lista = []

    for cliente in clientes.find():

        lista.append(convertir_id(cliente))

    return lista


@app.put("/clientes/{id}")
def actualizar_cliente(id: str, cliente_actualizado: dict):

    try:

        id_cliente = ObjectId(id)

    except InvalidId:

        return {"Error": "ID inválido"}

    cliente_encontrado = clientes.find_one(
        {
            "_id": id_cliente
        }
    )

    if not cliente_encontrado:

        return {"Error": "Cliente no encontrado"}

    clientes.update_one(

        {
            "_id": id_cliente
        },

        {
            "$set": {

                "Nombre": cliente_actualizado["Nombre"],
                "Telefono": cliente_actualizado["Telefono"],
                "Correo": cliente_actualizado["Correo"],
                "Tipo_Usuario": cliente_actualizado["Tipo_Usuario"]

            }
        }
    )

    return {"Mensaje": "Cliente actualizado correctamente"}


@app.delete("/clientes/{id}")
def eliminar_cliente(id: str):

    try:

        id_cliente = ObjectId(id)

    except InvalidId:

        return {"Error": "ID inválido"}

    cliente_encontrado = clientes.find_one(
        {
            "_id": id_cliente
        }
    )

    if not cliente_encontrado:

        return {"Error": "Cliente no encontrado"}

    clientes.delete_one(
        {
            "_id": id_cliente
        }
    )

    return {"Mensaje": "Cliente eliminado correctamente"}

# =====================================================
# SUCURSALES
# =====================================================

@app.post("/sucursales")
def agregar_sucursal(sucursal: dict):

    resultado = sucursales.insert_one(sucursal)

    return {

        "Mensaje": "Sucursal agregada correctamente",

        "ID_Generado": str(resultado.inserted_id)
    }


@app.get("/sucursales")
def obtener_sucursales():

    lista = []

    for sucursal in sucursales.find():

        lista.append(convertir_id(sucursal))

    return lista


@app.put("/sucursales/{id}")
def actualizar_sucursal(id: str, sucursal_actualizada: dict):

    try:

        id_sucursal = ObjectId(id)

    except InvalidId:

        return {"Error": "ID inválido"}

    sucursal_encontrada = sucursales.find_one(
        {
            "_id": id_sucursal
        }
    )

    if not sucursal_encontrada:

        return {"Error": "Sucursal no encontrada"}

    sucursales.update_one(

        {
            "_id": id_sucursal
        },

        {
            "$set": {

                "Nombre": sucursal_actualizada["Nombre"],
                "Direccion": sucursal_actualizada["Direccion"],
                "Telefono": sucursal_actualizada["Telefono"]

            }
        }
    )

    return {"Mensaje": "Sucursal actualizada correctamente"}


@app.delete("/sucursales/{id}")
def eliminar_sucursal(id: str):

    try:

        id_sucursal = ObjectId(id)

    except InvalidId:

        return {"Error": "ID inválido"}

    sucursal_encontrada = sucursales.find_one(
        {
            "_id": id_sucursal
        }
    )

    if not sucursal_encontrada:

        return {"Error": "Sucursal no encontrada"}

    sucursales.delete_one(
        {
            "_id": id_sucursal
        }
    )

    return {"Mensaje": "Sucursal eliminada correctamente"}

# =====================================================
# VENTAS
# =====================================================

@app.post("/ventas")
def agregar_venta(venta: dict):

    try:

        cliente_id = ObjectId(venta["Cliente_id"])

        producto_id = ObjectId(venta["Producto_id"])

        sucursal_id = ObjectId(venta["Sucursal_id"])

    except InvalidId:

        return {"Error": "Uno o más IDs son inválidos"}

    # =================================================
    # VALIDAR CLIENTE
    # =================================================

    cliente_encontrado = clientes.find_one(
        {
            "_id": cliente_id
        }
    )

    if not cliente_encontrado:

        return {"Error": "Cliente no encontrado"}

    # =================================================
    # VALIDAR PRODUCTO
    # =================================================

    producto_encontrado = productos.find_one(
        {
            "_id": producto_id
        }
    )

    if not producto_encontrado:

        return {"Error": "Producto no encontrado"}

    # =================================================
    # VALIDAR SUCURSAL
    # =================================================

    sucursal_encontrada = sucursales.find_one(
        {
            "_id": sucursal_id
        }
    )

    if not sucursal_encontrada:

        return {"Error": "Sucursal no encontrada"}

    # =================================================
    # VALIDAR STOCK
    # =================================================

    if producto_encontrado["Cantidad"] < venta["Cantidad"]:

        return {"Error": "Stock insuficiente"}

    # =================================================
    # GUARDAR OBJECTID
    # =================================================

    venta["Cliente_id"] = cliente_id

    venta["Producto_id"] = producto_id

    venta["Sucursal_id"] = sucursal_id

    # =================================================
    # INSERTAR VENTA
    # =================================================

    resultado = ventas.insert_one(venta)

    # =================================================
    # DESCONTAR STOCK
    # =================================================

    productos.update_one(

        {
            "_id": producto_id
        },

        {
            "$inc": {

                "Cantidad": -venta["Cantidad"]

            }
        }
    )

    return {

        "Mensaje": "Venta realizada correctamente",

        "ID_Venta": str(resultado.inserted_id)
    }


@app.get("/ventas")
def obtener_ventas():

    lista = []

    for venta in ventas.find():

        venta["_id"] = str(venta["_id"])

        # =============================================
        # BUSCAR DATOS RELACIONADOS
        # =============================================

        cliente = clientes.find_one(
            {
                "_id": venta["Cliente_id"]
            }
        )

        producto = productos.find_one(
            {
                "_id": venta["Producto_id"]
            }
        )

        sucursal = sucursales.find_one(
            {
                "_id": venta["Sucursal_id"]
            }
        )

        # =============================================
        # CONVERTIR IDS A STRING
        # =============================================

        venta["Cliente_id"] = str(venta["Cliente_id"])

        venta["Producto_id"] = str(venta["Producto_id"])

        venta["Sucursal_id"] = str(venta["Sucursal_id"])

        # =============================================
        # MOSTRAR INFORMACION
        # =============================================

        venta["Cliente"] = cliente["Nombre"]

        venta["Producto"] = producto["Nombre"]

        venta["Sucursal"] = sucursal["Nombre"]

        lista.append(venta)

    return lista


@app.put("/ventas/{id}")
def actualizar_estado_venta(id: str, venta_actualizada: dict):

    try:

        id_venta = ObjectId(id)

    except InvalidId:

        return {"Error": "ID inválido"}

    venta_encontrada = ventas.find_one(
        {
            "_id": id_venta
        }
    )

    if not venta_encontrada:

        return {"Error": "Venta no encontrada"}

    ventas.update_one(

        {
            "_id": id_venta
        },

        {
            "$set": {

                "Estado": venta_actualizada["Estado"]

            }
        }
    )

    return {"Mensaje": "Estado actualizado correctamente"}


@app.delete("/ventas/{id}")
def eliminar_venta(id: str):

    try:

        id_venta = ObjectId(id)

    except InvalidId:

        return {"Error": "ID inválido"}

    venta_encontrada = ventas.find_one(
        {
            "_id": id_venta
        }
    )

    if not venta_encontrada:

        return {"Error": "Venta no encontrada"}

    # =================================================
    # RECUPERAR STOCK
    # =================================================

    productos.update_one(

        {
            "_id": venta_encontrada["Producto_id"]
        },

        {
            "$inc": {

                "Cantidad": venta_encontrada["Cantidad"]

            }
        }
    )

    # =================================================
    # ELIMINAR VENTA
    # =================================================

    ventas.delete_one(
        {
            "_id": id_venta
        }
    )

    return {"Mensaje": "Venta eliminada correctamente"}
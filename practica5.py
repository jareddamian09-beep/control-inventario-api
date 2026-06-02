from pymongo import MongoClient
cliente = MongoClient("mongodb://localhost:27017/")    #Se conecta al servidor de MongoDB
db = cliente["Tienda2"]        #Usa o crea una base de datos
coleccion = db["Clientes1"]    #Usa o crea una coleccion  

#Insertar todos los clientes
'''empleados = [
{ "Nombre": "Ana", "Edad": 25, "Ciudad": "Guadalajara", 
"Compras": [{ "Producto": "Laptop", "Precio": 15000 }, { "Producto": "Mouse", "Precio": 300 }] },
{ "Nombre": "Luis", "Edad": 30,"Ciudad": "Zapopan", 
"Compras": [{ "Producto": "Teclado", "Precio": 800 }]},
{ "Nombre" : "Carlos", "Edad": 22, "Ciudad": "Guadalajara",
"Compras": [{ "Producto": "Monitor", "Precio": 4000 }, { "Producto": "Mouse", "Precio": 250 }]}
]

resultado = coleccion.insert_many(empleados)
print("ID de los insertados:", resultado.inserted_ids)'''

#Clientes con edad mayor a 23 ($gt)
'''for doc in coleccion.find({"Edad": {"$gt": 23}}):
    print(doc)'''

#Clientes con edad menor a 30 ($lt)
'''for doc in coleccion.find({"Edad": {"$lt": 30}}):
    print(doc)'''

#Clientes que vivan en Guadalajara o Zapopan ($in)
'''ambos_lugares = ({"Ciudad": {"$in": ["Guadalajara", "Zapopan"]}})

resultados = coleccion.find(ambos_lugares)
for doc in resultados:
    print(doc)'''

#Clientes mayores de 20 Y de Guadalajara ($and)    
'''tapatios_mayores = ( {"$and": [ {"Edad": {"$gt": 20}}, {"Ciudad": "Guadalajara"} ] } ) 

resultados = coleccion.find(tapatios_mayores)
for doc in resultados:
    print(doc)'''

#Clientes de Guadalajara O menores de 25 ($or)
'''tapatios_menores = ( {"$or": [ {"Ciudad": "Guadalajara"}, {"Edad": {"$lt": 25}} ] } )

resultados = coleccion.find(tapatios_menores)
for doc in resultados:
    print(doc)'''

#Mostrar solo nombre y ciudad
'''for doc in coleccion.find({}, {"Nombre": 1, "Ciudad": 1, "_id": 0}):
    print(doc)'''

#Mostrar nombre sin _id
'''for doc in coleccion.find({}, {"Nombre": 1, "_id": 0}):
    print(doc)'''

#Ordenar por edad ascendente
'''edad_ascendente = coleccion.find().sort({"Edad": 1})

for doc in edad_ascendente:
    print(doc)'''

#Mostrar nombre y edad descendente
'''nombre_edad_descendente = coleccion.find({}, {"Nombre": 1, "Edad": 1, "_id": 0}).sort({"Edad": -1})

for doc in nombre_edad_descendente:
    print(doc)'''

'''Realiza las siguientes operaciones usando las agregaciones en un único pipeline:
1. Contar clientes por ciudad ($sum: 1)
2. Calcular el promedio de edad ($avg)
3. Calcular el total de ventas
4. Calcular el total gastado por cliente'''

pipeline = [{ "$facet": {"Clientes_por_ciudad": [ {"$group": {"_id": "$Ciudad", "Clientes": {"$sum": 1}}} ], 
                         "Promedio_de_edad": [ {"$group": {"_id": None, "Promedio": {"$avg": "$Edad"}}} ], 
                         "Total_ventas": [ {"$unwind": "$Compras"}, {"$group": {"_id": None, "Total": {"$sum": "$Compras.Precio"}}} ], 
                         "Total_por_cliente": [ {"$unwind": "$Compras"}, {"$group": {"_id": "$Nombre", "Total": {"$sum": "$Compras.Precio"}}} ] } } ]

for doc in coleccion.aggregate(pipeline):
    print(doc)
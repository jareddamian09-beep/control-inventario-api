'''pipeline = [ { "$match": { "Edad": {"$gt": 25} }}]

resultados = coleccion.aggregate(pipeline)
for doc in resultados:
    print(doc)'''

'''pipeline = [{"$group": {"_id": "$Ciudad", "total_clientes": {"$sum": 1}}}]

resultados = coleccion.aggregate(pipeline)

for doc in resultados:
    print(doc)'''

'''pipeline = [{ "$group": {"_id": "$Ciudad", "total_clientes": {"$sum": 1}, "total_edad": {"$sum": "$Edad"} }}]
resultados = coleccion.aggregate(pipeline)

for doc in resultados:
    print(doc)'''

'''pipeline = [{ "$group": {"_id": "$Ciudad", "total_clientes": {"$sum": 1}, "total_edad": {"$avg": "$Edad"} }}]
resultados = coleccion.aggregate(pipeline)

for doc in resultados:
    print(doc)'''

'''pipeline = [{"$group": {"_id": "$Ciudad","total_clientes": {"$sum": 1}}}, { "$sort": {"total_clientes": -1}}]
resultados = coleccion.aggregate(pipeline)

for doc in resultados:
    print(doc)'''

'''pipeline = [{"$unwind": "$Compras"}, {"$group": {"_id": "$Nombre", "total_gastado": {"$sum": "$Compras.Precio"}}}]
resultados = coleccion.aggregate(pipeline)

for doc in resultados:
    print(doc)'''

#Clientes por ciudad
'''pipeline = [{"$group": {"_id": "$Ciudad", "clientes": {"$sum": 1}}}]
 
for doc in coleccion.aggregate(pipeline):
    print(doc)'''

#Promedio de edad
'''pipeline = [{"$group": {"_id": None, "promedio": {"$avg": "$Edad"}}}]

for doc in coleccion.aggregate(pipeline):
    print(doc)'''

#Calcular el total de ventas
'''pipeline = [{"$unwind": "$Compras"}, {"$group": {"_id": None, "total": {"$sum": "$Compras.Precio"}}}]

for doc in coleccion.aggregate(pipeline):
    print(doc)'''

#Calcular el total gastado por cliente
'''pipeline = [{"$unwind": "$Compras"}, {"$group": {"_id": "$Nombre", "total_por_cliente": {"$sum": "$Compras.Precio"}}}]

for doc in coleccion.aggregate(pipeline):
    print(doc)'''

#Pipeline completo
'''pipeline =  [ { "$facet": { 
              "Clientes": [ {"$group" : {"_id": "$Ciudad", "Clientes": {"$sum": 1}}}],
              "Promedio": [ {"$group": {"_id": None, "promedio": {"$avg": "$Edad"}}}],
              "total": [ {"$unwind": "$Compras"}, {"$group": {"_id": None, "total": {"$sum": "$Compras.Precio"}}}],
              "total_cliente": [ {"$unwind": "$Compras"}, {"$group": {"_id": "$Nombre", "total_por_cliente": {"$sum": "$Compras.Precio"}}}] 
            } ]

for doc in coleccion.aggregate(pipeline):
    print(doc)'''

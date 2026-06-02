#Paso 1
from pymongo import MongoClient     #Importa la libreria para conectarnos a Python con MongoDB
cliente = MongoClient("mongodb://localhost:27017/")    #Se conecta al servidor de MongoDB
db = cliente["empresa"]        #Usa o crea una base de datos llamada empresa
coleccion = db["empleados"]    #Usa o crea una coleccion llamada empleados. 

#SCRIPT 1
'''Insertar un registro en la base de datos (Diccionario que se guarda como un documento JSON) 
empleado = {
"nombre": "Ana",
"edad": 25,
"puesto": "Desarrollador",
"salario": 15000
}

resultado = coleccion.insert_one(empleado)      #Inserta un documento en la coleccion empleados 
print("ID insertado:", resultado.inserted_id)   #Mostrar el id del documento que se inserto.''' 

#SCRIPT 2
#Insertar varios registros en la base de datos. 
'''empleados = [
{"nombre": "Luis", "edad": 30, "puesto": "Tester","salario": 12000},
{"nombre": "Carlos", "edad": 28, "puesto": "Soporte","salario": 10000}
]
coleccion.insert_many(empleados)   #Inserta los documentos en la coleccion empleados'''

#SCRIPT 3
#Consultar
'''for doc in coleccion.find(): #Busca los registros sin parámetros, recorre uno por uno. 
    print(doc) #Imprime cada documento en la terminal.'''

#SCRIPT 4
#Consultar
'''for doc in coleccion.find({"edad": {"$gt": 26}}):  #Busca los registros en la colección, pero aquellos que cumplan con la condición.
    print(doc)  #Imprime los registros que tengan de edad mayor a 26.''' 

#SCRIPT 5
#Consultar
'''doc = coleccion.find_one({"nombre": "Ana"})  #Busca un solo documento (el primero que encuentra) con la condicion de que la clave nombre sea igual a Ana.
print(doc)   #Imprime el documento en la terminal.'''

#SCRIPT 6
#Consultar-Proyeccion
'''for doc in coleccion.find({}, {"nombre": 1, "salario": 1, "_id": 0}):  #Busca los documentos y pide que muestre los campos nombre y salario de cada uno excluyendo el id.
    print(doc) #Imprime todos los documentos, pero solo con nombre y salario.'''

#SCRIPT 7
#Actualizar
#coleccion.update_one( {"nombre": "Ana"}, {"$set": {"salario": 18000}} )  #Actualiza solo un documento en la colección, aquel que el campo "nombre" coincide con el valor "Ana" y actualiza su salario.   

#SCRIPT 8
#Actualizar
#coleccion.update_many( {"puesto": "Tester"}, {"$set": {"salario": 13000}} ) #Actualiza varios documentos en la coleccion, todos los que tengan el valor "TESTER" actualiza el campo salario a 13000

#SCRIPT 9
#Actualizar
#coleccion.update_one( {"nombre": "Luis"}, {"$inc": {"salario": 1000}} )  #Actualiza un documento que coincida con el valor Luis y al salario incrementarle 1000.

#SCRIPT 10
#Actualizar
'''resultado = coleccion.update_many( {"edad": {"$gt": 25}}, {"$set": {"activo": True}} )  # Actualiza varios documentos, aquellos que su edad sea mayor a 25 les agrega o cambia si ya existe el campo "activo"
print("Modificados:", resultado.modified_count)  #Imprime el total de los documentos que fueron actualizados o modificados '''

#SCRIPT 11
#Borrar
#coleccion.delete_one({"nombre": "Carlos"})  #Elimina el registro que corresponda al valor

#SCRIPT 12
#Borrar
#coleccion.delete_many({"edad": {"$lt": 28}}) #Elimina varios documentos que cumplan con la condicion de que la edad sea menoor a 28.

#SCRIPT 13
#Borrar
'''resultado = coleccion.delete_many({"puesto": "Soporte"})  #Borra aquellos documentos que en la clave "puesto" tenga el valor "Soporte"
print("Eliminados:", resultado.deleted_count)  #Imprime el total de los documentos que fueron eliminados '''

#SCRIPT 14
#Pipeline
'''pipeline = [{ "$group": { "_id": None, "total": {"$sum": "$salario"} } } ] #Se agrupan por ningun campo y calcula el total de los valores que aparecen en el campo salario.
for doc in coleccion.aggregate(pipeline):     #Hace que funcione el pipeline.
    print(doc)    #Imprime el resultado del pipeline. '''

#SCRIPT 15
#Pipeline
'''pipeline = [{ "$group": { "_id": None, "promedio": {"$avg": "$salario"} } } ]  #Se agrupa por ningun campo y calcule el promedio de los valores que aparecen en el campo salario
for doc in coleccion.aggregate(pipeline):    #Hace que funcione el pipeline
    print(doc)    #Imprime el resultado del pipeline. '''
from flask_restful import Resource, request
from flask import jsonify
from utils.cursor import Cursor
from datetime import datetime 

class EstructuraFisica(Resource):

    

    def get(self, id):
                
        estructura = None
        
        query = "\
                SELECT\
                        EF.ID,\
                        EF.NOMBRE,\
                        EF.DIRECCION,\
                        EF.CIUDAD,\
                        EF.FECHA_CREACION,\
                        EF.FECHA_ACTUALIZACION,\
                        DP.ID,\
                        DP.DESCRIPCION\
                FROM\
                    TP_ESTRUCTURAS_FISICAS AS EF\
                INNER JOIN\
                    TR_DEPARTAMENTOS AS DP\
                ON DP.ID = EF.ID_DEPARTAMENTO\
                WHERE\
                    EF.ID = %s\
        "
                
        with Cursor() as connection:
            try:
                
                connection.execute(query, (id,))
                estructura = connection.fetchone()
                
                if estructura != None:
                    
                    return {
                        "success": True,
                        "data": {
                            "id" : estructura[0],
                            "nombre": estructura[1],
                            "direccion": estructura[2],
                            "ciudad": estructura[3],
                            "fecha_creacion": str(estructura[4]),
                            "fecha_actualizacion": str(estructura[5]),
                            "id_departamento": estructura[6],
                            "nombre_departamento": estructura[7]
                        }
                    }
                else:
                    return {
                        "success" : False
                    }       
            
            except Exception as ex:
                return {
                    "success" : False,
                    "error": str(ex)
                }
    
    def post(self):
        
        estructura = None
        query = "INSERT INTO TP_ESTRUCTURAS_FISICAS (NOMBRE, DIRECCION, CIUDAD, ID_DEPARTAMENTO ) VALUES(%s, %s, %s, %s)"
        
        with Cursor() as connection:
            try:                
                connection.execute(query, 
                (
                    request.json["nombre"],
                    request.json["direccion"],
                    request.json["ciudad"],
                    request.json["id_departamento"]                    
                ))
                
                query = "\
                        SELECT\
                                EF.ID,\
                                EF.NOMBRE,\
                                EF.DIRECCION,\
                                EF.CIUDAD,\
                                EF.FECHA_CREACION,\
                                EF.FECHA_ACTUALIZACION,\
                                DP.ID,\
                                DP.DESCRIPCION\
                        FROM\
                            TP_ESTRUCTURAS_FISICAS AS EF\
                        INNER JOIN\
                            TR_DEPARTAMENTOS AS DP\
                        ON DP.ID = EF.ID_DEPARTAMENTO\
                        WHERE\
                            EF.ID = (SELECT MAX(ID) FROM (TP_ESTRUCTURAS_FISICAS))\
                "
                
                connection.execute(query)
                estructura = connection.fetchone()
                
                if estructura != None:
                    
                    return {
                        "success": True,
                        "data": {
                            "id" : estructura[0],
                            "nombre": estructura[1],
                            "direccion": estructura[2],
                            "ciudad": estructura[3],
                            "fecha_creacion": str(estructura[4]),
                            "fecha_actualizacion": str(estructura[5]),
                            "id_departamento": estructura[6],
                            "nombre_departamento": estructura[7]
                        }
                    }
                else:
                    return {
                        "success" : False
                    }       
            
            except Exception as ex:
                return {
                    "success" : False,
                    "error": str(ex)
                }
    
    def delete(self, id):
                
        estructura = None
        
        query = "\
                SELECT\
                        EF.ID,\
                        EF.NOMBRE,\
                        EF.DIRECCION,\
                        EF.CIUDAD,\
                        EF.FECHA_CREACION,\
                        EF.FECHA_ACTUALIZACION,\
                        DP.ID,\
                        DP.DESCRIPCION\
                FROM\
                    TP_ESTRUCTURAS_FISICAS AS EF\
                INNER JOIN\
                    TR_DEPARTAMENTOS AS DP\
                ON DP.ID = EF.ID_DEPARTAMENTO\
                WHERE\
                    EF.ID = %s\
        "
        
        
        with Cursor() as connection:
            try:
                connection.execute(query, (id,))
                estructura = connection.fetchone()
                
                query = "DELETE FROM TP_ESTRUCTURAS_FISICAS WHERE ID = %s"
                
                connection.execute(query, (id,))
                
                if estructura != None:
                    
                    return {
                        "success": True,
                        "data": {
                            "id" : estructura[0],
                            "nombre": estructura[1],
                            "direccion": estructura[2],
                            "ciudad": estructura[3],
                            "fecha_creacion": str(estructura[4]),
                            "fecha_actualizacion": str(estructura[5]),
                            "id_departamento": estructura[6],
                            "nombre_departamento": estructura[7]
                        }
                    }
                else:
                    return {
                        "success" : False
                    }                
            except Exception as ex:
                return {
                    "success" : False,
                    "error" : str(ex)
                }
        
    def put(self, id):
        
        estructura = None
        
        query = "\
                SELECT\
                        ID,\
                        NOMBRE,\
                        DIRECCION,\
                        CIUDAD,\
                        FECHA_CREACION,\
                        FECHA_ACTUALIZACION,\
                        ID_DEPARTAMENTO\
                FROM\
                    TP_ESTRUCTURAS_FISICAS\
                WHERE\
                    ID = %s\
        "
        
        with Cursor() as connection:
            try:
                connection.execute(query, (id,))
                dataEstructura = connection.fetchone()
                
                if dataEstructura != None:
                    estructura = {
                            "id" : dataEstructura[0],
                            "nombre": dataEstructura[1],
                            "direccion": dataEstructura[2],
                            "ciudad": dataEstructura[3],
                            "fecha_creacion": str(dataEstructura[4]),
                            "fecha_actualizacion": str(dataEstructura[5]),
                            "id_departamento": dataEstructura[6],
                    }
                    
                    nombre = None
                    direccion = None
                    ciudad = None
                    id_departamento = None
                    
                    if "nombre" in request.json and estructura["nombre"] != request.json["nombre"]:
                        nombre = request.json["nombre"]
                    else:
                        nombre = estructura["nombre"]
                        
                    if "direccion" in request.json and estructura["direccion"] != request.json["direccion"]:
                        direccion = request.json["direccion"]
                    else:
                        direccion = estructura["direccion"]
                        
                    if "ciudad" in request.json and estructura["ciudad"] != request.json["ciudad"]:
                        ciudad = request.json["ciudad"]
                    else:
                        ciudad = estructura["ciudad"]
                        
                    if "id_departamento" in request.json and estructura["id_departamento"] != request.json["id_departamento"]:
                        id_departamento = request.json["id_departamento"]
                    else:
                        id_departamento = estructura["id_departamento"]
                        
                    query = "\
                        UPDATE\
                            TP_ESTRUCTURAS_FISICAS\
                        SET\
                            NOMBRE = %s,\
                            DIRECCION = %s,\
                            CIUDAD = %s,\
                            ID_DEPARTAMENTO = %s,\
                            FECHA_ACTUALIZACION = NOW()\
                        WHERE ID = %s\
                    "
                    
                    connection.execute(query, 
                    (
                        nombre,
                        direccion,
                        ciudad,
                        id_departamento,
                        id
                    ))
                    
                    
                    query = "\
                            SELECT\
                                    EF.ID,\
                                    EF.NOMBRE,\
                                    EF.DIRECCION,\
                                    EF.CIUDAD,\
                                    EF.FECHA_CREACION,\
                                    EF.FECHA_ACTUALIZACION,\
                                    DP.ID,\
                                    DP.DESCRIPCION\
                            FROM\
                                TP_ESTRUCTURAS_FISICAS AS EF\
                            INNER JOIN\
                                TR_DEPARTAMENTOS AS DP\
                            ON DP.ID = EF.ID_DEPARTAMENTO\
                            WHERE\
                                EF.ID = %s\
                    "
                    
                    connection.execute(query, (id,))
                    estructura = connection.fetchone()
                    
                    if estructura != None:
                        
                        return {
                            "success": True,
                            "data": {
                            "id" : estructura[0],
                            "nombre": estructura[1],
                            "direccion": estructura[2],
                            "ciudad": estructura[3],
                            "fecha_creacion": str(estructura[4]),
                            "fecha_actualizacion": str(estructura[5]),
                            "id_departamento": estructura[6],
                            "nombre_departamento": estructura[7]
                        }
                        }
                        
                else:
                    return {
                        "success" : False
                    }
                
            except Exception as ex:
                return {
                    "success" : False,
                    "error" : str(ex)
                }
        
    
class EstructurasFisicas(Resource):
    
    def get(self):
        estructuras = []
        
        query = "\
                SELECT\
                        EF.ID,\
                        EF.NOMBRE,\
                        EF.DIRECCION,\
                        EF.CIUDAD,\
                        EF.FECHA_CREACION,\
                        EF.FECHA_ACTUALIZACION,\
                        DP.ID,\
                        DP.DESCRIPCION\
                FROM\
                    TP_ESTRUCTURAS_FISICAS AS EF\
                INNER JOIN\
                    TR_DEPARTAMENTOS AS DP\
                ON DP.ID = EF.ID_DEPARTAMENTO\
        "
                
        with Cursor() as connection:
            try:
                
                connection.execute(query)
                dataEstructuras = connection.fetchall()
                
                if dataEstructuras != None:
                    
                    for estructura in dataEstructuras:
                        estructuras.append(
                            {
                            "id" : estructura[0],
                            "nombre": estructura[1],
                            "direccion": estructura[2],
                            "ciudad": estructura[3],
                            "fecha_creacion": str(estructura[4]),
                            "fecha_actualizacion": str(estructura[5]),
                            "id_departamento": estructura[6],
                            "nombre_departamento": estructura[7]
                            }
                        )
                    
                    return {
                        "success": True,
                        "registros": len(estructuras),
                        "data": estructuras
                    }
                else:
                    return {
                        "success" : False
                    }       
            
            except Exception as ex:
                return {
                    "success" : False,
                    "error": str(ex)
                }
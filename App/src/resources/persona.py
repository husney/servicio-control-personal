from flask_restful import Resource, request
from flask import jsonify
from utils.cursor import Cursor
from datetime import datetime 

class Persona(Resource):

    

    def get(self, id):
                
        persona = None
        
        query = "\
                        SELECT\
                                P.ID,\
                                I.CODIGO,\
                                I.NOMBRE,\
                                P.NUMERO_IDENTIFICACION,\
                                P.PRIMER_NOMBRE,\
                                P.SEGUNDO_NOMBRE,\
                                P.PRIMER_APELLIDO,\
                                P.SEGUNDO_APELLIDO,\
                                P.EDAD,\
                                P.FECHA_NACIMIENTO,\
                                P.FECHA_CREACION,\
                                P.FECHA_ACTUALIZACION\
                        FROM\
                            TM_PERSONAS AS P\
                        INNER JOIN\
                            TR_TIPOS_IDENTIFICACION AS I\
                        ON I.ID = P.ID_TIPO_IDENTIFICACION\
                        WHERE\
                            P.ID = %s\
                "
                
        with Cursor() as connection:
            try:
                
                connection.execute(query, (id,))
                persona = connection.fetchone()
                
                if persona != None:
                    
                    return {
                        "success": True,
                        "data": {
                            "id" : persona[0],
                            "codigo_tipo_identificacion": persona[1],
                            "nombre_tipo_identificacion": persona[2],
                            "numero_identificacion": persona[3],
                            "primer_nombre": persona[4],
                            "segundo_nombre": persona[5],
                            "primer_apellido": persona[6],
                            "segundo_apellido": persona[7],
                            "edad": persona[8],
                            "fecha_nacimiento": str(persona[9]),
                            "fecha_creacion": str(persona[10]),
                            "fecha_actualizacion": str(persona[11])
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
        
        persona = None
        query = "INSERT INTO TM_PERSONAS (NUMERO_IDENTIFICACION, PRIMER_NOMBRE, SEGUNDO_NOMBRE, PRIMER_APELLIDO, SEGUNDO_APELLIDO, FECHA_NACIMIENTO, EDAD, ID_TIPO_IDENTIFICACION ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        
        with Cursor() as connection:
            try:                
                connection.execute(query, 
                (
                    request.json["numero_identificacion"],
                    request.json["primer_nombre"],
                    request.json["segundo_nombre"],
                    request.json["primer_apellido"],
                    request.json["segundo_apellido"],
                    request.json["fecha_nacimiento"],
                    request.json["edad"],
                    request.json["id_tipo_identificacion"]
                ))
                
                query = "\
                        SELECT\
                                P.ID,\
                                I.CODIGO,\
                                I.NOMBRE,\
                                P.NUMERO_IDENTIFICACION,\
                                P.PRIMER_NOMBRE,\
                                P.SEGUNDO_NOMBRE,\
                                P.PRIMER_APELLIDO,\
                                P.SEGUNDO_APELLIDO,\
                                P.EDAD,\
                                P.FECHA_NACIMIENTO,\
                                P.FECHA_CREACION,\
                                P.FECHA_ACTUALIZACION\
                        FROM\
                            TM_PERSONAS AS P\
                        INNER JOIN\
                            TR_TIPOS_IDENTIFICACION AS I\
                        ON I.ID = P.ID_TIPO_IDENTIFICACION\
                        WHERE\
                            P.ID = (SELECT MAX(ID) FROM (TM_PERSONAS))\
                "
                
                connection.execute(query)
                persona = connection.fetchone()
                
                if persona != None:
                    
                    return {
                        "success": True,
                        "data": {
                            "id" : persona[0],
                            "codigo_tipo_identificacion": persona[1],
                            "nombre_tipo_identificacion": persona[2],
                            "numero_identificacion": persona[3],
                            "primer_nombre": persona[4],
                            "segundo_nombre": persona[5],
                            "primer_apellido": persona[6],
                            "segundo_apellido": persona[7],
                            "edad": persona[8],
                            "fecha_nacimiento": str(persona[9]),
                            "fecha_creacion": str(persona[10]),
                            "fecha_actualizacion": str(persona[11])
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
                
        persona = None
        
        query = "\
                    SELECT\
                            P.ID,\
                            I.CODIGO,\
                            I.NOMBRE,\
                            P.NUMERO_IDENTIFICACION,\
                            P.PRIMER_NOMBRE,\
                            P.SEGUNDO_NOMBRE,\
                            P.PRIMER_APELLIDO,\
                            P.SEGUNDO_APELLIDO,\
                            P.EDAD,\
                            P.FECHA_NACIMIENTO,\
                            P.FECHA_CREACION,\
                            P.FECHA_ACTUALIZACION\
                    FROM\
                        TM_PERSONAS AS P\
                    INNER JOIN\
                        TR_TIPOS_IDENTIFICACION AS I\
                    ON I.ID = P.ID_TIPO_IDENTIFICACION\
                    WHERE\
                        P.ID = (%s)\
                "
        
        
        with Cursor() as connection:
            try:
                connection.execute(query, (id,))
                persona = connection.fetchone()
                
                query = "DELETE FROM TM_PERSONAS WHERE ID = %s"
                
                connection.execute(query, (id,))
                
                if persona != None:
                    
                    return {
                        "success": True,
                        "data": {
                            "id" : persona[0],
                            "codigo_tipo_identificacion": persona[1],
                            "nombre_tipo_identificacion": persona[2],
                            "numero_identificacion": persona[3],
                            "primer_nombre": persona[4],
                            "segundo_nombre": persona[5],
                            "primer_apellido": persona[6],
                            "segundo_apellido": persona[7],
                            "edad": persona[8],
                            "fecha_nacimiento": str(persona[9]),
                            "fecha_creacion": str(persona[10]),
                            "fecha_actualizacion": str(persona[11])
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
        
        persona = None
        
        query = "\
                    SELECT\
                            ID,\
                            ID_TIPO_IDENTIFICACION,\
                            NUMERO_IDENTIFICACION,\
                            PRIMER_NOMBRE,\
                            SEGUNDO_NOMBRE,\
                            PRIMER_APELLIDO,\
                            SEGUNDO_APELLIDO,\
                            EDAD,\
                            FECHA_NACIMIENTO\
                    FROM\
                        TM_PERSONAS\
                    WHERE\
                        ID = %s\
                "
        
        with Cursor() as connection:
            try:
                connection.execute(query, (int(id),))
                dataPersona = connection.fetchone()
                
                if dataPersona != None:
                    persona = {
                            "id" : dataPersona[0],
                            "tipo_identificacion": dataPersona[1],                            
                            "numero_identificacion": dataPersona[2],
                            "primer_nombre": dataPersona[3],
                            "segundo_nombre": dataPersona[4],
                            "primer_apellido": dataPersona[5],
                            "segundo_apellido": dataPersona[6],
                            "edad": dataPersona[7],
                            "fecha_nacimiento": str(dataPersona[8]),
                    }
                    
                    tipo_identificacion = None
                    numero_identificacion = None
                    primer_nombre = None
                    segundo_nombre = None
                    primer_apellido = None
                    edad = None
                    fecha_nacimiento = None
                    
                    if "tipo_identificacion" in request.json and persona["tipo_identificacion"] != request.json["tipo_identificacion"]:
                        tipo_identificacion = request.json["tipo_identificacion"]
                    else:
                        tipo_identificacion = persona["tipo_identificacion"]
                        
                    if "numero_identificacion" in request.json and persona["numero_identificacion"] != request.json["numero_identificacion"]:
                        numero_identificacion = request.json["numero_identificacion"]
                    else:
                        numero_identificacion = persona["numero_identificacion"]
                        
                    if "primer_nombre" in request.json and persona["primer_nombre"] != request.json["primer_nombre"]:
                        primer_nombre = request.json["primer_nombre"]
                    else:
                        primer_nombre = persona["primer_nombre"]
                        
                    if "segundo_nombre" in request.json and persona["segundo_nombre"] != request.json["segundo_nombre"]:
                        segundo_nombre = request.json["segundo_nombre"]
                    else:
                        segundo_nombre = persona["segundo_nombre"]
                        
                    if "primer_apellido" in request.json and persona["primer_apellido"] != request.json["primer_apellido"]:
                        primer_apellido = request.json["primer_apellido"]
                    else:
                        primer_apellido = persona["primer_apellido"]
                        
                    if "segundo_apellido" in request.json and persona["segundo_apellido"] != request.json["segundo_apellido"]:
                        segundo_apellido = request.json["segundo_apellido"]
                    else:
                        segundo_apellido = persona["segundo_apellido"]
                        
                    if "edad" in request.json and persona["edad"] != request.json["edad"]:
                        edad = request.json["edad"]
                    else:
                        edad = persona["edad"]
                        
                    if "fecha_nacimiento" in request.json and persona["fecha_nacimiento"] != request.json["fecha_nacimiento"]:
                        fecha_nacimiento = request.json["fecha_nacimiento"]
                    else:
                        fecha_nacimiento = persona["fecha_nacimiento"]
                        
                    query = "\
                        UPDATE\
                            TM_PERSONAS\
                        SET\
                            ID_TIPO_IDENTIFICACION = %s,\
                            NUMERO_IDENTIFICACION = %s,\
                            PRIMER_NOMBRE = %s,\
                            SEGUNDO_NOMBRE = %s,\
                            PRIMER_APELLIDO = %s,\
                            SEGUNDO_APELLIDO = %s,\
                            EDAD = %s,\
                            FECHA_NACIMIENTO = %s,\
                            FECHA_ACTUALIZACION = NOW()\
                        WHERE ID = %s\
                    "
                    
                    connection.execute(query, 
                    (
                        tipo_identificacion,
                        numero_identificacion,
                        primer_nombre,
                        segundo_nombre,
                        primer_apellido,
                        segundo_apellido,
                        edad,
                        fecha_nacimiento,
                        id
                    ))
                    
                    query = "\
                        SELECT\
                                P.ID,\
                                I.CODIGO,\
                                I.NOMBRE,\
                                P.NUMERO_IDENTIFICACION,\
                                P.PRIMER_NOMBRE,\
                                P.SEGUNDO_NOMBRE,\
                                P.PRIMER_APELLIDO,\
                                P.SEGUNDO_APELLIDO,\
                                P.EDAD,\
                                P.FECHA_NACIMIENTO,\
                                P.FECHA_CREACION,\
                                P.FECHA_ACTUALIZACION\
                        FROM\
                            TM_PERSONAS AS P\
                        INNER JOIN\
                            TR_TIPOS_IDENTIFICACION AS I\
                        ON I.ID = P.ID_TIPO_IDENTIFICACION\
                        WHERE\
                            P.ID = (SELECT MAX(ID) FROM (TM_PERSONAS))\
                    "
                    
                    connection.execute(query)
                    persona = connection.fetchone()
                    
                    if persona != None:
                        
                        return {
                            "success": True,
                            "data": {
                                "id" : persona[0],
                                "codigo_tipo_identificacion": persona[1],
                                "nombre_tipo_identificacion": persona[2],
                                "numero_identificacion": persona[3],
                                "primer_nombre": persona[4],
                                "segundo_nombre": persona[5],
                                "primer_apellido": persona[6],
                                "segundo_apellido": persona[7],
                                "edad": persona[8],
                                "fecha_nacimiento": str(persona[9]),
                                "fecha_creacion": str(persona[10]),
                                "fecha_actualizacion": str(persona[11])
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
        
    
class Personas(Resource):
    
    def get(self):
        personas = []
        
        query = "\
                SELECT\
                        P.ID,\
                        I.CODIGO,\
                        I.NOMBRE,\
                        P.NUMERO_IDENTIFICACION,\
                        P.PRIMER_NOMBRE,\
                        P.SEGUNDO_NOMBRE,\
                        P.PRIMER_APELLIDO,\
                        P.SEGUNDO_APELLIDO,\
                        P.EDAD,\
                        P.FECHA_NACIMIENTO,\
                        P.FECHA_CREACION,\
                        P.FECHA_ACTUALIZACION\
                FROM\
                    TM_PERSONAS AS P\
                INNER JOIN\
                    TR_TIPOS_IDENTIFICACION AS I\
                ON I.ID = P.ID_TIPO_IDENTIFICACION\
        "
                
        with Cursor() as connection:
            try:
                
                connection.execute(query)
                dataPersonas = connection.fetchall()
                
                if dataPersonas != None:
                    
                    for persona in dataPersonas:
                        personas.append(
                            {
                            "id" : persona[0],
                            "codigo_tipo_identificacion": persona[1],
                            "nombre_tipo_identificacion": persona[2],
                            "numero_identificacion": persona[3],
                            "primer_nombre": persona[4],
                            "segundo_nombre": persona[5],
                            "primer_apellido": persona[6],
                            "segundo_apellido": persona[7],
                            "edad": persona[8],
                            "fecha_nacimiento": str(persona[9]),
                            "fecha_creacion": str(persona[10]),
                            "fecha_actualizacion": str(persona[11])
                            }
                        )
                    
                    return {
                        "success": True,
                        "registros": len(personas),
                        "data": personas
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
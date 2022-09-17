from flask_restful import Resource, request
from flask import jsonify
from utils.cursor import Cursor
from datetime import datetime 

class Historial(Resource):

    

    def get(self, id):
                
        historial = None
        
        query = "\
                SELECT\
                        H.ID,\
                        H.FECHA_INGRESO,\
                        H.FECHA_SALIDA,\
                        H.FECHA_CREACION,\
                        H.FECHA_ACTUALIZACION,\
                        EF.ID,\
                        EF.NOMBRE,\
                        EF.DIRECCION,\
                        EF.CIUDAD,\
                        EF.ID_DEPARTAMENTO,\
                        DP.DESCRIPCION,\
                        PI.ID,\
                        TI_PI.ID,\
                        TI_PI.CODIGO,\
                        TI_PI.NOMBRE,\
                        PI.NUMERO_IDENTIFICACION,\
                        PI.PRIMER_NOMBRE,\
                        PI.SEGUNDO_NOMBRE,\
                        PI.PRIMER_APELLIDO,\
                        PI.SEGUNDO_APELLIDO,\
                        PR.ID,\
                        TI_PR.ID,\
                        TI_PR.CODIGO,\
                        TI_PR.NOMBRE,\
                        PR.NUMERO_IDENTIFICACION,\
                        PR.PRIMER_NOMBRE,\
                        PR.SEGUNDO_NOMBRE,\
                        PR.PRIMER_APELLIDO,\
                        PR.SEGUNDO_APELLIDO\
                FROM\
                    TM_HISTORIAL AS H\
                INNER JOIN\
                    TP_ESTRUCTURAS_FISICAS AS EF\
                ON\
                    EF.ID = H.ID_ESTRUCTURA_FISICA\
                INNER JOIN\
                    TR_DEPARTAMENTOS AS DP\
                ON\
                    DP.ID = EF.ID_DEPARTAMENTO\
                INNER JOIN\
                    TM_PERSONAS AS PI\
                ON\
                    PI.ID = H.ID_PERSONA_INGRESA\
                INNER JOIN\
                    TR_TIPOS_IDENTIFICACION AS TI_PI\
                ON\
                    TI_PI.ID = PI.ID_TIPO_IDENTIFICACION\
                INNER JOIN\
                    TM_PERSONAS AS PR\
                ON\
                    PR.ID = H.ID_PERSONA_REGISTRA\
                INNER JOIN\
                    TR_TIPOS_IDENTIFICACION AS TI_PR\
                ON\
                    TI_PR.ID = PR.ID_TIPO_IDENTIFICACION\
                WHERE\
                    H.ID = %s\
        "
                
        with Cursor() as connection:
            try:
                
                connection.execute(query, (id,))
                historial = connection.fetchone()
                
                if historial != None:
                    
                    return {
                        "success": True,
                        "data": {
                            "id" : historial[0],
                            "fecha_ingreso": str(historial[1]),
                            "fecha_salida": str(historial[2]),
                            "fecha_creacion": str(historial[3]),
                            "fecha_actualizacion": str(historial[4]),
                            "id_estructura_fisica": historial[5],
                            "nombre_estructura_fisica": historial[6],
                            "direccion_estructura_fisica": historial[7],
                            "ciudad_estructura_fisica": historial[8],
                            "id_departamento_estructura_fisica": historial[9],
                            "nombre_departamento_estructura_fisica": historial[10],
                            "id_persona_ingresa": historial[11],
                            "id_tipo_identificacion_persona_ingresa": historial[12],
                            "codigo_tipo_identificacion_pesona_ingresa": historial[13],
                            "nombre_tipo_identificacion_persona_ingresa": historial[14],
                            "numero_identificacion_persona_ingresa": historial[15],
                            "primer_nombre_persona_ingresa": historial[16],
                            "segundo_nombre_persona_ingresa": historial[17],
                            "primer_apellido_persona_ingresa": historial[18],
                            "segundo_apellido_persona_ingresa": historial[19],
                            "id_persona_registra": historial[20],
                            "id_tipo_identificacion_persona_registra": historial[21],
                            "codigo_tipo_identificacion_pesona_registra": historial[22],
                            "nombre_tipo_identificacion_persona_registra": historial[23],
                            "numero_identificacion_persona_registra": historial[24],
                            "primer_nombre_persona_registra": historial[25],
                            "segundo_nombre_persona_registra": historial[26],
                            "primer_apellido_persona_registra": historial[27],
                            "segundo_apellido_persona_registra": historial[28],
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
        
        historial = None
        query = "INSERT INTO TM_HISTORIAL (ID_ESTRUCTURA_FISICA, ID_PERSONA_INGRESA, ID_PERSONA_REGISTRA) VALUES(%s, %s, %s)"
        
        with Cursor() as connection:
            try:                
                connection.execute(query, 
                (
                    request.json["id_estructura_fisica"],
                    request.json["id_persona_ingresa"],
                    request.json["id_persona_registra"]
                ))
                
                query = "\
                        SELECT\
                                H.ID,\
                                H.FECHA_INGRESO,\
                                H.FECHA_SALIDA,\
                                H.FECHA_CREACION,\
                                H.FECHA_ACTUALIZACION,\
                                EF.ID,\
                                EF.NOMBRE,\
                                EF.DIRECCION,\
                                EF.CIUDAD,\
                                EF.ID_DEPARTAMENTO,\
                                DP.DESCRIPCION,\
                                PI.ID,\
                                TI_PI.ID,\
                                TI_PI.CODIGO,\
                                TI_PI.NOMBRE,\
                                PI.NUMERO_IDENTIFICACION,\
                                PI.PRIMER_NOMBRE,\
                                PI.SEGUNDO_NOMBRE,\
                                PI.PRIMER_APELLIDO,\
                                PI.SEGUNDO_APELLIDO,\
                                PR.ID,\
                                TI_PR.ID,\
                                TI_PR.CODIGO,\
                                TI_PR.NOMBRE,\
                                PR.NUMERO_IDENTIFICACION,\
                                PR.PRIMER_NOMBRE,\
                                PR.SEGUNDO_NOMBRE,\
                                PR.PRIMER_APELLIDO,\
                                PR.SEGUNDO_APELLIDO\
                        FROM\
                            TM_HISTORIAL AS H\
                        INNER JOIN\
                            TP_ESTRUCTURAS_FISICAS AS EF\
                        ON\
                            EF.ID = H.ID_ESTRUCTURA_FISICA\
                        INNER JOIN\
                            TR_DEPARTAMENTOS AS DP\
                        ON\
                            DP.ID = EF.ID_DEPARTAMENTO\
                        INNER JOIN\
                            TM_PERSONAS AS PI\
                        ON\
                            PI.ID = H.ID_PERSONA_INGRESA\
                        INNER JOIN\
                            TR_TIPOS_IDENTIFICACION AS TI_PI\
                        ON\
                            TI_PI.ID = PI.ID_TIPO_IDENTIFICACION\
                        INNER JOIN\
                            TM_PERSONAS AS PR\
                        ON\
                            PR.ID = H.ID_PERSONA_REGISTRA\
                        INNER JOIN\
                            TR_TIPOS_IDENTIFICACION AS TI_PR\
                        ON\
                            TI_PR.ID = PR.ID_TIPO_IDENTIFICACION\
                        WHERE\
                            H.ID = (SELECT MAX(ID) FROM (TM_HISTORIAL))\
                "
                
                connection.execute(query)
                historial = connection.fetchone()
                
                if historial != None:
                    
                    return {
                        "success": True,
                        "data": {
                            "id" : historial[0],
                            "fecha_ingreso": str(historial[1]),
                            "fecha_salida": str(historial[2]),
                            "fecha_creacion": str(historial[3]),
                            "fecha_actualizacion": str(historial[4]),
                            "id_estructura_fisica": historial[5],
                            "nombre_estructura_fisica": historial[6],
                            "direccion_estructura_fisica": historial[7],
                            "ciudad_estructura_fisica": historial[8],
                            "id_departamento_estructura_fisica": historial[9],
                            "nombre_departamento_estructura_fisica": historial[10],
                            "id_persona_ingresa": historial[11],
                            "id_tipo_identificacion_persona_ingresa": historial[12],
                            "codigo_tipo_identificacion_pesona_ingresa": historial[13],
                            "nombre_tipo_identificacion_persona_ingresa": historial[14],
                            "numero_identificacion_persona_ingresa": historial[15],
                            "primer_nombre_persona_ingresa": historial[16],
                            "segundo_nombre_persona_ingresa": historial[17],
                            "primer_apellido_persona_ingresa": historial[18],
                            "segundo_apellido_persona_ingresa": historial[19],
                            "id_persona_registra": historial[20],
                            "id_tipo_identificacion_persona_registra": historial[21],
                            "codigo_tipo_identificacion_pesona_registra": historial[22],
                            "nombre_tipo_identificacion_persona_registra": historial[23],
                            "numero_identificacion_persona_registra": historial[24],
                            "primer_nombre_persona_registra": historial[25],
                            "segundo_nombre_persona_registra": historial[26],
                            "primer_apellido_persona_registra": historial[27],
                            "segundo_apellido_persona_registra": historial[28],
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
                
        historial = None
        
        query = "\
                SELECT\
                        H.ID,\
                        H.FECHA_INGRESO,\
                        H.FECHA_SALIDA,\
                        H.FECHA_CREACION,\
                        H.FECHA_ACTUALIZACION,\
                        EF.ID,\
                        EF.NOMBRE,\
                        EF.DIRECCION,\
                        EF.CIUDAD,\
                        EF.ID_DEPARTAMENTO,\
                        DP.DESCRIPCION,\
                        PI.ID,\
                        TI_PI.ID,\
                        TI_PI.CODIGO,\
                        TI_PI.NOMBRE,\
                        PI.NUMERO_IDENTIFICACION,\
                        PI.PRIMER_NOMBRE,\
                        PI.SEGUNDO_NOMBRE,\
                        PI.PRIMER_APELLIDO,\
                        PI.SEGUNDO_APELLIDO,\
                        PR.ID,\
                        TI_PR.ID,\
                        TI_PR.CODIGO,\
                        TI_PR.NOMBRE,\
                        PR.NUMERO_IDENTIFICACION,\
                        PR.PRIMER_NOMBRE,\
                        PR.SEGUNDO_NOMBRE,\
                        PR.PRIMER_APELLIDO,\
                        PR.SEGUNDO_APELLIDO\
                FROM\
                    TM_HISTORIAL AS H\
                INNER JOIN\
                    TP_ESTRUCTURAS_FISICAS AS EF\
                ON\
                    EF.ID = H.ID_ESTRUCTURA_FISICA\
                INNER JOIN\
                    TR_DEPARTAMENTOS AS DP\
                ON\
                    DP.ID = EF.ID_DEPARTAMENTO\
                INNER JOIN\
                    TM_PERSONAS AS PI\
                ON\
                    PI.ID = H.ID_PERSONA_INGRESA\
                INNER JOIN\
                    TR_TIPOS_IDENTIFICACION AS TI_PI\
                ON\
                    TI_PI.ID = PI.ID_TIPO_IDENTIFICACION\
                INNER JOIN\
                    TM_PERSONAS AS PR\
                ON\
                    PR.ID = H.ID_PERSONA_REGISTRA\
                INNER JOIN\
                    TR_TIPOS_IDENTIFICACION AS TI_PR\
                ON\
                    TI_PR.ID = PR.ID_TIPO_IDENTIFICACION\
                WHERE\
                    H.ID = %s\
        "
        
        
        with Cursor() as connection:
            try:
                connection.execute(query, (id,))
                historial = connection.fetchone()
                
                query = "DELETE FROM TM_HISTORIAL WHERE ID = %s"                
                connection.execute(query, (id,))
                
                if historial != None:
                    
                    return {
                        "success": True,
                        "data": {
                            "id" : historial[0],
                            "fecha_ingreso": str(historial[1]),
                            "fecha_salida": str(historial[2]),
                            "fecha_creacion": str(historial[3]),
                            "fecha_actualizacion": str(historial[4]),
                            "id_estructura_fisica": historial[5],
                            "nombre_estructura_fisica": historial[6],
                            "direccion_estructura_fisica": historial[7],
                            "ciudad_estructura_fisica": historial[8],
                            "id_departamento_estructura_fisica": historial[9],
                            "nombre_departamento_estructura_fisica": historial[10],
                            "id_persona_ingresa": historial[11],
                            "id_tipo_identificacion_persona_ingresa": historial[12],
                            "codigo_tipo_identificacion_pesona_ingresa": historial[13],
                            "nombre_tipo_identificacion_persona_ingresa": historial[14],
                            "numero_identificacion_persona_ingresa": historial[15],
                            "primer_nombre_persona_ingresa": historial[16],
                            "segundo_nombre_persona_ingresa": historial[17],
                            "primer_apellido_persona_ingresa": historial[18],
                            "segundo_apellido_persona_ingresa": historial[19],
                            "id_persona_registra": historial[20],
                            "id_tipo_identificacion_persona_registra": historial[21],
                            "codigo_tipo_identificacion_pesona_registra": historial[22],
                            "nombre_tipo_identificacion_persona_registra": historial[23],
                            "numero_identificacion_persona_registra": historial[24],
                            "primer_nombre_persona_registra": historial[25],
                            "segundo_nombre_persona_registra": historial[26],
                            "primer_apellido_persona_registra": historial[27],
                            "segundo_apellido_persona_registra": historial[28],
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
        
        historial = None
        
        query = "\
                SELECT\
                        ID_ESTRUCTURA_FISICA,\
                        FECHA_INGRESO,\
                        FECHA_SALIDA,\
                        ID_PERSONA_INGRESA,\
                        ID_PERSONA_REGISTRA\
                FROM\
                    TM_HISTORIAL\
                WHERE\
                    ID = %s\
        "
        
        with Cursor() as connection:
            try:
                connection.execute(query, (id,))
                dataHistorial = connection.fetchone()
                
                if dataHistorial != None:
                    historial = {
                        "id_estructura_fisica" : dataHistorial[0],
                        "fecha_ingreso": str(dataHistorial[1]),
                        "fecha_salida": str(dataHistorial[2]),
                        "id_persona_ingresa": dataHistorial[3],
                        "id_persona_registra": dataHistorial[4]
                    }
                    
                    id_estructura_fisica = None
                    fecha_ingreso = None
                    fecha_salida = None
                    id_persona_ingresa = None
                    id_persona_registra = None
                    
                    if "id_estructura_fisica" in request.json and historial["id_estructura_fisica"] != request.json["id_estructura_fisica"]:
                        id_estructura_fisica = request.json["id_estructura_fisica"]
                    else:
                        id_estructura_fisica = historial["id_estructura_fisica"]
                    
                    if "fecha_ingreso" in request.json and historial["fecha_ingreso"] != request.json["fecha_ingreso"]:
                        fecha_ingreso = request.json["fecha_ingreso"]
                    else:
                        fecha_ingreso = historial["fecha_ingreso"]
                        
                    if "fecha_salida" in request.json and historial["fecha_salida"] != request.json["fecha_salida"]:
                        fecha_salida = request.json["fecha_salida"]
                    else:
                        fecha_salida = historial["fecha_salida"]
                        
                    if "id_persona_ingresa" in request.json and historial["id_persona_ingresa"] != request.json["id_persona_ingresa"]:
                        id_persona_ingresa = request.json["id_persona_ingresa"]
                    else:
                        id_persona_ingresa = historial["id_persona_ingresa"]
                        
                    if "id_persona_registra" in request.json and historial["id_persona_registra"] != request.json["id_persona_registra"]:
                        id_persona_registra = request.json["id_persona_registra"]
                    else:
                        id_persona_registra = historial["id_persona_registra"]
                        
                    
                    query = "\
                        UPDATE\
                            TM_HISTORIAL\
                        SET\
                            FECHA_INGRESO = %s,\
                            ID_PERSONA_INGRESA = %s,\
                            ID_PERSONA_REGISTRA = %s,\
                            ID_ESTRUCTURA_FISICA = %s,\
                            FECHA_ACTUALIZACION = NOW()\
                        WHERE ID = %s\
                    "
                    
                    connection.execute(query, 
                    (
                        fecha_ingreso,                        
                        id_persona_ingresa,
                        id_persona_registra,
                        id_estructura_fisica,
                        id
                    ))
                    
                    if fecha_salida != "None":
                        
                        query = "\
                            UPDATE\
                                TM_HISTORIAL\
                            SET\
                                FECHA_SALIDA = %s,\
                                FECHA_ACTUALIZACION = NOW()\
                            WHERE ID = %s\
                        "
                        connection.execute(query, 
                        (
                            fecha_salida,
                            id
                        )) 
                    
                    query = "\
                            SELECT\
                                    H.ID,\
                                    H.FECHA_INGRESO,\
                                    H.FECHA_SALIDA,\
                                    H.FECHA_CREACION,\
                                    H.FECHA_ACTUALIZACION,\
                                    EF.ID,\
                                    EF.NOMBRE,\
                                    EF.DIRECCION,\
                                    EF.CIUDAD,\
                                    EF.ID_DEPARTAMENTO,\
                                    DP.DESCRIPCION,\
                                    PI.ID,\
                                    TI_PI.ID,\
                                    TI_PI.CODIGO,\
                                    TI_PI.NOMBRE,\
                                    PI.NUMERO_IDENTIFICACION,\
                                    PI.PRIMER_NOMBRE,\
                                    PI.SEGUNDO_NOMBRE,\
                                    PI.PRIMER_APELLIDO,\
                                    PI.SEGUNDO_APELLIDO,\
                                    PR.ID,\
                                    TI_PR.ID,\
                                    TI_PR.CODIGO,\
                                    TI_PR.NOMBRE,\
                                    PR.NUMERO_IDENTIFICACION,\
                                    PR.PRIMER_NOMBRE,\
                                    PR.SEGUNDO_NOMBRE,\
                                    PR.PRIMER_APELLIDO,\
                                    PR.SEGUNDO_APELLIDO\
                            FROM\
                                TM_HISTORIAL AS H\
                            INNER JOIN\
                                TP_ESTRUCTURAS_FISICAS AS EF\
                            ON\
                                EF.ID = H.ID_ESTRUCTURA_FISICA\
                            INNER JOIN\
                                TR_DEPARTAMENTOS AS DP\
                            ON\
                                DP.ID = EF.ID_DEPARTAMENTO\
                            INNER JOIN\
                                TM_PERSONAS AS PI\
                            ON\
                                PI.ID = H.ID_PERSONA_INGRESA\
                            INNER JOIN\
                                TR_TIPOS_IDENTIFICACION AS TI_PI\
                            ON\
                                TI_PI.ID = PI.ID_TIPO_IDENTIFICACION\
                            INNER JOIN\
                                TM_PERSONAS AS PR\
                            ON\
                                PR.ID = H.ID_PERSONA_REGISTRA\
                            INNER JOIN\
                                TR_TIPOS_IDENTIFICACION AS TI_PR\
                            ON\
                                TI_PR.ID = PR.ID_TIPO_IDENTIFICACION\
                            WHERE\
                                H.ID = %s\
                    "
                    
                    connection.execute(query, (id,))
                    historial = connection.fetchone()
                    
                    if historial != None:
                        
                        return {
                            "success": True,
                            "data": {
                                "id" : historial[0],
                                "fecha_ingreso": str(historial[1]),
                                "fecha_salida": str(historial[2]),
                                "fecha_creacion": str(historial[3]),
                                "fecha_actualizacion": str(historial[4]),
                                "id_estructura_fisica": historial[5],
                                "nombre_estructura_fisica": historial[6],
                                "direccion_estructura_fisica": historial[7],
                                "ciudad_estructura_fisica": historial[8],
                                "id_departamento_estructura_fisica": historial[9],
                                "nombre_departamento_estructura_fisica": historial[10],
                                "id_persona_ingresa": historial[11],
                                "id_tipo_identificacion_persona_ingresa": historial[12],
                                "codigo_tipo_identificacion_pesona_ingresa": historial[13],
                                "nombre_tipo_identificacion_persona_ingresa": historial[14],
                                "numero_identificacion_persona_ingresa": historial[15],
                                "primer_nombre_persona_ingresa": historial[16],
                                "segundo_nombre_persona_ingresa": historial[17],
                                "primer_apellido_persona_ingresa": historial[18],
                                "segundo_apellido_persona_ingresa": historial[19],
                                "id_persona_registra": historial[20],
                                "id_tipo_identificacion_persona_registra": historial[21],
                                "codigo_tipo_identificacion_pesona_registra": historial[22],
                                "nombre_tipo_identificacion_persona_registra": historial[23],
                                "numero_identificacion_persona_registra": historial[24],
                                "primer_nombre_persona_registra": historial[25],
                                "segundo_nombre_persona_registra": historial[26],
                                "primer_apellido_persona_registra": historial[27],
                                "segundo_apellido_persona_registra": historial[28],
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
        
    
# class EstructurasFisicas(Resource):
    
#     def get(self):
#         estructuras = []
        
#         query = "\
#                 SELECT\
#                         EF.ID,\
#                         EF.NOMBRE,\
#                         EF.DIRECCION,\
#                         EF.CIUDAD,\
#                         EF.FECHA_CREACION,\
#                         EF.FECHA_ACTUALIZACION,\
#                         DP.ID,\
#                         DP.DESCRIPCION\
#                 FROM\
#                     TP_ESTRUCTURAS_FISICAS AS EF\
#                 INNER JOIN\
#                     TR_DEPARTAMENTOS AS DP\
#                 ON DP.ID = EF.ID_DEPARTAMENTO\
#         "
                
#         with Cursor() as connection:
#             try:
                
#                 connection.execute(query)
#                 dataEstructuras = connection.fetchall()
                
#                 if dataEstructuras != None:
                    
#                     for estructura in dataEstructuras:
#                         estructuras.append(
#                             {
#                             "id" : estructura[0],
#                             "nombre": estructura[1],
#                             "direccion": estructura[2],
#                             "ciudad": estructura[3],
#                             "fecha_creacion": str(estructura[4]),
#                             "fecha_actualizacion": str(estructura[5]),
#                             "id_departamento": estructura[6],
#                             "nombre_departamento": estructura[7]
#                             }
#                         )
                    
#                     return {
#                         "success": True,
#                         "registros": len(estructuras),
#                         "data": estructuras
#                     }
#                 else:
#                     return {
#                         "success" : False
#                     }       
            
#             except Exception as ex:
#                 return {
#                     "success" : False,
#                     "error": str(ex)
#                 }
from flask_restful import Resource, request
from flask import jsonify
from utils.cursor import Cursor
from datetime import datetime 

class TipoIdentificacion(Resource):

    

    def get(self, id):
                
        tipoIdentificacion = None
        
        query = "\
                SELECT\
                        ID,\
                        CODIGO,\
                        NOMBRE\
                FROM\
                    TR_TIPOS_IDENTIFICACION\
                WHERE\
                    ID = %s\
        "
                
        with Cursor() as connection:
            try:
                
                connection.execute(query, (id,))
                tipoIdentificacion = connection.fetchone()
                
                if tipoIdentificacion != None:
                    
                    return {
                        "success": True,
                        "data": {
                            "id" : tipoIdentificacion[0],
                            "codigo" : tipoIdentificacion[1],
                            "nombre": tipoIdentificacion[2],
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

    
class TiposIdentificacion(Resource):
    
    def get(self):
        
        tiposIdentificacion = []
        
        query = "\
                SELECT\
                        ID,\
                        CODIGO,\
                        NOMBRE\
                FROM\
                    TR_TIPOS_IDENTIFICACION\
        "
                
        with Cursor() as connection:
            try:                
                connection.execute(query)
                dataDepartamentos = connection.fetchall()
                
                if tiposIdentificacion != None:
                    
                    for tipoIdentificacion in dataDepartamentos:
                        tiposIdentificacion.append(
                             {
                                "id" : tipoIdentificacion[0],
                                "codigo" : tipoIdentificacion[1],   
                                "nombre": tipoIdentificacion[2],
                            }
                        )
                    
                    return {
                        "success": True,
                        "registros" : len(tiposIdentificacion),
                        "data": tiposIdentificacion
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
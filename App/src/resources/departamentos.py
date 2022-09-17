from flask_restful import Resource, request
from flask import jsonify
from utils.cursor import Cursor
from datetime import datetime 

class Departamento(Resource):

    

    def get(self, id):
                
        departamento = None
        
        query = "\
                SELECT\
                        ID,\
                        DESCRIPCION\
                FROM\
                    TR_DEPARTAMENTOS\
                WHERE\
                    ID = %s\
        "
                
        with Cursor() as connection:
            try:
                
                connection.execute(query, (id,))
                departamento = connection.fetchone()
                
                if departamento != None:
                    
                    return {
                        "success": True,
                        "data": {
                            "id" : departamento[0],
                            "nombre": departamento[1],
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

    
class Departamentos(Resource):
    
    def get(self):
        
        departamentos = []
        
        query = "\
                SELECT\
                        ID,\
                        DESCRIPCION\
                FROM\
                    TR_DEPARTAMENTOS\
        "
                
        with Cursor() as connection:
            try:                
                connection.execute(query)
                dataDepartamentos = connection.fetchall()
                
                if departamentos != None:
                    
                    for departamento in dataDepartamentos:
                        departamentos.append(
                            {
                                "id" : departamento[0],
                                "nombre": departamento[1]
                            }
                        )
                    
                    return {
                        "success": True,
                        "registros" : len(departamentos),
                        "data": departamentos
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
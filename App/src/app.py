from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():    
    return 'Gestión de personas '

from resources.persona import Persona, Personas
from resources.estructuraFisica import EstructuraFisica, EstructurasFisicas
from resources.historial import Historial
from resources.departamentos import Departamento, Departamentos
from resources.tipoIdentificacion import TipoIdentificacion, TiposIdentificacion

api.add_resource(Persona, '/persona/<id>', '/persona')
api.add_resource(Personas, '/personas')

api.add_resource(EstructuraFisica, '/estructuraFisica/<id>', '/estructuraFisica')
api.add_resource(EstructurasFisicas, '/estructurasFisicas')

api.add_resource(Historial, '/historial/<id>', '/historial')

api.add_resource(Departamento, '/departamento/<id>')
api.add_resource(Departamentos, '/departamentos')

api.add_resource(TipoIdentificacion, '/tipoIdentificacion/<id>')
api.add_resource(TiposIdentificacion, '/tiposIdentificacion')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3090, debug=True)
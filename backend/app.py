from flask import Flask
from flask_cors import CORS
from controlador.controlador import rutas
from controlador.controlador_usuario import ControladorUsuario
from controlador.controlador_diagnostico import ControladorDiagnostico
from controlador.controlador_resultados import ControladorResultados
from controlador.controlador_admin import ControladorAdmin
from controlador.controlador_configuracion import ControladorConfiguracion
from controlador.controlador_sesion import ControladorSesion

app = Flask(__name__)
CORS(app, 
     resources={
         r"/*": { 
             "origins": "https://unfv-dec-react.onrender.com",
             "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
             "allow_headers": ["Content-Type", "Authorization"], 
             "supports_credentials": True 
         }
     })
app.secret_key = 'SECRET_KEY'
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True

app.register_blueprint(rutas)
app.register_blueprint(ControladorUsuario.blueprint)
app.register_blueprint(ControladorDiagnostico.blueprint)
app.register_blueprint(ControladorResultados.blueprint)
app.register_blueprint(ControladorAdmin.blueprint)
app.register_blueprint(ControladorConfiguracion.blueprint)
app.register_blueprint(ControladorSesion.blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

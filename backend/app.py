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
         r"/*": {  # O puedes especificar rutas como r"/login"
             "origins": "https://unfv-dec-react-0yp3.onrender.com",  # Tu frontend
             "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Métodos permitidos
             "allow_headers": ["Content-Type", "Authorization"],  # Headers permitidos
             "supports_credentials": True  # Para cookies/sesiones
         }
     })
app.secret_key = 'SECRET_KEY'

# Registrar blueprint de rutas
app.register_blueprint(rutas)
app.register_blueprint(ControladorUsuario.blueprint)
app.register_blueprint(ControladorDiagnostico.blueprint)
app.register_blueprint(ControladorResultados.blueprint)
app.register_blueprint(ControladorAdmin.blueprint)
app.register_blueprint(ControladorConfiguracion.blueprint)
app.register_blueprint(ControladorSesion.blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

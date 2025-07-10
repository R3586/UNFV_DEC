from flask import Blueprint, jsonify, session, request
from modelo.modelo_configuracion import ModeloConfiguracion

class ControladorConfiguracion:
    blueprint = Blueprint('configuracion', __name__)

    @staticmethod
    @blueprint.route('/api/configuracion', methods=['GET', 'POST'])
    def configuracion():
        if not session.get('logged_in'):
            return jsonify({'message': 'No autorizado'}), 401
        
        if request.method == 'GET':
            datos = ModeloConfiguracion.obtener_datos_usuario(session['user_id'])
            if datos:
                return jsonify(datos), 200
            return jsonify({'message': 'Usuario no encontrado'}), 404
        
        if request.method == 'POST':
            data = request.json
            exito = ModeloConfiguracion.actualizar_datos_usuario(session['user_id'], data)
            if exito:
                return jsonify({'message': 'Datos actualizados correctamente'}), 200
            return jsonify({'message': 'Error al actualizar datos'}), 500
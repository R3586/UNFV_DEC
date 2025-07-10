from flask import Blueprint, jsonify, session, request
from modelo.modelo_admin import ModeloAdmin

class ControladorAdmin:
    blueprint = Blueprint('admin', __name__)

    @staticmethod
    @blueprint.route('/api/admin', methods=['GET'])
    def admin_panel():
        if not session.get('logged_in') or session.get('user_type') != 'admin':
            return jsonify({'message': 'Acceso no autorizado'}), 403
        
        filtro = request.args.get('filtro', '').lower()
        pacientes = ModeloAdmin.obtener_pacientes(filtro)
        return jsonify({'pacientes': pacientes}), 200

    @staticmethod
    @blueprint.route('/api/admin/diagnosticos/<int:usuario_id>', methods=['GET'])
    def obtener_historial_usuario(usuario_id):
        if not session.get('logged_in') or session.get('user_type') != 'admin':
            return jsonify({'message': 'Acceso no autorizado'}), 403
        
        historial = ModeloAdmin.obtener_historial_diagnosticos(usuario_id)
        return jsonify(historial), 200
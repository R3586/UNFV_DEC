from flask import Blueprint, jsonify, session
from modelo.modelo_resultados import ModeloResultados
from datetime import datetime

class ControladorResultados:
    blueprint = Blueprint('resultados', __name__)

    @staticmethod
    @blueprint.route('/api/resultados', methods=['GET'])
    def resultados():
        if not session.get('logged_in'):
            return jsonify({'message': 'Unauthorized'}), 401
        diagnostico = None
        if 'ultimo_diagnostico' in session:
            riesgo, confianza, fecha_str = session['ultimo_diagnostico']
            diagnostico = {'riesgo': riesgo, 'confianza': confianza, 'fecha': fecha_str}
            session.pop('ultimo_diagnostico')
        else:
            row = ModeloResultados.obtener_ultimo_diagnostico(session['user_id'])
            if row:
                diagnostico = {'riesgo': row[0], 'confianza': row[1], 'fecha': row[2]}
        return jsonify({'diagnostico': diagnostico}), 200

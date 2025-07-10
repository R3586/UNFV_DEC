import psycopg2
from modelo.modelo import obtener_conexion_bd

class ModeloResultados:
    @staticmethod
    def obtener_ultimo_diagnostico(usuario_id):
        conn = obtener_conexion_bd()
        cur = conn.cursor()
        cur.execute("""
            SELECT r.riesgo, r.confianza, r.fecha_diagnostico 
            FROM diagnostico_resultados r
            JOIN diagnostico_datos d ON r.datos_id = d.id
            WHERE d.usuario_id = %s 
            ORDER BY r.fecha_diagnostico DESC 
            LIMIT 1
        """, (usuario_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        return row

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import Lexer
import Syntactic
import Logs as loger

app = Flask(__name__)
CORS(app)


@app.route('/analizar-ruby', methods=['POST'])
def analizar_codigo_ruby():
    try:
        # Obtener el código del request
        data = request.get_json()

        if not data or 'codigo' not in data:
            return jsonify({
                "status": "error",
                "errores": ["No se proporcionó código para analizar"]
            }), 400

        input_code = data['codigo']

        # Limpiar listas de errores antes del análisis
        Lexer.error_list.clear()
        Syntactic.error_list.clear()

        # Realizar análisis léxico y sintáctico
        syntactic_result = Syntactic.analysing(input_code)
        lexer_errors = Lexer.error_list

        # Manejar casos donde el resultado puede ser None
        syntactic_errors = syntactic_result if syntactic_result is not None else []

        # Combinar errores de análisis léxico y sintáctico
        all_errors = lexer_errors + syntactic_errors

        # Registrar logs
        try:
            loger.create_log(Lexer.lexer, "ruby_analysis", input_code, lexer_errors)
            loger.create_syntactic_log(Syntactic.parser, "ruby_analysis", input_code, syntactic_errors)
        except Exception as log_error:
            print(f"Error al crear logs: {log_error}")

        # Responder según la presencia de errores
        if all_errors:
            return jsonify({
                "status": "error",
                "errores": all_errors
            }), 400
        else:
            return jsonify({
                "status": "success",
                "mensaje": "Código Ruby analizado correctamente sin errores"
            }), 200

    except Exception as e:
        # Manejo de errores generales
        return jsonify({
            "status": "error",
            "errores": [f"Error interno del servidor: {str(e)}"]
        }), 500


if __name__ == '__main__':
    # Asegúrate de tener instaladas las dependencias: flask, flask-cors, ply
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
from datetime import datetime
import os

def create_log(lexer, usuario, data, errors):
    os.makedirs("logs", exist_ok=True)
    fecha_hora = datetime.now().strftime("%d%m%Y-%Hh%M")
    log_filename = f"logs/lexico-{usuario}-{fecha_hora}.txt"
    with open(log_filename, "w") as log_file:
        lexer.input(data)
        # Tokenizar y registrar tokens válidos en el archivo de log
        while True:
            tok = lexer.token()
            if not tok:
                break
            log_file.write(str(tok) + "\n")
            print(tok)

        log_file.write("\nErrores:\n")
        for error in errors:
            log_file.write(error + "\n")


def create_syntactic_log(parser, usuario, code, error_list):
    # Crear directorio de logs si no existe
    os.makedirs("logs", exist_ok=True)

    # Nombre del archivo de log (si ya existe, se agrega nuevo contenido)
    fecha_hora = datetime.now().strftime("%d%m%Y-%Hh%M")
    log_filename = f"logs/sintactico-{usuario}-{fecha_hora}.txt"

    # Abrir archivo de log en modo append para agregar entradas sin sobrescribir
    with open(log_filename, "a") as log_file:
        # Escribir un separador y fecha para distinguir cada análisis
        log_file.write("\n\n" + "=" * 30 + "\n")
        log_file.write(f"Log Entry \n")
        log_file.write("=" * 30 + "\n\n")

        # Escribir el código de entrada
        log_file.write("Input Code:\n")
        log_file.write(code + "\n\n")

        # Intentar analizar el código
        try:
            result = parser.parse(code)

            log_file.write("Parsing Result:\n")
            if result is not None:
                log_file.write("Successful parse\n")
            else:
                log_file.write("Parse completed without explicit result\n")

        except Exception as e:
            log_file.write(f"Parsing Exception: {str(e)}\n")

        # Escribir errores sintácticos
        log_file.write("\nSyntax Errors:\n")
        if error_list:
            for error in error_list:
                log_file.write(error + "\n")
        else:
            log_file.write("No syntax errors detected\n")

    print(f"Syntactic analysis log updated: {log_filename}")
    return log_filename

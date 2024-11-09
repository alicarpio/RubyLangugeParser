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
            print(tok)  # Opcional, para ver también en la consola

        # Registrar errores almacenados en la lista
        log_file.write("\nErrores:\n")
        for error in errors:
            log_file.write(error + "\n")

    print(f"Log creado: {log_filename}")
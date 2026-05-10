
# IMPORTACIÓN DE FECHA Y HORA


from datetime import datetime


# FUNCIÓN PARA REGISTRAR LOGS


def registrar_log(mensaje):

    try:

        # Obtiene fecha y hora actual
        fecha = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Abre archivo logs.txt
        with open(
            "logs.txt",
            "a",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                f"[{fecha}] -> {mensaje}\n"
            )

    except Exception as e:

        print(
            f"Error al escribir log: {e}"
        )

# IMPORTACIONES

# Clase abstracta base
from modelos.entidad import Entidad

# Excepción personalizada
from excepciones.excepciones_personalizadas import ErrorCliente

# Sistema de logs
from utils.logger import registrar_log


# CLASE CLIENTE

# Clase que representa un cliente del sistema
class Cliente(Entidad):

 
    # CONSTRUCTOR

    def __init__(self, nombre, documento, correo):

        # Encapsulación de atributos
        self.__nombre = None
        self.__documento = None
        self.__correo = None

        # Validaciones mediante setters
        self.set_nombre(nombre)
        self.set_documento(documento)
        self.set_correo(correo)

    # GETTERS

    # Retorna el nombre del cliente
    def get_nombre(self):
        return self.__nombre

    # Retorna el documento
    def get_documento(self):
        return self.__documento

    # Retorna el correo
    def get_correo(self):
        return self.__correo

 
    # SETTERS CON VALIDACIONES

    # Método para validar y asignar nombre
    def set_nombre(self, nombre):

        try:

            if not nombre.strip():
                raise ErrorCliente(
                    "El nombre no puede estar vacío"
                )

            if len(nombre) < 3:
                raise ErrorCliente(
                    "El nombre es demasiado corto"
                )

            self.__nombre = nombre

            registrar_log(
                f"Nombre asignado correctamente: {nombre}"
            )

        except ErrorCliente as e:

            registrar_log(f"ERROR CLIENTE: {e}")
            raise

    # Método para validar documento
    def set_documento(self, documento):

        try:

            if not documento.isdigit():
                raise ErrorCliente(
                    "El documento debe contener solo números"
                )

            if len(documento) < 5:
                raise ErrorCliente(
                    "El documento es demasiado corto"
                )

            self.__documento = documento

            registrar_log(
                f"Documento asignado correctamente: {documento}"
            )

        except ErrorCliente as e:

            registrar_log(f"ERROR DOCUMENTO: {e}")
            raise

    # Método para validar correo electrónico
    def set_correo(self, correo):

        try:

            if (
                "@" not in correo
                or "." not in correo
                or len(correo) < 8
            ):

                raise ErrorCliente(
                    "Correo electrónico inválido"
                )

            self.__correo = correo

            registrar_log(
                f"Correo asignado correctamente: {correo}"
            )

        except ErrorCliente as e:

            registrar_log(f"ERROR CORREO: {e}")
            raise

 
    # MÉTODO ABSTRACTO IMPLEMENTADO

    # Muestra la información del cliente
    def mostrar_informacion(self):

        return (
            f"Cliente: {self.__nombre}\n"
            f"Documento: {self.__documento}\n"
            f"Correo: {self.__correo}"
        )

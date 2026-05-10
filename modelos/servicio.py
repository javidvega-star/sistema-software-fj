
# IMPORTACIONES


from abc import ABC, abstractmethod

from excepciones.excepciones_personalizadas import ErrorServicio

from utils.logger import registrar_log


# CLASE ABSTRACTA SERVICIO


class Servicio(ABC):

    # Constructor base
    def __init__(self, nombre, costo_base):

        self.nombre = nombre
        self.costo_base = costo_base

    # Método abstracto para calcular costos
    @abstractmethod
    def calcular_costo(self):
        pass

    # Método abstracto para describir servicio
    @abstractmethod
    def describir_servicio(self):
        pass



# SERVICIO RESERVA DE SALA


class ReservaSala(Servicio):

    def __init__(self, nombre, costo_base, horas):

        super().__init__(nombre, costo_base)

        try:

            if horas <= 0:
                raise ErrorServicio(
                    "Las horas deben ser mayores a cero"
                )

            self.horas = horas

            registrar_log(
                f"ReservaSala creada correctamente: {nombre}"
            )

        except ErrorServicio as e:

            registrar_log(f"ERROR SERVICIO: {e}")
            raise

    def calcular_costo(self):

        return self.costo_base * self.horas

    def describir_servicio(self):

        return (
            f"Servicio: Reserva de Sala\n"
            f"Horas: {self.horas}\n"
            f"Costo: {self.calcular_costo()}"
        )



# SERVICIO ALQUILER DE EQUIPOS


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_base, dias):

        super().__init__(nombre, costo_base)

        try:

            if dias <= 0:
                raise ErrorServicio(
                    "Los días deben ser mayores a cero"
                )

            self.dias = dias

            registrar_log(
                f"AlquilerEquipo creado: {nombre}"
            )

        except ErrorServicio as e:

            registrar_log(f"ERROR ALQUILER: {e}")
            raise

    def calcular_costo(self):

        return self.costo_base * self.dias

    def describir_servicio(self):

        return (
            f"Servicio: Alquiler de Equipo\n"
            f"Días: {self.dias}\n"
            f"Costo: {self.calcular_costo()}"
        )



# SERVICIO ASESORÍA ESPECIALIZADA


class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, costo_base, nivel):

        super().__init__(nombre, costo_base)

        niveles_validos = [
            "basica",
            "intermedia",
            "avanzada"
        ]

        try:

            if nivel.lower() not in niveles_validos:

                raise ErrorServicio(
                    "Nivel de asesoría inválido"
                )

            self.nivel = nivel.lower()

            registrar_log(
                f"Asesoría creada correctamente: {nombre}"
            )

        except ErrorServicio as e:

            registrar_log(f"ERROR ASESORÍA: {e}")
            raise

    def calcular_costo(self):

        if self.nivel == "basica":
            return self.costo_base

        elif self.nivel == "intermedia":
            return self.costo_base * 1.5

        else:
            return self.costo_base * 2

    def describir_servicio(self):

        return (
            f"Servicio: Asesoría Especializada\n"
            f"Nivel: {self.nivel}\n"
            f"Costo: {self.calcular_costo()}"
        )
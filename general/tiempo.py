import logging
from datetime import datetime

from .log import setup_logging
from .validaciones import Validaciones

# Configura el logging
setup_logging()
# Obtiene un logger para este módulo
logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class Tiempo:
    """Una clase que contiene métodos para realizar operaciones con marcas de tiempo,
    entre otras
    """

    def marca_a_ms(marca_tiempo: str, credenciales: dict = {}) -> tuple[int, str]:
        """Convierte una cadena de tiempo de formato hh:mm:ss.sss a milisegundos

        Args:
            marca_tiempo (str): Una cadena de tiempo en formato hh:mm:ss.sss
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[int, str]: El tiempo en milisegundos y mensaje de error
        """
        # Validar que 'marca_tiempo' sea del tipo str
        res, msj = Validaciones.es_tipo(marca_tiempo, str, credenciales)
        if not res:
            return None, msj
        # Validar que 'marca_tiempo' esté compuesto de 3 elementos al hacer split
        res, msj = Validaciones.es_len_correcto(
            marca_tiempo.split(":"), 3, credenciales
        )
        if not res:
            return None, msj
        # Intenta calcular los milisegundos
        try:
            horas = int(marca_tiempo.split(":")[0])
            minutos = int(marca_tiempo.split(":")[1])
            segundos = float(marca_tiempo.split(":")[2])
            return (int)((horas * 60 * 60 + minutos * 60 + segundos) * 1000), None
        except ValueError as e:
            mensaje = f"La marca_tiempo debe contener números válidos: {e}"
            logger.exception(mensaje)
            return None, "Error tiempo"
        except Exception as e:
            mensaje = f"No se convirtió a milisegundos, problema imprevisto: {e}"
            logger.exception(mensaje)
            return None, "Error tiempo"

    @staticmethod
    def calcular_intervalo(
        inicio: str, fin: str, frmt_tiempo: str = "%H:%M:%S.%f", credenciales: dict = {}
    ) -> tuple[float, str]:
        """Devuelve el intervalo de tiempo entre las dos marcas seleccionadas, las
        cuales previamente fueran convertidas a datetime en el formato indicado

        Args:
            inicio (str): Una cadena de tiempo en formato hh:mm:ss.sss
            fin (str): Una cadena de tiempo en formato hh:mm:ss.sss
            frmt_tiempo (str): Formato de tiempo para inicio y fin
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[float, str]: Intervalo de tiempo en segundos y mensaje de error
        """
        # Validar que 'inicio' sea del tipo str
        res, msj = Validaciones.es_tipo(inicio, str, credenciales)
        if not res:
            return None, msj
        # Validar que 'inicio' esté compuesto de 3 elementos al hacer split
        res, msj = Validaciones.es_len_correcto(inicio.split(":"), 3, credenciales)
        if not res:
            return None, msj
        # Validar que 'fin' sea del tipo str
        res, msj = Validaciones.es_tipo(fin, str, credenciales)
        if not res:
            return None, msj
        # Validar que 'fin' esté compuesto de 3 elementos al hacer split
        res, msj = Validaciones.es_len_correcto(fin.split(":"), 3, credenciales)
        if not res:
            return None, msj
        # Validar que 'frmt_tiempo' sea del tipo str
        res, msj = Validaciones.es_tipo(frmt_tiempo, str, credenciales)
        if not res:
            return None, msj
        # Validar que 'frmt_tiempo' esté compuesto de 3 elementos al hacer split
        res, msj = Validaciones.es_len_correcto(frmt_tiempo.split(":"), 3, credenciales)
        if not res:
            return None, msj
        # Intenta calcular los milisegundos
        try:
            inicio: datetime = datetime.strptime(inicio, frmt_tiempo)
            fin: datetime = datetime.strptime(fin, frmt_tiempo)
            return (fin - inicio).total_seconds(), None
        except Exception as e:
            mensaje = f"No se calculó el intervalo, problema imprevisto: {e}"
            logger.exception(mensaje)
            return None, "Error tiempo"

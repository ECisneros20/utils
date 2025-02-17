import logging
import os
import shutil

from .log import setup_logging
from .validaciones import Validaciones

# Configura el logging
setup_logging()
# Obtiene un logger para este módulo
logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class Carpeta:
    """Una clase que contiene métodos para crear y borrar carpetas indicando la ruta
    absoluta
    """

    @staticmethod
    def borrar_carpeta(ruta_carpeta: str, credenciales: dict = {}) -> tuple[str, str]:
        """Elimina la carpeta

        Args:
            ruta_carpeta (str): Ruta a borrar, debe ser absoluta
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[str, str]: Ruta de la carpeta borrada y mensaje de error
        """
        # Validar que 'ruta_carpeta' sea absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_carpeta, credenciales)
        if not res:
            return None, msj
        # Validar que 'ruta_carpeta' exista
        res, msj = Validaciones.existe_carpeta(ruta_carpeta, credenciales)
        if not res:
            return ruta_carpeta, msj
        # Intenta borrar la carpeta
        try:
            shutil.rmtree(ruta_carpeta)
            mensaje = f"Carpeta borrada: {ruta_carpeta}"
            logger.info(mensaje)
            return ruta_carpeta, None
        except OSError as e:
            mensaje = f"Un archivo está abierto dentro de {ruta_carpeta}: {e}"
            logger.exception(mensaje)
            return None, "Error carpeta"
        except Exception as e:
            mensaje = f"No se borró la carpeta {ruta_carpeta}, problema imprevisto: {e}"
            logger.exception(mensaje)
            return None, "Error carpeta"

    @staticmethod
    def crear_carpeta(ruta_carpeta: str, credenciales: dict = {}) -> tuple[str, str]:
        """Crea la carpeta

        Args:
            ruta_carpeta (str): Ruta a crear, debe ser absoluta
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[str, str]: Ruta de la carpeta creada y mensaje de error
        """
        # Validar que 'ruta_carpeta' sea absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_carpeta, credenciales)
        if not res:
            return None, msj
        # Intenta crear la carpeta
        try:
            os.makedirs(ruta_carpeta, exist_ok=True)
            mensaje = f"Carpeta creada: {ruta_carpeta}"
            logger.info(mensaje)
            return ruta_carpeta, None
        except OSError as e:
            mensaje = f"Un archivo está abierto dentro de {ruta_carpeta}: {e}"
            logger.exception(mensaje)
            return None, "Error carpeta"
        except Exception as e:
            mensaje = f"No se creó la carpeta {ruta_carpeta}, problema imprevisto: {e}"
            logger.exception(mensaje)
            return None, "Error carpeta"

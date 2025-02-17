import logging
import os
import re
from collections.abc import Iterable
from typing import Any

from .log import setup_logging

# Configura el logging
setup_logging()
# Obtiene un logger para este módulo
logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class Validaciones:
    """Una clase que contiene métodos para validar tipos de variables, archivos,
    carpetas, etc
    """

    @staticmethod
    def es_tipo(
        var: Any, tipo_esperado: type, credenciales: dict = {}
    ) -> tuple[bool, str]:
        """Valida si la variable es del tipo esperado

        Args:
            var (Any): Variable a validar
            tipo_esperado (type): Tipo de dato que se espera
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[bool, str]: Es o no el tipo de variable esperado y mensaje de error
        """
        # Validar que 'tipo_esperado' sea del tipo type
        if not isinstance(tipo_esperado, type):
            mensaje = f"El `tipo_esperado` no es {type}, sino {type(tipo_esperado)}"
            logger.error(mensaje)
            return False, "Error validaciones"
        # Validar que 'var' sea del 'tipo_esperado'
        if not isinstance(var, tipo_esperado):
            mensaje = f"La `var` no es {tipo_esperado}, sino {type(var)}"
            logger.error(mensaje)
            return False, "Error validaciones"
        return True, None

    @staticmethod
    def es_tipos(
        var: Any, tipos_esperados: Iterable[type], credenciales: dict = {}
    ) -> tuple[bool, str]:
        """Valida si la variable es de alguno de los tipos esperados

        Args:
            var (Any): Variable a validar
            tipos_esperados (Iterable[type]): Tipos de datos que se espera
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[bool, str]: Es o no de alguno de los tipos de variables esperados y
            mensaje de error
        """
        # Validar que 'tipos_esperados' sea del tipo Iterable
        res, msj = Validaciones.es_tipo(tipos_esperados, Iterable, credenciales)
        if not res:
            return False, msj
        # Validar que 'var' sea de alguno de los 'tipos_esperados'
        for tipo_esperado in tipos_esperados:
            res, _ = Validaciones.es_tipo(var, tipo_esperado, credenciales)
            if res:
                return True, None
        mensaje = f"La `var` no es ninguno de {tipos_esperados}, sino {type(var)}"
        logger.error(mensaje)
        return False, "Error validaciones"

    @staticmethod
    def es_len_correcto(
        var: Iterable[Any], len_esperado: int, credenciales: dict = {}
    ) -> tuple[bool, str]:
        """Valida si la longitud del iterable es la esperada

        Args:
            var (Iterable[Any]): Variable a validar
            len_esperado (int): Longitud esperada
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[bool, str]: Tiene o no la longitud esperada y mensaje de error
        """
        # Validar que 'var' sea del tipo Iterable
        res, msj = Validaciones.es_tipo(var, Iterable, credenciales)
        if not res:
            return False, msj
        # Validar que 'len_esperado' sea del tipo int
        res, msj = Validaciones.es_tipo(len_esperado, int, credenciales)
        if not res:
            return False, msj
        # Validar que 'var' tenga el 'len_esperado'
        if len(var) != len_esperado:
            mensaje = f"Se esperaba {len_esperado} elementos, en vez de {len(var)}"
            logger.error(mensaje)
            return False, "Error validaciones"
        return True, None

    @staticmethod
    def es_formato_expediente(
        num_expediente: str, credenciales: dict = {}
    ) -> tuple[bool, str]:
        """Valida si el número de expediente tiene el formato adecuado

        Args:
            num_expediente (str): Variable a validar
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[bool, str]: Tiene o no el formato del expediente y mensaje de error
        """
        # Validar que 'num_expediente' sea del tipo str
        res, msj = Validaciones.es_tipo(num_expediente, str, credenciales)
        if not res:
            return False, msj
        # Validar que 'num_expediente' tenga el formato de expediente
        formato = re.compile(r"^\d{5}-\d{4}-\d-\d{4}-\w{2}-\w{2}-\d{2}$")
        if formato.match(num_expediente) is None:
            mensaje = f"Formato de expediente no identificado: {num_expediente}"
            logger.error(mensaje)
            return False, "Error validaciones"
        return True, None

    @staticmethod
    def es_ruta_absoluta(ruta: str, credenciales: dict = {}) -> tuple[bool, str]:
        """Valida si la ruta es de tipo absoluta

        Args:
            ruta (str): Variable a validar
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[bool, str]: Es o no una ruta absoluta y mensaje de error
        """
        # Validar que 'ruta' sea del tipo str
        res, msj = Validaciones.es_tipo(ruta, str, credenciales)
        if not res:
            return False, msj
        # Validar que 'ruta' sea ruta absoluta
        if not os.path.isabs(ruta):
            mensaje = f"La ruta no es absoluta: {ruta}"
            logger.error(mensaje)
            return False, "Error validaciones"
        return True, None

    @staticmethod
    def es_tipo_archivo(
        ruta_archivo: str, tipo_esperado: str, credenciales: dict = {}
    ) -> tuple[bool, str]:
        """Valida si la ruta del archivo es del tipo esperado

        Args:
            ruta_archivo (str): Variable a validar
            tipo_esperado (str): Tipo de archivo que se espera
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[bool, str]: Es o no el tipo de archivo esperado y mensaje de error
        """
        # Validar que 'ruta_archivo' sea ruta absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_archivo, credenciales)
        if not res:
            return False, msj
        # Validar que 'tipo_esperado' sea del tipo str
        res, msj = Validaciones.es_tipo(tipo_esperado, str, credenciales)
        if not res:
            return False, msj
        # Validar que 'ruta archivo' sea del 'tipo_esperado'
        if not ruta_archivo.endswith(tipo_esperado):
            mensaje = f"El archivo no es {tipo_esperado}: {ruta_archivo}"
            logger.error(mensaje)
            return False, "Error validaciones"
        return True, None

    @staticmethod
    def es_tipos_archivos(
        ruta_archivo: str, tipos_esperados: Iterable[str], credenciales: dict = {}
    ) -> tuple[bool, str]:
        """Valida si la ruta del archivo es de alguno de los tipos esperados

        Args:
            ruta_archivo (str): Variable a validar
            tipos_esperados (Iterable[str]): Tipos de archivos que se espera
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[bool, str]: Es o no de alguno de los tipos de archivos esperados y
            mensaje de error
        """
        # Validar que 'ruta_archivo' sea ruta absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_archivo, credenciales)
        if not res:
            return False, msj
        # Validar que 'tipos_esperados' sea del tipo Iterable
        res, msj = Validaciones.es_tipo(tipos_esperados, Iterable, credenciales)
        if not res:
            return False, msj
        # Validar que 'ruta_archivo' sea de alguno de los 'tipos_esperados'
        for tp_espera in tipos_esperados:
            res, _ = Validaciones.es_tipo_archivo(ruta_archivo, tp_espera, credenciales)
            if res:
                return True, None
        mensaje = f"El archivo no es ninguno de {tipos_esperados}: {ruta_archivo}"
        logger.error(mensaje)
        return False, "Error validaciones"

    @staticmethod
    def existe_ruta(ruta: str, credenciales: dict = {}) -> tuple[bool, str]:
        """Valida si la ruta existe

        Args:
            ruta (str): Variable a validar
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[bool, str]: Existe o no la ruta y mensaje de error
        """
        # Validar que 'ruta' sea ruta absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta, credenciales)
        if not res:
            return False, msj
        # Validar que 'ruta' exista
        if not os.path.exists(ruta):
            mensaje = f"El archivo no existe: {ruta}"
            logger.error(mensaje)
            return False, "Error validaciones"
        return True, None

    @staticmethod
    def existe_archivo(ruta_archivo: str, credenciales: dict = {}) -> tuple[bool, str]:
        """Valida si la ruta del archivo existe y es un archivo

        Args:
            ruta_archivo (str): Variable a validar
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[bool, str]: Existe y es un archivo y mensaje de error
        """
        # Validar que 'ruta_archivo' sea ruta absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_archivo, credenciales)
        if not res:
            return False, msj
        # Validar que 'ruta_archivo' exista
        res, msj = Validaciones.existe_ruta(ruta_archivo, credenciales)
        if not res:
            return False, msj
        # Validar que 'ruta_archivo' sea un archivo
        if not os.path.isfile(ruta_archivo):
            mensaje = f"No es un archivo: {ruta_archivo}"
            logger.error(mensaje)
            return False, "Error validaciones"
        return True, None

    @staticmethod
    def existe_carpeta(ruta_carpeta: str, credenciales: dict = {}) -> tuple[bool, str]:
        """Valida si la ruta de la carpeta existe y es una carpeta

        Args:
            ruta_carpeta (str): Variable a validar
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[bool, str]: Existe y es una carpeta y mensaje de error
        """
        # Validar que 'ruta_carpeta' sea ruta absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_carpeta, credenciales)
        if not res:
            return False, msj
        # Validar que 'ruta_carpeta' exista
        res, msj = Validaciones.existe_ruta(ruta_carpeta, credenciales)
        if not res:
            return False, msj
        # Validar que 'ruta_carpeta' sea una carpeta
        if not os.path.isdir(ruta_carpeta):
            mensaje = f"No es una carpeta: {ruta_carpeta}"
            logger.error(mensaje)
            return False, "Error validaciones"
        return True, None

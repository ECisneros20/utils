import logging
import os
from typing import Any

import pandas as pd
from docxtpl import DocxTemplate

from .constantes import Constantes
from .log import setup_logging
from .validaciones import Validaciones

# Configura el logging
setup_logging()
# Obtiene un logger para este módulo
logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class Archivo:
    """Una clase que contiene métodos para crear y actualizar archivo csv y txt, crear
    archivos docx, y borrar archivos en general
    """

    @staticmethod
    def borrar_archivo(ruta_archivo: str, credenciales: dict = {}) -> tuple[str, str]:
        """Elimina el archivo

        Args:
            ruta_archivo (str): Ruta a borrar, debe ser absoluta
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[str, str]: Ruta del archivo borrado y mensaje de error
        """
        # Validar que 'ruta_archivo' sea absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_archivo, credenciales)
        if not res:
            return None, msj
        # Validar que 'ruta_archivo' exista
        res, msj = Validaciones.existe_archivo(ruta_archivo, credenciales)
        if not res:
            return ruta_archivo, msj
        # Intentar borrar el archivo
        try:
            os.remove(ruta_archivo)
            mensaje = f"Archivo eliminado: {ruta_archivo}"
            logger.info(mensaje)
            return ruta_archivo, None
        except OSError as e:
            mensaje = f"El archivo está abierto: {ruta_archivo}: {e}"
            logger.exception(mensaje)
            return None, "Error archivo"
        except Exception as e:
            mensaje = f"No se borró el archivo {ruta_archivo}, problema imprevisto: {e}"
            logger.exception(mensaje)
            return None, "Error archivo"

    @staticmethod
    def crear_csv(
        ruta_csv: str,
        filas: list[list[Any]],
        columnas: list[Any],
        credenciales: dict = {},
    ) -> tuple[str, str]:
        """Crea el archivo csv en la ruta indicada

        Args:
            ruta_csv (str): Ruta a crear, debe ser absoluta
            filas (list[list[Any]]): Los datos a agregar en el csv
            columnas (list[Any]): Nombres de las columnas del csv
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[str, str]: Ruta del csv y mensaje de error
        """
        # Validar que 'ruta_csv' sea absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_csv, credenciales)
        if not res:
            return None, msj
        # Validar que 'ruta_csv' sea del tipo csv
        res, msj = Validaciones.es_tipo_archivo(ruta_csv, ".csv", credenciales)
        if not res:
            return None, msj
        # Validar que la carpeta donde estará 'ruta_csv' exista
        res, msj = Validaciones.existe_carpeta(os.path.dirname(ruta_csv), credenciales)
        if not res:
            return None, msj
        # Validar que 'filas' sea del tipo list
        res, msj = Validaciones.es_tipo(filas, list, credenciales)
        if not res:
            return None, msj
        # Validar que 'columnas' sea del tipo list
        res, msj = Validaciones.es_tipo(columnas, list, credenciales)
        if not res:
            return None, msj
        len_values = -1
        for lista in filas:
            # Validar que cada componente sea una lista y tenga la misma longitud
            res, msj = Validaciones.es_tipo(lista, list, credenciales)
            if not res:
                return None, msj
            if len_values == -1:
                len_values = len(lista)
            else:
                # Validar que cada componente tenga el mismo len
                res, msj = Validaciones.es_len_correcto(lista, len_values, credenciales)
                if not res:
                    return None, msj
        # Validar que 'columnas' tenga el mismo len que cada lista de filas
        res, msj = Validaciones.es_len_correcto(columnas, len_values)
        if not res:
            return None, msj
        # Intenta crear el csv
        try:
            # Se crea un df a partir de la información de entrada
            df = pd.DataFrame(filas, columnas)
            # Se guarda el csv en la ruta definida
            df.to_csv(ruta_csv, index=False, encoding=Constantes.encoding.value)
            return ruta_csv, None
        except Exception as e:
            mensaje = f"Error al operar con el df, problema imprevisto: {e}"
            logger.exception(mensaje)
            return None, "Error archivo"

    @staticmethod
    def actualizar_csv(
        ruta_csv: str,
        filas: list[list[Any]],
        columnas: list[Any],
        credenciales: dict = {},
    ) -> tuple[str, str]:
        """Actualiza el archivo csv en la ruta indicada

        Args:
            ruta_csv (str): Ruta a actualizar, debe ser absoluta
            filas (list[list[Any]]): Los datos a agregar en el csv
            columnas (list[Any]): Nombres de las columnas del csv
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[str, str]: Ruta del csv y mensaje de error
        """
        # Validar que 'ruta_csv' sea absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_csv, credenciales)
        if not res:
            return None, msj
        # Validar que 'ruta_csv' sea del tipo csv
        res, msj = Validaciones.es_tipo_archivo(ruta_csv, ".csv", credenciales)
        if not res:
            return None, msj
        # Validar que el archivo en 'ruta_csv' exista
        res, msj = Validaciones.existe_archivo(ruta_csv, credenciales)
        if not res:
            # Si no existe, intenta crear el csv con la función anterior
            res, msj = Archivo.crear_csv(ruta_csv, filas, columnas, credenciales)
            return res, msj
        # Como el archivo en 'ruta_csv' existe, intenta cargarse como df
        try:
            df = pd.read_csv(ruta_csv, encoding=Constantes.encoding.value)
        except Exception as e:
            mensaje = f"No se cargó el csv como df, problema imprevisto: {e}"
            logger.exception(mensaje)
            return None, "Error archivo"
        # Validar que 'filas' sea del tipo list
        res, msj = Validaciones.es_tipo(filas, list, credenciales)
        if not res:
            return None, msj
        # Validar que 'columnas' sea del tipo list
        res, msj = Validaciones.es_tipo(columnas, list, credenciales)
        if not res:
            return None, msj
        len_values = -1
        for lst in filas:
            # Validar que cada componente sea una lista y tenga la misma longitud
            res, msj = Validaciones.es_tipo(lst, list, credenciales)
            if not res:
                return None, msj
            if len_values == -1:
                len_values = len(lst)
            else:
                # Validar que cada componente tenga el mismo len
                res, msj = Validaciones.es_len_correcto(lst, len_values, credenciales)
                if not res:
                    return None, msj
        # Validar que 'columnas' tenga el mismo len que cada lista de filas
        res, msj = Validaciones.es_len_correcto(columnas, len_values)
        if not res:
            return None, msj
        # Validar que las columnas del csv estén incluidas en las nuevas columnas
        if set(df.columns.tolist()).issubset(set(columnas)):
            mensaje = f"Las columnas del csv se incluyen en: {columnas}"
            logger.info(mensaje)
        else:
            mensaje = f"Las columnas del csv no se incluyen en: {columnas}"
            logger.error(mensaje)
            return None, "Error archivo"
        # Intenta actulizar el csv
        try:
            # Se crea un df_aux a partir de la información de entrada
            df_aux = pd.DataFrame(filas, columnas)
            # Se concatenan las nuevas filas
            df = pd.concat([df, df_aux])
            # Se guarda el csv en la ruta definida
            df.to_csv(ruta_csv, index=False, encoding=Constantes.encoding.value)
            return ruta_csv, None
        except Exception as e:
            mensaje = f"Error al operar con los df, problema imprevisto: {e}"
            logger.exception(mensaje)
            return None, "Error archivo"

    @staticmethod
    def crear_txt(
        ruta_txt: str, texto: str, credenciales: dict = {}
    ) -> tuple[str, str]:
        """Crea el archivo de texto en la ruta indicada

        Args:
            ruta_txt (str): Ruta a crear, debe ser absoluta
            texto (str): Los datos a agregar en el archivo de texto
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[str, str]: Ruta del archivo de texto y mensaje de error
        """
        # Validar que 'ruta_txt' sea absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_txt, credenciales)
        if not res:
            return None, msj
        # Validar que 'ruta_txt' sea del tipo txt
        res, msj = Validaciones.es_tipo_archivo(ruta_txt, ".txt", credenciales)
        if not res:
            return None, msj
        # Validar que la carpeta donde estará 'ruta_txt' exista
        res, msj = Validaciones.existe_carpeta(os.path.dirname(ruta_txt), credenciales)
        if not res:
            return None, msj
        # Validar que 'texto' sea del tipo str
        res, msj = Validaciones.es_tipo(texto, str, credenciales)
        if not res:
            return None, msj
        # Intenta crear el txt
        try:
            # Abrir el archivo en modo escribir ('w')
            with open(ruta_txt, "w", encoding=Constantes.encoding.value) as f:
                # Escribir un nuevo archivo
                f.write(texto)
            return ruta_txt, None
        except Exception as e:
            mensaje = f"Error al escribir en {ruta_txt}, problema imprevisto: {e}"
            logger.exception(mensaje)
            return None, "Error archivo"

    @staticmethod
    def actualizar_txt(
        ruta_txt: str, texto: str, credenciales: dict = {}
    ) -> tuple[str, str]:
        """Actualiza el archivo de texto en la ruta indicada

        Args:
            ruta_txt (str): Ruta a actualizar, debe ser absoluta
            texto (str): Los datos a agregar en el archivo de texto
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[str, str]: Ruta del archivo de texto y mensaje de error
        """
        # Validar que 'ruta_txt' sea absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_txt, credenciales)
        if not res:
            return None, msj
        # Validar que 'ruta_txt' sea del tipo txt
        res, msj = Validaciones.es_tipo_archivo(ruta_txt, ".txt", credenciales)
        if not res:
            return None, msj
        # Validar que la carpeta donde estará 'ruta_txt' exista
        res, msj = Validaciones.existe_carpeta(os.path.dirname(ruta_txt), credenciales)
        if not res:
            return None, msj
        # Validar que 'texto' sea del tipo str
        res, msj = Validaciones.es_tipo(texto, str, credenciales)
        if not res:
            return None, msj
        # Intenta actualizar el csv
        try:
            # Abrir el archivo en modo añadir ('a')
            with open(ruta_txt, "a", encoding=Constantes.encoding.value) as f:
                # Escribir nuevas líneas al final del archivo
                f.write(texto)
            return ruta_txt, None
        except Exception as e:
            mensaje = f"Error al escribir en {ruta_txt}, problema imprevisto: {e}"
            logger.exception(mensaje)
            return None, "Error archivo"

    @staticmethod
    def crear_docx(
        ruta_docx: str,
        ruta_plantilla: str,
        datos: list[str],
        credenciales: dict = {},
    ) -> tuple[str, str]:
        """Crea el archivo docx en la ruta indicada

        Args:
            ruta_docx (str): Ruta a crear, debe ser absoluta
            ruta_plantilla (str): Ruta de la plantilla base, debe ser absoluta
            datos (list[str]): Valores a agregar en el archivo docx
            credenciales (dict): Datos a registrar en el log

        Returns:
            tuple[str, str]: Ruta del docx y mensaje de error
        """
        # Validar que 'ruta_docx' sea absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_docx, credenciales)
        if not res:
            return None, msj
        # Validar que 'ruta_docx' sea del tipo docx
        res, msj = Validaciones.es_tipo_archivo(ruta_docx, ".docx", credenciales)
        if not res:
            return None, msj
        # Validar que la carpeta donde estará 'ruta_docx' exista
        res, msj = Validaciones.existe_carpeta(os.path.dirname(ruta_docx), credenciales)
        if not res:
            return None, msj
        # Validar que 'ruta_plantilla' sea absoluta
        res, msj = Validaciones.es_ruta_absoluta(ruta_plantilla, credenciales)
        if not res:
            return None, msj
        # Validar que 'ruta_plantilla' sea del tipo docx
        res, msj = Validaciones.es_tipo_archivo(ruta_plantilla, ".docx", credenciales)
        if not res:
            return None, msj
        # Validar que el archivo en 'ruta_plantilla' exista
        res, msj = Validaciones.existe_archivo(ruta_plantilla, credenciales)
        if not res:
            return None, msj
        # Validar que 'datos' sea del tipo list
        res, msj = Validaciones.es_tipo(datos, list, credenciales)
        if not res:
            return None, msj
        # Intenta crear el docx. Cargar los datos recolectados en las variables de la
        # plantilla. Se asume que la cantidad de espacios en la plantilla elegida es
        # igual al de 'datos'
        try:
            # Cargar plantilla de archivo de salida
            doc = DocxTemplate(ruta_plantilla)
            context = {}
            for pos, dato in enumerate(datos):
                # Validar que cada componente sea del tipo str
                res, msj = Validaciones.es_tipo(dato, str, credenciales)
                if res:
                    context[f"p{pos}"] = dato
            # Reemplazar los contenidos de las variables de la plantilla
            doc.render(context)
            # Guardar los resultados en un archivo de salida
            doc.save(ruta_docx)
            return ruta_docx, None
        except PermissionError as e:
            mensaje = f"El archivo docx o la plantilla están abiertos: {e}"
            logger.exception(mensaje)
            return None, "Error archivo"
        except Exception as e:
            mensaje = f"No se generó el archivo docx, problema imprevisto: {e}"
            logger.exception(mensaje)
            return None, "Error archivo"

import configparser
import os
from enum import Enum, unique


@unique
class Constantes(Enum):
    """Una clase que contiene constantes base del sistema, así como la ruta principal y
    de los subdirectorios del proyecto para desarrollo y producción.
    """

    # Encoding para editar y crear archivos txt y csv
    encoding = "utf-8"
    # Ruta principal del proyecto
    ruta_principal = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    ).replace("\\", "/")
    # Rutas de proyecto back-end
    ruta_data = f"{ruta_principal}/data"
    ruta_log = f"{ruta_principal}/log"
    ruta_models = f"{ruta_principal}/models"
    ruta_reports = f"{ruta_principal}/reports"
    ruta_src = f"{ruta_principal}/src"
    ruta_tests = f"{ruta_principal}/tests"
    ruta_tmp = f"{ruta_principal}/tmp"

    # Cargar config.ini
    config = configparser.ConfigParser()
    config.read("config.ini")

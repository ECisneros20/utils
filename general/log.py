import logging

from .constantes import Constantes


def setup_logging() -> None:
    """Setea el mensaje de logging para todos los scripts del utils y también del
    proyecto
    """
    # Ruta del archivo log
    archivo_log = f"{Constantes.ruta_log.value}/app.log"
    # Configuración del logger
    logging.basicConfig(
        format="%(asctime)s *|* %(name)s *|* %(levelname)s *|* %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
        handlers=[
            logging.FileHandler(
                filename=archivo_log, mode="a", encoding=Constantes.encoding.value
            )
        ],
    )

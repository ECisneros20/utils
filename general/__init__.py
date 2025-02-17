# Copyright 2025 Enzo Cisneros Collazos. All rights reserved.

# This is used to defer the actual importing for when the objects are requested. This
# way `import utils` provides the names in the namespace without actually importing
# anything (and especially none of the back-ends).

# Este archivo se utiliza para aplazar la importación real para cuando se soliciten los
# objetos. De esta forma `import utils` proporciona los nombres sin importar ninguno de
# los back-ends.

from .archivo import Archivo
from .carpeta import Carpeta
from .constantes import Constantes
from .log import setup_logging
from .tiempo import Tiempo
from .validaciones import Validaciones

__all__ = [
    Archivo,
    Carpeta,
    Constantes,
    setup_logging,
    Tiempo,
    Validaciones,
]

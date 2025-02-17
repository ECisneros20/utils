# utils

# 1. Descripción del proyecto

Se entrega el proyecto utils con lo siguiente:

<table border="1">
    <tr>
        <th>Carpeta / Archivo</th>
        <th>Ejemplos</th>
        <th>Descripción</th>
    </tr>
    <tr>
        <td>docs/</td>
        <td>...</td>
        <td>documentación de las clases y métodos</td>
    </tr>
    <tr>
        <td>general/</td>
        <td>...</td>
        <td>paquete principal con utilidades a reutilizar en todos los proyectos</td>
    </tr>
    <tr>
        <td>__init__.py</td>
        <td>-</td>
        <td>permite estructurar las clases y métodos para su importación en proyectos back-end</td>
    </tr>
    <tr>
        <td>.gitignore</td>
        <td>-</td>
        <td>permite ignorar archivos al actualizar el repo en git</td>
    </tr>
    <tr>
        <td>CHANGELOG.rst</td>
        <td>-</td>
        <td>muestra un registro de cambios manual al actualizar el repo en git</td>
    </tr>
    <tr>
        <td>README.md</td>
        <td>-</td>
        <td>pasos para setear el proyecto y la carpeta de documentación docs</td>
    </tr>
    <tr>
        <td>requirements_app.txt</td>
        <td>-</td>
        <td>librerías a instalar para despliegue back-end</td>
    </tr>
    <tr>
        <td>requirements_general1.txt</td>
        <td>-</td>
        <td>librerías suplementarias</td>
    </tr>
    <tr>
        <td>requirements_general2.txt</td>
        <td>-</td>
        <td>librerías a instalar para validaciones básicas</td>
    </tr>
    <tr>
        <td>requirements_general3.txt</td>
        <td>-</td>
        <td>librerías pytorch y dependencias para GPU desde otra fuente</td>
    </tr>
    <tr>
        <td>requirements.bat</td>
        <td>-</td>
        <td>automatiza la creación de venv e instalación de librerías</td>
    </tr>
    <tr>
        <td>setear_docs.bat</td>
        <td>-</td>
        <td>automatiza parcialmente la creación de la documentación</td>
    </tr>
</table>

Adicionalmente, se entrega la parte principal del codebase con lo siguiente:

<table class="codebase" border="1">
    <tr>
        <th>Paquete</th>
        <th>Script</th>
        <th>Clase</th>
        <th>Métodos</th>
    </tr>
    <tr>
        <td rowspan="7">general</td>
        <td>__init.py__</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>archivo.py</td>
        <td>Archivo</td>
        <td>
            borrar_archivo</br>
            crear_csv</br>
            actualizar_csv</br>
            crear_txt</br>
            actualizar_txt</br>
            crear_docx</br>
        </td>
    </tr>
    <tr>
        <td>carpeta.py</td>
        <td>Carpeta</td>
        <td>
            borrar_carpeta</br>
            crear_carpeta</br>
        </td>
    </tr>
    <tr>
        <td>constantes.py</td>
        <td>Constantes</td>
        <td>-</td>
    </tr>
    <tr>
        <td>log.py</td>
        <td>-</td>
        <td>
            setup_logging</br>
        </td>
    </tr>
    <tr>
        <td>tiempo.py</td>
        <td>Tiempo</td>
        <td>
            marca_a_ms</br>
            calcular_intervalo</br>
        </td>
    </tr>
    <tr>
        <td>validaciones.py</td>
        <td>Validaciones</td>
        <td>
            es_tipo</br>
            es_tipos</br>
            es_len_correcto</br>
            es_formato_expediente</br>
            es_ruta_absoluta</br>
            es_tipo_archivo</br>
            es_tipos_archivos</br>
            existe_ruta</br>
            existe_archivo</br>
            existe_carpeta</br>
        </td>
    </tr>
</table>

# 2. Realizar cambios al codebase

Si se quieren hacer cambios en la estructura de este codebase, colocar el siguiente comando (asegurarse de crear un token y tener acceso al repo privado). No hay más pasos:
```bash
git clone -b develop https://<token>@github.com/ECisneros20/utils.git
```

# 3. Utilizar el codebase para un nuevo proyecto (tiene que estar dentro de un proyecto back-end o microservicio)

Si se quiere emplear el codebase para un nuevo proyecto, colocar el siguiente comando (asegurarse de crear un token y tener acceso al repo privado):
```bash
git clone https://<token>@github.com/ECisneros20/utils.git
```

# 4. Setear entorno de trabajo

## Ejecutar el archivo .bat

Crea el entorno virtual e instala las librerías base:
```bash
requirements.bat
```

# 5. Autogenerar la documentación

## Ejecutar el archivo .bat, el cual borrará la carpeta docs actual:

Hay partes que se deben hacer manual antes de terminar de ejecutar el archivo: 
```bash
setear_docs.bat
```

## [Manual 1] Responder al inicializador:

- Separate source and build directories (y/n) [n]: n
- Project name: Documentación de utils
- Author name(s): Enzo Cisneros
- Project release []: 0.1.0
- Project language [en]: es

## [Manual 2] Editar el archivo conf.py de la carpeta docs

- Agregar al inicio:
```bash
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
```

- Reemplazar extensions:
```bash
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]
```

- Reemplazar html_theme:
```bash
html_theme = 'sphinx_rtd_theme'
```

## [Manual 3] Editar el archivo index.rst de la carpeta docs

- Agregar después de caption: Contents:
```bash
   :caption: Contents:

   modules
```
- Al terminar, ignorar los warnings

## [Manual 4] Revisar documentación

- Cortar la carpeta "html" desde "docs\\_build\html" hacia "docs"
- Borrar todo lo que no pertenezca a esta nueva carpeta
- Cortar el interior de la carpeta "html"
- Borrar la carpeta vacía "html"

## [Manual 5] Revisar documentación

- Abrir archivo index.html

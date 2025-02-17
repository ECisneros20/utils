@echo off
REM Define la ruta del entorno virtual
set VENV_DIR=..\venv

REM Activa el entorno virtual
call %VENV_DIR%\Scripts\activate.bat

REM Crear y acceder a la carpeta docs; si la carpeta existe, primero la borra
rmdir /s /q ".\docs"
mkdir docs
cd docs

REM Inicializar Sphinx
echo [Manual 1] Complete los datos que indica el README.md
pause
sphinx-quickstart

REM Agregar los scripts creados a Sphinx
cd ..
sphinx-apidoc -o docs .
echo [Manual 2] Edite el archivo conf.py de la carpeta docs
echo [Manual 3] Edite el archivo index.rst de la carpeta docs
pause

REM Generar el index.html
cd docs
call make.bat html

echo Carpeta docs autogenerada.
pause

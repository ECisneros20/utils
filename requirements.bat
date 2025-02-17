@echo off
REM Define la ruta del entorno virtual
set VENV_DIR=..\venv

REM Crea el entorno virtual
call py -3.10 -m venv %VENV_DIR%

REM Activa el entorno virtual
call %VENV_DIR%\Scripts\activate.bat

REM Actualiza la versión del pip
call python.exe -m pip install --upgrade pip

REM Instala los paquetes de los archivos requirements.txt
pip install -r requirements_general1.txt
pip install -r requirements_general2.txt
pip install -r requirements_general3.txt
pip install -r requirements_app.txt

echo Entorno virtual completo.
pause

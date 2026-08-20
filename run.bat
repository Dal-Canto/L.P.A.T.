@echo off
REM Run LPAT using a local venv; creates venv if missing and installs package in editable mode
if not exist venv (
  python -m venv venv
)
call .\venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install pyyaml
if "%1"=="" (
  echo Usage: run.bat templates\60min.detox
  pause
) else (
  python -m lpat %1
)

@echo off
echo Starting AIT CMMS Application...
cd /d "%~dp0"
py -3 AIT_CMMS_REV3.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Python launcher failed. Trying 'python' command...
    python AIT_CMMS_REV3.py
)
pause
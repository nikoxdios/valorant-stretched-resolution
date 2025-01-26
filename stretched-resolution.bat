@echo off
setlocal enabledelayedexpansion

REM Define las rutas principales
set "LOCALAPPDATA=%LOCALAPPDATA%"
set "CONFIG_PATH=%LOCALAPPDATA%\\VALORANT\\Saved\\Config"

REM Verifica si la carpeta de Config existe
if not exist "%CONFIG_PATH%" (
    echo La carpeta de configuracion de VALORANT no existe.
    pause
    exit /b
)

REM Busca la carpeta que coincida con el patrón del ID de usuario
set "USER_DIR="
for /d %%D in ("%CONFIG_PATH%\*-*") do (
    set "USER_DIR=%%~fD"
    REM Salir del bucle al encontrar la primera coincidencia
    goto :FOUND
)

:FOUND
if "%USER_DIR%"=="" (
    echo No se encontro ninguna carpeta con un ID de usuario.
    pause
    exit /b
)

REM Define la ruta al GameUserSettings.ini
set "GAME_SETTINGS=%USER_DIR%\Windows\GameUserSettings.ini"

REM Verifica si GameUserSettings.ini existe
if not exist "!GAME_SETTINGS!" (
    echo GameUserSettings.ini no encontrado en "!USER_DIR!".
    pause
    exit /b
)

REM Pedir la resolución deseada
set /p WIDTH=Introduce el ancho de la pantalla (e.g., 1024): 
set /p HEIGHT=Introduce el alto de la pantalla (e.g., 768): 

REM Actualizar valores en GameUserSettings.ini
(for /f "tokens=1* delims==" %%A in ('type "!GAME_SETTINGS!"') do (
    set "line=%%A=%%B"
    if "%%A"=="ResolutionSizeX" (set "line=ResolutionSizeX=!WIDTH!")
    if "%%A"=="ResolutionSizeY" (set "line=ResolutionSizeY=!HEIGHT!")
    if "%%A"=="LastUserConfirmedResolutionSizeX" (set "line=LastUserConfirmedResolutionSizeX=!WIDTH!")
    if "%%A"=="LastUserConfirmedResolutionSizeY" (set "line=LastUserConfirmedResolutionSizeY=!HEIGHT!")
    if "%%A"=="DesiredScreenWidth" (set "line=DesiredScreenWidth=!WIDTH!")
    if "%%A"=="DesiredScreenHeight" (set "line=DesiredScreenHeight=!HEIGHT!")
    if "%%A"=="LastUserConfirmedDesiredScreenWidth" (set "line=LastUserConfirmedDesiredScreenWidth=!WIDTH!")
    if "%%A"=="LastUserConfirmedDesiredScreenHeight" (set "line=LastUserConfirmedDesiredScreenHeight=!HEIGHT!")
    if "%%A"=="bShouldLetterbox" (set "line=bShouldLetterbox=False")
    if "%%A"=="bLastConfirmedShouldLetterbox" (set "line=bLastConfirmedShouldLetterbox=False")
    if "%%A"=="FullscreenMode" (set "line=FullscreenMode=2")
    if "%%A"=="LastConfirmedFullscreenMode" (set "line=LastConfirmedFullscreenMode=2")
    if "%%A"=="PreferredFullscreenMode" (set "line=PreferredFullscreenMode=2")
    echo !line!
)) > "!GAME_SETTINGS!.tmp"

REM Reemplazar el archivo original
move /y "!GAME_SETTINGS!.tmp" "!GAME_SETTINGS!" >nul

echo Resolución actualizada exitosamente a %WIDTH%x%HEIGHT% en GameUserSettings.ini.
pause

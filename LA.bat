@echo off

setlocal EnableExtensions EnableDelayedExpansion

set ROOT_DIR=%~dp0

set "ARG1=%1"
set "ARG2=%2"

IF "%ARG2%" == "-s3d" (
    py -3 "%ROOT_DIR%\src\linearAdvance.py" %1 %2 > %ROOT_DIR%\log.txt 2>&1
) ELSE IF "%ARG1%" == "-ps" (
    py -3 "%ROOT_DIR%\src\linearAdvance.py" %2 %1 > %ROOT_DIR%\log.txt 2>&1
) ELSE (
    echo "Error in argument of type of slicer" %1 %2> %ROOT_DIR%\log.txt 2>&1
)

rem C:\Users\User\Desktop\3D\Profiles\Scripts\LA.bat -ps;
rem C:\Users\User\Desktop\3D\Profiles\Scripts\LA.bat [output_filepath] -s3d
@echo off

setlocal EnableExtensions EnableDelayedExpansion

set ROOT_DIR=%~dp0

rem Wrapper script for starting filaswitch. Needed in order to support
rem Slic3r automatic post-processing as Slic3r always puts the file path
rem after all commans -> default argument ordering doesn't work

rem switch file and hwconfig argument order

set "ARG1=%1"
set "ARG2=%2"

IF "%ARG2%" == "-s3d" (
    py -3 "%ROOT_DIR%\LAsimplify3D.py" %1 %2 > %ROOT_DIR%\log.txt 2>&1
) ELSE IF "%ARG1%" == "-ps" (
    py -3 "%ROOT_DIR%\LAsimplify3D.py" %2 %1 > %ROOT_DIR%\log.txt 2>&1
) ELSE (
    echo "Error in argument of type of slicer" %1 %2> %ROOT_DIR%\log.txt 2>&1
)

rem C:\Users\User\Desktop\3D\Profiles\Scripts\LA.bat -ps;
rem C:\Users\User\Desktop\3D\Profiles\Scripts\LA.bat [output_filepath] -s3d
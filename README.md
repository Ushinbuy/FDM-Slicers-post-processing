# FDM Slicers post processing
This repository contain FDM Slicers GCODE post processing. This script change file `.gcode` after slicer save them. 
This script require **python 3 version**.

## Linear Advanced

### Description
Script add Linear Advanced (or Pressure Advanced) on wall and disable this for inner parts. 

### How to use in Simplify3D
1. On "Starting Script" add 

`; LA value M572 D0 S0.08`

, where `M572 D0` - Linear Advance command for youre printer system. In RRF it is `M572 D0`, for Marlin it is `M900`, for Repitier it is `TODO()`. The `S0.08` is the value of Linaear Advance.

2. In "Adittional terminal commands for post processing" add 

`/Users/user/Scripts/LA.sh [output_filepath] -s3d`

, where `/Users/user/Scripts/LA.sh` - directory of this script (on Mac and Linux `LA.sh`, for Windows `LA.bat`). The picture bellow show this as example. 

<img src = pictures/LA_S3D.png>

### How to use in PrusaSlicer

1. In "Filament Setting -> Custom G-Code -> Start G-code" add 

`; LA value M572 D0 S0.08`

, where `M572 D0` - Linear Advance command for youre printer system. In RRF it is `M572 D0`, for Marlin it is `M900`, for Repitier it is `TODO()`. The `S0.08` is the value of Linaear Advance.

<img src = pictures/LA_PS_01.png>

2. In "Print Settings -> Output oprions -> Post-processing scripts" add

`/Users/user/Scripts/LA.sh -ps;`

, where `/Users/user/Scripts/LA.sh` - directory of this script (on Mac and Linux `LA.sh`, for Windows `LA.bat`). The picture bellow show this as example. 

<img src = pictures/LA_PS_02.png>

## Log

Script save all `print()` functions in file `log.txt` in current directory.
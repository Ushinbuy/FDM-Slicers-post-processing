#!/bin/bash

# set -x == set -o xtrace

PATH+=:/usr/local/bin/

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

exec 1>$DIR/log.txt
exec 2>&1

echo "Arguments is"
echo "${@}"

ARG1=$1
ARG2=$2

# /usr/bin/env python3 $DIR/LAsimplify3D.py "${@}"

# switch file and hwconfig argument order
if [ "$ARG2" == "-s3d" ]; then
  echo "start script"
  python3 $DIR/linearAdvance.py "${@}"
elif [ "$ARG1" == "-ps" ]; then
  echo "start script"
  python3 $DIR/linearAdvance.py "$2" "$1"
else
  echo "Error in argument of type of slicer"
fi

# /Users/nik-nik/Desktop/Profiles/Scripts/LA.sh [output_filepath] -s3d
# /Users/nik-nik/Desktop/Profiles/Scripts/LA.sh -ps;
#!/bin/bash

# set -x == set -o xtrace

PATH+=:/usr/local/bin/

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

exec 1>$DIR/log.txt
exec 2>&1

echo "Arguments is"
echo "${@}"

if [ "$2" == "-s3d" ]; then
  echo "start script"
  python3 $DIR/src/linearAdvance.py "${@}"
elif [ "$1" == "-ps" ]; then
  echo "start script"
  python3 $DIR/src/linearAdvance.py "$2" "$1"
else
  echo "Error in argument of type of slicer"
fi

# /Users/nik-nik/Desktop/Profiles/Scripts/LA.sh [output_filepath] -s3d
# /Users/nik-nik/Desktop/Profiles/Scripts/LA.sh -ps;
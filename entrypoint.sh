#!/bin/bash

echo "STARTING BUILD PROCESS OF FILE \"$@\""

declare requirements="src/requirements.txt"

if [ -f $requirements ]; then
    echo "INSTALL REQUIREMENTS"
    wine python.exe -m pip install -r $requirements
    python3 -m pip install -r $requirements
fi

wine python.exe build.py src/$@
python3 build.py src/$@

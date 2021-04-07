#!/bin/bash
python3 src/main.py

if [ "$?" != "0" ]; then
    if [ "$1" != "--norepeat" ]; then
        echo "Run failed, starting setup..."
        /bin/bash setup.sh
        echo "Restarting program..."
        /bin/bash run.sh "--norepeat"
    fi
    exit 1
fi

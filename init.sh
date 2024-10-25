#!/bin/bash
if [ -e init.py ]; then
    python init.py
    rm init.py
    echo "Initialization done"
else
    echo "Already initialized"
fi

#!/usr/bin/env bash
pip install -r ./requirements.txt
if [[ $? -ne 0 ]]; then 
    echo """Check requirements.txt location.
            Must be near checkProcess.py"""
    exit 1 ;
fi
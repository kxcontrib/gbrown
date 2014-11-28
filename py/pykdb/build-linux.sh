#!/bin/sh
python setup.py build -cunix

python setup.py install --record files.txt --user


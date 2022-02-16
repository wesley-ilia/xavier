#!/bin/bash

rm -fr raw_data clean_data

python3 download_from_s3.py

python3 codesh_normalize.py
python3 thor_normalize.py
python3 startupbase_normalize.py
python3 slintel_normalize.py

python3 main.py
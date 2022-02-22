DIR_RAW = raw_data
DIR_CLEAN = clean_data

all: dir
	python3 download_from_s3.py
	python3 main.py


dir:
	mkdir -p $(DIR_RAW)
	mkdir -p $(DIR_CLEAN)

.PHONY: dir

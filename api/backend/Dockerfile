FROM python:3.9.9-slim-buster

WORKDIR /home/backend

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /home/backend

ENTRYPOINT ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]

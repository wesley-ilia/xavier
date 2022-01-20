FROM python:3.8.12-bullseye

WORKDIR /backend

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /backend

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]

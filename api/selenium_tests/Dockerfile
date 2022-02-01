FROM python:3.8.12-bullseye

WORKDIR /selenium_tests

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

#Download chromedriver version
RUN apt-get update -y;\
	apt-get install -y wget unzip chromium

COPY chromedriver /usr/bin/

COPY . /selenium_tests

RUN mkdir ~/Downloads

ENTRYPOINT ["pytest", "main.py"]
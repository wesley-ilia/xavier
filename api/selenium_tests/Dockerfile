FROM python:3.8.12-buster

WORKDIR /selenium_tests/

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

#Download chromedriver version
RUN apt-get update -y;\
	apt-get install -y wget unzip chromium

ENV CHROMIUM_VERSION="https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip"
ENV CHROMIUM_DRIVER_ZIP="chromedriver_linux64.zip"

RUN wget -O $CHROMIUM_DRIVER_ZIP $CHROMIUM_VERSION;\
	unzip $CHROMIUM_DRIVER_ZIP;\
	mv chromedriver /usr/local/bin/;\
	rm -f $CHROMIUM_DRIVER_ZIP

RUN mkdir ~/Downloads

COPY . /selenium_tests/

# RUN apk add --no-cache bash

RUN chmod +x ./wait-for-it.sh ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["pytest", "main.py"]
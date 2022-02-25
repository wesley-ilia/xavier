FROM python:3.8.12-buster

WORKDIR /slintel

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

#Download chromedriver version
RUN apt-get update -y;\
	apt-get install -y wget unzip chromium

#SETUP CHROMEDRIVER
ENV CHROMEDRIVER_VERSION="https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip"
ENV CHROMEDRIVER_FILE="chromedriver_linux64.zip"

RUN wget -O $CHROMEDRIVER_FILE $CHROMEDRIVER_VERSION;\
	unzip $CHROMEDRIVER_FILE;\
	mv chromedriver /usr/bin/;\
	rm -f $CHROMEDRIVER_FILE

ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

COPY ["main.py", "utils_get_by_website.py", "slintel_bot.py", "s3.py", "/slintel/"]

ENTRYPOINT ["/tini", "--"]
CMD ["python", "main.py"]

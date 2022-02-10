FROM python:3.8.12-bullseye

WORKDIR /slintel

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

#Download chromedriver version
RUN apt-get update -y;\
	apt-get install -y wget unzip curl

#SETUP CHROMIUM
ENV CHROMIUM_DOWNLOAD="deb http://download.opensuse.org/repositories/home:/ungoogled_chromium/Debian_Bullseye/ /"

ENV CHROMIUM_KEY="https://download.opensuse.org/repositories/home:/ungoogled_chromium/Debian_Bullseye/Release.key" 

RUN echo $CHROMIUM_DOWNLOAD | tee /etc/apt/sources.list.d/home-ungoogled_chromium.list > /dev/null

RUN curl -s $CHROMIUM_KEY | gpg --dearmor | tee /etc/apt/trusted.gpg.d/home-ungoogled_chromium.gpg > /dev/null

RUN apt-get update -y;\
	apt install -y ungoogled-chromium

#SETUP CHROMEDRIVER
ENV CHROMEDRIVER_VERSION="https://chromedriver.storage.googleapis.com/95.0.4638.54/chromedriver_linux64.zip"
ENV CHROMEDRIVER_FILE="chromedriver_linux64.zip"

RUN wget -O $CHROMEDRIVER_FILE $CHROMEDRIVER_VERSION;\
	unzip $CHROMEDRIVER_FILE;\
	mv chromedriver /usr/local/bin/;\
	rm -f $CHROMEDRIVER_FILE

#setup aws credentials
COPY aws_script.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/aws_script.sh

ENTRYPOINT ["aws_script.sh"]

COPY ["main.py", "slintel_bot.py", "s3.py", "/slintel/"]

CMD ["python", "main.py"]

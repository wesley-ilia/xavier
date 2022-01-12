FROM python:3.8.12-bullseye

WORKDIR /codesh

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
	rm -f $CHROMIUM_DRIVER_ZIP;\
	export PATH=$PATH:/usr/local/bin

#setup aws credentials
COPY aws_script.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/aws_script.sh;\
	ln -s /usr/local/bin/aws_script.sh

ENTRYPOINT ["aws_script.sh"]


COPY . /codesh
CMD ["python", "main.py"]

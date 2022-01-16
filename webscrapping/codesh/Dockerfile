FROM python:3.8.12-bullseye

WORKDIR /codesh

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

#Download chromedriver version
RUN apt-get update -y;\
	apt-get install -y wget unzip chromium

COPY chromedriver /usr/local/bin/

#setup aws credentials
COPY aws_script.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/aws_script.sh

ENTRYPOINT ["aws_script.sh"]

COPY ["main.py", "selenium_bot.py", "beautiful_bot.py", "s3.py", "/codesh/"]

CMD ["python", "main.py"]

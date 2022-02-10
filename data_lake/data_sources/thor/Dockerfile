FROM python:3.8.12-bullseye

WORKDIR /thor

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN apt-get update -y;\
	apt-get install -y wget unzip chromium

COPY chromedriver /usr/local/bin/

#setup aws credentials

COPY aws_script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/aws_script.sh
ENTRYPOINT ["aws_script.sh"]

COPY ["main.py", "s3.py", "thor_bot.py", "/thor/"]

CMD ["python", "main.py"]


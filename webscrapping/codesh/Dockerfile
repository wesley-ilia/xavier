FROM python:3.8.12-bullseye

WORKDIR /codesh

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN mkdir -p ~/.aws
COPY aws_script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/aws_script.sh;\
	export PATH=$PATH:/usr/local/bin
CMD ["aws_script.sh"]

COPY . /codesh
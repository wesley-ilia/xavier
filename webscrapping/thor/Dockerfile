#FROM amazon/aws-lambda-python

#COPY . .
#COPY login.env /root/
#RUN apt update -y && pip install pip pandas bs4 requests --upgrade && python thor_request.py

FROM amazon/aws-lambda-python

COPY start.sh /root/
RUN mkdir thor

COPY . thor/
RUN python -m pip install  pip pandas bs4 --upgrade
RUN pip install --upgrade pip
RUN pip install pandas
RUN pip install requests
RUN pip install bs4

VOLUME ["/home/ferrari"]

ENTRYPOINT bash /root/start.sh


#RUN pip install pytest
#RUN pip install mysql-connector-python
#RUN pip install selenium
#RUN pip install fastapi
#RUN pip install jinja2
#RUN pip install uvicorn
#RUN pip install pymysql

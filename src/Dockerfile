#Using Python 3
FROM python:3.8-rc

#work directory
WORKDIR /todoapp

COPY . /todoapp

#install requirements
RUN pip install -U -r requirements.txt

EXPOSE 80

ENV NAME TodoENV

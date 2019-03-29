#Using Python 3
FROM python:3.8-rc

WORKDIR /restapis

COPY . /restapis

RUN pip --proxy http://proxy.rd.francetelecom.fr:8080 install -U -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "restapis/drf/todolist_api/manage.py", "runserver"]
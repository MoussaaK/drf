#Using Python 3
FROM python:3.8-rc

#work directory
WORKDIR /restapis

COPY . /restapis

CMD["pwd"]

#install requirements
RUN pip --proxy http://x.x.x.x install -U -r requirements.txt

EXPOSE 8000

ENV NAME todo

ENTRYPOINT ["python", "./drf/todolist_api/manage.py"]

CMD ["runserver", "0.0.0.0:8000"]
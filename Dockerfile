FROM python:2.7.14-alpine3.6

RUN mkdir /src
COPY ./requirements.txt /src/
COPY ./app.py /src/
RUN pip install -r /src/requirements.txt
CMD [ "python", "./src/app.py" ]
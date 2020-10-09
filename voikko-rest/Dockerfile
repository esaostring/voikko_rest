FROM python:3.7.0-stretch

RUN DEBIAN_FRONTEND=noninteractive \
	&& apt-get update \
	&& apt-get install -y voikko-fi python-libvoikko \
        && apt-get install -y python-flask python-flask-restful python-flask-sqlalchemy

WORKDIR /usr/src/app

RUN cp /usr/lib/python3/dist-packages/libvoikko.py /usr/src/app/libvoikko.py

RUN pip install flask flask-jsonpify flask-restful

COPY ./rest_app.py ./

ENTRYPOINT ["python3", "./rest_app.py"]


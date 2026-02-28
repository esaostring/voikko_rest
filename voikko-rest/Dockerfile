FROM python:3.14-slim

RUN DEBIAN_FRONTEND=noninteractive \
	&& apt-get update \
	&& apt-get install -y voikko-fi python-libvoikko

WORKDIR /opt

COPY requirements.txt ./

RUN python3 -m venv venv && ./venv/bin/pip install --upgrade pip && ./venv/bin/pip install -r requirements.txt

COPY ./rest_app.py ./

ENTRYPOINT ["./venv/bin/fastapi", "run", "--port", "8899", "./rest_app.py"]

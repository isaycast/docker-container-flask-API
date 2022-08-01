FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY employees_API employees_API


RUN pip3 install -r employees_API/requirements.txt


CMD [ "python", "employees_API/run.py" ]
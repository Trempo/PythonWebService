FROM python:3.9

RUN apt-get update && apt-get install vim -y --no-install-recommends

RUN apt install git

RUN git clone https://github.com/Trempo/PythonWebService.git

WORKDIR  PythonWebService/

RUN ls

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-m gunicorn PythonWebService.wsgi " ]

# start server
EXPOSE 80
STOPSIGNAL SIGTERM

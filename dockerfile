FROM python:3.9 as base

RUN apt-get update && apt-get install vim -y --no-install-recommends

RUN apt install gnupg && gpg --version | grep Home

RUN apt install git

RUN git clone https://github.com/Trempo/PythonWebService.git

WORKDIR  PythonWebService/

RUN mkdir ~/.gnupg

RUN pip install --no-cache-dir -r requirements.txt

RUN pip list

COPY . .

# start server
FROM base as run
EXPOSE 80
STOPSIGNAL SIGTERM
CMD gunicorn -b 0.0.0.0:80  PythonWebService.wsgi


FROM base as test
CMD chmod +x run_test.sh; ./run_test.sh

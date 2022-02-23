FROM python:3.9

RUN apt-get update && apt-get install vim -y --no-install-recommends

RUN apt install gnupg && gpg --version | grep Home

RUN apt install git

RUN git clone https://github.com/Trempo/PythonWebService.git

WORKDIR  PythonWebService/

RUN mkdir ~/.gnupg

RUN pip install --no-cache-dir -r requirements.txt

RUN pip list

COPY . .

RUN chmod +x run_tests.sh

# start server
EXPOSE 80
STOPSIGNAL SIGTERM
CMD gunicorn -b :80  PythonWebService.wsgi


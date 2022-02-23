gunicorn --daemon PythonWebService.wsgi; python manage.py test; pkill gunicorn

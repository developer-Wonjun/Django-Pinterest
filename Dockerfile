FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/developer-Wonjun/Django-Pinterest.git

WORKDIR /home/Django-Pinterest/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=@35^ma!fx3rrcu6#%@kc0(_4do(p1)0+5+cndpl_g1q9nu)rdg" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]
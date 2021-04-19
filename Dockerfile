FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/developer-Wonjun/Django-Pinterest.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=@35^ma!fx3rrcu6#%@kc0(_4do(p1)0+5+cndpl_g1q9nu)rdg" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
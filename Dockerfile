FROM python:2.7.12-alpine

COPY       . /srv/
RUN        pip install -r /srv/requirements.txt

EXPOSE     8000

CMD ["python /srv/app.py"]

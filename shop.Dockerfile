FROM python:3.10

RUN apt update && apt install curl -y

COPY shop/requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY shop app/

WORKDIR app/

COPY wait-for-command.sh /

COPY shop/docker-entrypoint.sh /

COPY shop/runserver.sh /

RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh /runserver.sh

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"
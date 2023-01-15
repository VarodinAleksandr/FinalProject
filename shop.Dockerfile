FROM python:3.10

RUN apt update && apt install curl -y

COPY shop/requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY wait-for-command.sh /

COPY shop app/

WORKDIR app/

COPY shop/docker-entrypoint.sh /docker-entrypoint.sh
COPY shop/runserver.sh /runserver.sh
COPY wait-for-command.sh /wait-for-command.sh

RUN chmod +x /docker-entrypoint.sh /wait-for-command.sh /runserver.sh

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
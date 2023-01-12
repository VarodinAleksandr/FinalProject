FROM python:3.10

RUN apt update && apt install curl -y

COPY shop/requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY wait-for-command.sh /

COPY shop app/

WORKDIR app/

EXPOSE 8000

COPY shop/docker-entrypoint.sh /docker-entrypoint.sh

RUN ["chmod", "+x", "/docker-entrypoint.sh"]

RUN chmod +x docker-entrypoint.sh /wait-for-command.sh runserver.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
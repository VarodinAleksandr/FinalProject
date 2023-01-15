FROM python:3.10

RUN apt update && apt install curl -y

COPY shop/requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY wait-for-command.sh /

COPY store app/

WORKDIR app/

EXPOSE 8001

COPY store/docker-entrypoint.sh /docker-entrypoint.sh

RUN ["chmod", "+x", "/docker-entrypoint.sh"]

RUN chmod +x docker-entrypoint.sh /wait-for-command.sh runserver.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
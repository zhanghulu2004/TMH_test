FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN tmh_test create-db
RUN tmh_test populate-db
RUN tmh_test add-user -u admin -p admin
EXPOSE 5000
CMD ["tmh_test", "run"]

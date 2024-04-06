FROM python:3.11-alpine

ARG USER_ID=10001
ARG USER_NAME=webapp

RUN addgroup -g ${USER_ID} ${USER_NAME} && \
    adduser -DH --uid ${USER_ID} -G ${USER_NAME} ${USER_NAME}

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY src/* /app/

USER ${USER_NAME}

ENTRYPOINT [ "python", "app.py" ]

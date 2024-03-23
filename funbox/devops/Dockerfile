FROM python:3.11-alpine

ENV USER_ID=10001
ENV USER_NAME=webapp
ENV PORT=5000

RUN

RUN addgroup -g ${USER_ID} ${USER_NAME} && \
    adduser -DH --uid ${USER_ID} -G ${USER_NAME} ${USER_NAME}

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY src/* /app/

USER ${USER_NAME}
EXPOSE ${PORT}

ENTRYPOINT [ "python", "app.py" ]

FROM python:alpine

ENV FLASK_APP=app.py

WORKDIR /app

COPY . .

RUN apk update && \
    apk add --no-cache --virtual build-pkg build-base && \
    pip install pdm && \
    pdm install --prod && \
    apk del build-pkg && \
    apk add --no-cache libstdc++

EXPOSE 5000

CMD ["pdm", "run", "gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

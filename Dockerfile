FROM python

WORKDIR /app

COPY . /app

VOLUME ["/app/logs"]

RUN pip install PyYAML

CMD ["python", "main.py" ]
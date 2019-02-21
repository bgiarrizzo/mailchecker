FROM python:alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /tools/
WORKDIR /tools/

COPY mailchecker.py .
COPY requirements.txt .

RUN pip install -r requirements.txt \
  && rm -rf requirements.txt

EXPOSE 8081

CMD ["python3", "mailcheck.py"]

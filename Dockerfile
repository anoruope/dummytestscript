FROM python:3.6.8

LABEL maintainer="SWS" \
      description="SENSOR"

COPY . /app
WORKDIR /app

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

CMD ["python3","/app/tester.py"]
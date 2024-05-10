FROM ubuntu:20.04
WORKDIR /app

RUN apt-get update && apt-get install -y git
RUN apt-get install -y python3 && apt-get install -y python3-pip
RUN git clone https://github.com/IngSebastianTorres/DBTOJSON-Push-Notifier.git

RUN pip install -r /app/DBTOJSON-Push-Notifier/requirements.txt
CMD ["python3", "/app/DBTOJSON-Push-Notifier/main.py"]
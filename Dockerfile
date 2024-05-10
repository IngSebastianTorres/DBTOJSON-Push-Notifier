FROM ubuntu:20.04
WORKDIR /app

ENV GIT_ACCESS_TOKEN='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'
RUN apt-get update && apt-get install -y git
RUN git clone git@github.com:IngSebastianTorres/pushNotificationPythonFlask.git
RUN apt install python3
#COPY . .
RUN pip install -r ./requirements.txt
CMD ["python3", "./main.py"]
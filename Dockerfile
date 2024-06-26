#COMMAND TO BUILD BASE IMAGE
#docker build -t dbtojson-push-notifier:0.0.1 --no-cache .

#PYTHON SCRIPT MIGRATION AND PUSH NOTIFICATION CONFIGURATION
FROM ubuntu:20.04 as buildOS
ENV TZ=America/Bogota
ENV NODE_VERSION=18.20.2
ENV ANGULAR_VERSION=14.2.13
ENV GIT_ACCESS_TOKEN=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




RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /app

RUN apt-get update && apt-get install -y git\
    && apt-get install -y python3\
    && apt-get install -y python3-pip\
    && apt install -y curl\
    && apt-get -y install cron\
    && apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/America/Bogota /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

RUN git config --global user.email ingsebastiantorres95@gmail.com

COPY cronjob.sh /root/cronjob.sh
# Give execute permissions to the cron job
RUN chmod 0644 /root/cronjob.sh && crontab -l | { cat; echo "40 07 * * * bash /root/cronjob.sh"; } | crontab -
RUN chmod 0644 /root/cronjob.sh && crontab -l | { cat; echo "35 08 * * * bash /root/cronjob.sh"; } | crontab -
RUN chmod 0644 /root/cronjob.sh && crontab -l | { cat; echo "50 09 * * * bash /root/cronjob.sh"; } | crontab -

RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" |  tee /etc/apt/sources.list.d/ngrok.list &&  apt update &&  apt install ngrok

#NODE JS AND ALL DEPENDENCIES TO BUILD ANGULAR APPLICATION
SHELL ["/bin/bash", "--login", "-i", "-c"]
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash && source /root/.bashrc && nvm install v$NODE_VERSION

 
RUN git clone https://IngSebastianTorres:${GIT_ACCESS_TOKEN}@github.com/IngSebastianTorres/lraKpiTest.git\
    && npm install -g @angular/cli@$ANGULAR_VERSION\ 
    && npm install -g npm@10.8.0\
    && npm install --prefix /app/lraKpiTest\
    && cd /app/lraKpiTest\ 
    && git checkout gh-pages\
    && ln -s /root/.nvm/versions/node/v18.20.2/bin/node /usr/bin/node
SHELL ["/bin/bash", "--login", "-c"]

#ENV PATH=/usr/local/bin/ngrok:"$(npm prefix -g)"/bin:$PATH
RUN git clone https://github.com/IngSebastianTorres/DBTOJSON-Push-Notifier.git\
    && rm -rf /var/cache/apt/archives /var/lib/apt/lists/*.\
    && apt-get clean\
    && pip install -r /app/DBTOJSON-Push-Notifier/requirements.txt

RUN ngrok config add-authtoken 2JfC25sas7dHCCX4DzzxJTd1UW4_4Sd7wWF6E6782JF54pftd     
    
CMD cron & ngrok http --domain=marmoset-select-barnacle.ngrok-free.app 9999 > /dev/null & python3 /app/DBTOJSON-Push-Notifier/main.py 
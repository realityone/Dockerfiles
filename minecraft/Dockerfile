FROM debian:latest

RUN apt-get update && \
    apt-get install openjdk-7-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* 

ADD entrypoint.sh /usr/local/bin/entrypoint.sh

VOLUME /spigotmc
WORKDIR /spigotmc

CMD ["entrypoint.sh"]

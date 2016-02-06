FROM debian:latest

RUN apt-get update && \
    apt-get install -y openjdk-7-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* 

ADD entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh

VOLUME /spigotmc
WORKDIR /spigotmc

CMD ["/usr/bin/entrypoint.sh"]

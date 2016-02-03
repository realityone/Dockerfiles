FROM debian:latest

ADD . /ngrokd
WORKDIR /ngrokd

VOLUME /ngrokd/certs

EXPOSE 80
EXPOSE 4443

CMD ["./ngrokd", "-tlsKey", "certs/server.key", "-tlsCrt", "certs/server.crt", "-domain", "ouo.moe"]

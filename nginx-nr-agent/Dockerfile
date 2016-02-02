FROM nginx:latest

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 && \
    echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y nginx-nr-agent && \
    rm -rf /var/lib/apt/lists/* 

RUN ln -sf /dev/stdout /dev/tty 

ADD entrypoint.py /usr/bin/entrypoint.py
ADD default.conf /etc/nginx/conf.d/default.conf
RUN chmod +x /usr/bin/entrypoint.py

CMD ["/usr/bin/entrypoint.py"]
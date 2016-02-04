FROM maxexcloo/nginx-php

RUN wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add - && \
    sh -c 'echo "deb http://apt.newrelic.com/debian/ newrelic non-free" > /etc/apt/sources.list.d/newrelic.list' && \
    apt-get update && \
    apt-get install newrelic-php5 && \
    newrelic-install install && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD default.conf /etc/php5/fpm/pool.d/default.conf 
ADD php-fpm.conf /etc/supervisor/conf.d/php-fpm.conf 
ADD data /data

RUN chmod +x /data/entrypoint.sh

CMD ["/data/entrypoint.sh"]
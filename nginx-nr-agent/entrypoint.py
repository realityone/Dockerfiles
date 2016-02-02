#!/usr/bin/env python
import os
import socket
import StringIO
import subprocess
import ConfigParser


NGINX = '/usr/sbin/nginx'
NGINX_NR_AGENT = '/usr/bin/nginx-nr-agent.py'
NGINX_NR_AGENT_CONFIG = '/etc/nginx-nr-agent/nginx-nr-agent.ini'


class NginxNRAgentConfig(object):

    TEMPLATE = StringIO.StringIO("""# global settings

[global]
newrelic_license_key=YOUR_LICENSE_KEY_HERE
poll_interval=60

# logging settings

[loggers]
keys=root

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler,fileHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
args=('/var/log/nginx-nr-agent.log','a',)

[formatter_simpleFormatter]
format=%(asctime)s %(name)s [%(levelname)s]: %(message)s
datefmt=

# data sources settings

[source1]
name=exampleorg
url=http://127.0.0.1/status
""")

    CONFIG = {
        'global': ['newrelic_license_key',
                   'poll_interval'],
        'source1': ['name',
                    'url',
                    'http_user',
                    'http_pass']
    }

    def __init__(self, setting_file):
        super(NginxNRAgentConfig, self).__init__()
        self.setting_file = setting_file
        self.config = ConfigParser.ConfigParser()

        self.config.readfp(self.TEMPLATE)

    def do_config(self):
        for section, options in self.CONFIG.iteritems():
            for o in options:
                name = o.upper()
                if name in os.environ:
                    self.config.set(section, o, os.environ[name])

        with open(self.setting_file, 'wb') as config_file:
            self.config.write(config_file)


def main():
    config = NginxNRAgentConfig(NGINX_NR_AGENT_CONFIG)
    config.do_config()

    subprocess.call(['ln', '-sf', '/dev/stdout', '/dev/tty'])
    subprocess.call([NGINX, '-g', 'daemon on;'])
    subprocess.call([NGINX_NR_AGENT, '-f', '-c', NGINX_NR_AGENT_CONFIG, 'start'])

if __name__ == '__main__':
    main()


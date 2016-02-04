#!/bin/bash

mkdir -p /data/config /data/http /data/logs /data/secure

supervisord -n

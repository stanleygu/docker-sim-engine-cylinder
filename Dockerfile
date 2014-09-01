# Makes the most basic simulation working unit
# VERSION 0.0.5

FROM        stanleygu/roadrunner
MAINTAINER  Stanley Gu <stanleygu@gmail.com>

# Add RPC Server
ADD         ./tasks.py /usr/local/stanleygu/tasks.py

RUN         su user -c "source /usr/local/bin/virtualenvwrapper.sh; workon localpy; pip install celery==3.1.13 redis==2.10.3"

CMD         cd /usr/local/stanleygu && \
            su user -c "source /usr/local/bin/virtualenvwrapper.sh; workon localpy; celery -A tasks worker --loglevel=info"

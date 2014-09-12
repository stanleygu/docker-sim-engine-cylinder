# Makes the most basic simulation working unit
# VERSION 0.0.5

FROM        stanleygu/roadrunner
MAINTAINER  Stanley Gu <stanleygu@gmail.com>

# Add RPC Server
ADD         . /home/user/.virtualenvs/localpy/simworker
RUN         chown -R user /home/user/.virtualenvs/localpy/simworker

RUN         su user -c "source /usr/local/bin/virtualenvwrapper.sh; workon localpy; pip install celery==3.1.13 redis==2.10.3; pip install -e /home/user/.virtualenvs/localpy/simworker"

CMD         cd /usr/local/simworker && \
            su user -c "source /usr/local/bin/virtualenvwrapper.sh; workon localpy; celery -A tasks worker --loglevel=info"

# Makes the most basic simulation working unit

FROM        stanleygu/roadrunner
MAINTAINER  Stanley Gu <stanleygu@gmail.com>

# Add RPC Server
ADD         ./cylinder.py /usr/local/stanleygu/cylinder.py

CMD         su user -c "/home/user/.virtualenvs/localpy/bin/python /usr/local/stanleygu/cylinder.py 3131"

EXPOSE      3131

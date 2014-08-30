import roadrunner
import os

from celery import Celery

app = Celery(
    'cylinder',
    backend=os.environ['BROKER_URL'],
    broker=os.environ['BROKER_URL'])
rr = roadrunner.RoadRunner()


@app.task
def add(x, y):
    return x + y


@app.task
def rrRun(method, *params):
    if (method is not None):
        if (isinstance(method, basestring)):
            return getattr(rr, method)(*params)
        else:
            fun = getattr(rr, method.pop(0))
            for m in method:
                fun = getattr(fun, m)
            return fun(*params)

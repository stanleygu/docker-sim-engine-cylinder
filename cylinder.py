import zerorpc
import roadrunner
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = sys.argv[1]


class CylinderRPC(object):
    def getVersion(self):
        return 'Version 0.0.1'

    def loadModel(self, params, id):
        sbml = str(params['sbml'])
        rr = roadrunner.RoadRunner()
        self.rr = rr
        rr.load(sbml)
        return True

    def simulate(self, params, id):
        rr = self.rr
        rr.reset()
        return rr.simulate(params['timeStart'],
                           params['timeEnd'],
                           params['numPoints'])

    def rrRun(self, method, params):
        rr = self.rr
        if (isinstance(method, basestring)):
            return getattr(rr, method)(*params)
        else:
            fun = getattr(rr, method.pop(0))
            for m in method:
                fun = getattr(fun, m)
            return fun(*params)

    def getParameterIds(self, params, id):
        rr = self.rr
        return rr.model.getGlobalParameterIds()

    def getParameters(self, params, id):
        rr = self.rr
        ids = rr.model.getGlobalParameterIds()
        values = rr.model.getGlobalParameterValues()
        return {'ids': ids, 'values': values}

    def setParameterValueById(self, params, id):
        rr = self.rr
        rr.model[params['id']] = float(params['value'])
        rr.reset()
        return True

s = zerorpc.Server(CylinderRPC())
try:
    port
except NameError:
    print "Port was not defined"
else:
    print "Running zerorpc on Port: " + port
    s.bind("tcp://0.0.0.0:" + port)
    s.run()

import Pyro4

import os
import random

class FileService(object) :
    def listdir(self, d) :
        return os.listdir(d)
    
    def isdir(self, d) :
        return os.path.isdir(d)
    
    def getcwd(self) :
        return os.getcwd()
    
    def getFiles(self, d) :
        m = map(lambda x : x[2], os.walk(d))
        return m
    
    def getFile(self, name) :
        try :
            f = open(name, 'r')
            return f.read()
        except IOError :
            return ''

class StateService(object) :
    def __init__(self) :
        self.inc = 100
    
    def changeState(self, x) :
        self.inc = x
        return random.randint(0, self.inc)

def main() :
    service = FileService()
    #service = StateService()
    #Pyro4.Daemon.serveSimple({service: "example.service"}, ns=False)
    daemon = Pyro4.Daemon(host='localhost', port=9975)
    uri = daemon.register(service, 'service')
    print "uri=",uri
    daemon.requestLoop()

if __name__ == "__main__" :
    main()


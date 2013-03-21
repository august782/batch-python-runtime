import SocketServer
import os

import sys
sys.path.append("../")
sys.path.append("../batch/")
sys.path.append("../../")
sys.path.append("../../test/")
sys.path.append("../../test/evaluation")

import json

from batch import Service
from evaluation import TestObj

import numpy as np

class BasicObj :

    def __init__(self, inc) :
        self.inc = inc
    
    def foo(self) :
        return self.inc
    
    def range(self, x) :
        return range(x)
    
    def getImage(self, name) :
        img = open("tcp/" + name + '.jpg', "rb")
        buff = []
        try :
            byte = img.read(1)
            while byte != "" :
                buff.append(byte)
                byte = img.read(1)
        finally :
            img.close()
        
        return buff

class FileObj :
    
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

class MatrixObj :
    
    def matrix(self) :
        self.m = np.array([[1,2,3],[4,5,6],[7,8,9]])
    
    def mult(self) :
        #self.m = np.multiply(self.m, self.m)
        self.m = self.m * self.m
    
    def rows(self) :
        return range(3)
    
    def cols(self) :
        return range(3)
    
    def item(self, i) :
        return self.m.item(i)

#class BatchHandler(SocketServer.BaseRequestHandler) :
class BatchHandler(SocketServer.StreamRequestHandler) :
    
    def handle(self) :
        self.data = self.rfile.readline().strip()
        #print "{0} wrote:".format(self.client_address[0])
        #print self.data
        self.rfile.readline()   # Extra newline
        header = self.rfile.readline().strip()
        #print "{0} header:".format(self.client_address[0])
        #print header
        self.forest = self.rfile.readline().strip()
        #print "{0} forest is:".format(self.client_address[0])
        #print self.forest
        
        #service = Service.Service(BasicObj(100))
        service = Service.Service(FileObj())
        #service = Service.Service(MatrixObj())
        out = {}
        if not self.forest :
            out = service.serve(self.data, None)
        else :
            out = service.serve(self.data, json.loads(self.forest))
        #print BasicObj.BasicObj(1000).foo(1)
        self.request.send("Batch 1.0 JSON 1.0\n")   # Header required
        self.request.send(json.dumps(out))

if __name__ == "__main__" :
    HOST, PORT = "localhost", 9825

    server = SocketServer.TCPServer((HOST, PORT), BatchHandler)
    print "Server start..."
    server.serve_forever()


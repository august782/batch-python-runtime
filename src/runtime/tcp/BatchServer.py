import SocketServer

import sys
sys.path.append("../")
sys.path.append("../batch/")
sys.path.append("../../")
sys.path.append("../../test/")
sys.path.append("../../test/evaluation")

import json

from batch import Service
from evaluation import BasicObj

#class BatchHandler(SocketServer.BaseRequestHandler) :
class BatchHandler(SocketServer.StreamRequestHandler) :
    
    def handle(self) :
        self.forest = self.rfile.readline().strip()
        print "{0} forest is:".format(self.client_address[0])
        print self.forest
        #self.data = self.request.recv(10240).strip()
        #print "{0} wrote:".format(self.client_address[0])
        #print self.data
        self.data = self.rfile.readline().strip()
        print "{0} wrote:".format(self.client_address[0])
        print self.data
        
        service = Service.Service(BasicObj.BasicObj(100))
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


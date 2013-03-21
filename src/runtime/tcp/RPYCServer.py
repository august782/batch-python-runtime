import sys
import os

sys.path.insert(0, 'rpyc-3.2.3')
import rpyc

import numpy as np

class BasicService(rpyc.Service) :
    """
    def __init__(self) :
        self.y = 3
    """
    
    def exposed_foo(self) :
        return 100
    
    def exposed_range(self, x) :
        return range(x)
    
    def exposed_getImage(self, name) :
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
    
class TestService(rpyc.Service) :
    def exposed_test_range(self, x) :
        return range(x)
    
    def exposed_process(self) :
        print "process"

class FileService(rpyc.Service) :
    def exposed_listdir(self, d) :
        return os.listdir(d)
    
    def exposed_isdir(self, d) :
        return os.path.isdir(d)
    
    def exposed_getcwd(self) :
        return os.getcwd()
    
    def exposed_getFiles(self, d) :
        m = map(lambda x : x[2], os.walk(d))
        return m
    
    def exposed_getFile(self, name) :
        try :
            f = open(name, 'r')
            return f.read()
        except IOError :
            return ''

class MatrixService(rpyc.Service) :
    def exposed_matrix(self) :
        self.m = np.array([[1,2,3],[4,5,6],[7,8,9]])
    
    def exposed_mult(self) :
        self.m = self.m * self.m
    
    def exposed_rows(self) :
        return range(3)
    
    def exposed_cols(self) :
        return range(3)
    
    def exposed_item(self, i) :
        return self.m.item(i)

if __name__ == "__main__" :
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(FileService, port = 9981, protocol_config = {"allow_all_attrs" : True})
    print "Server start"
    t.start()


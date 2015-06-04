"""
* @name asio_acceptor.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/4 19:15
*
* @desc asio_acceptor.py
"""

class AsioAcceptor:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.rmiServer = None

    def setRmiServer(self, rmiServer):
        self.rmiServer = rmiServer
####
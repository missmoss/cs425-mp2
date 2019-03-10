import numpy as np
import socketserver as ss
import parser
import socket

# IMPORT STATEMENTS
import socket
import sys
from threading import Thread
import threading
import time
import logging
import fcntl, os
import errno
import signal



class Node:

    s = None
    ip = None

    service = None
    con = None

    serv = None

    def openServer(self, port):

        serverSocket = socket.socket()
        serverSocket.bind(port)
        serverSocket.listen(20)

        return serverSocket



    def connect2Service(self, port, address, TYPE=None):

        s = socket.socket()
        self.con = s.connect((port, address))

        self.service = s.getpeername()


    def sendInitiation(self):
        self.con.send('CONNECT node 1 ')



node = Node()






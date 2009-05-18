#!/usr/bin/python

import os
import sys
import commands
import socket

class Host(object):
    def __init__(self,_hostname): 
        try:
            self.setIP(_hostname)
            self.__myHostname = _hostname
        except socket.gaierror:
            print "Hostname is invalid or does not resolve in DNS!"
            raise SystemExit
    def __str__(self): return " ".join([self.__myHostname,self.__myIP])
    def validateHostname(self,_hostname): return socket.gethostbyname(_hostname)
    def setIP(self,_hostname):
        try:
            self.__myIP = socket.gethostbyname(_hostname)
        except socket.gaierror:
            raise         
    def getHostname(self): return self.__myHostname
    def getIP(self): return self.__myIP
    def hostCommand(self,_command): return os.system("ssh " + " ".join([self.getHostname(),_command]))
    def hostFile(self,_file,_path): return os.system("scp " + _file + " " + self.getHostname() + ":" + _path)
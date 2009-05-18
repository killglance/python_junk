#!/usr/bin/python

from host import Host

class Cluster(object):
    def __init__(self,_cluster = []):
        if isinstance(_cluster,str):
            #if the param is a string, create a host from the string and add it as a list of hosts
            self.__myCluster = [ Host(_cluster) ]
        else:
            self.__myCluster = _cluster
    def __str__(self):
        #use list comprehension uses for to iterate over __myCluster, assign them into h as a list and convert to string using str(h)
        return " ".join([ str(h) for h in self.__myCluster])
    def __iterateCluster(self):
        return
    def populateCluster(self,hostFile):    
        #Parse the file provided. Strip all newlines and spaces off the end and split list on whitespace
        for result in [line.strip().split() for line in open(hostFile)]:
            if result[1].startswith("agent-"):
            #if result[1].startswith("agent-") or result[1].startswith("rhel5-"):
                self.__myCluster.append(Host(result[1]))
    def remoteCommand(self,_command):
        for h in self.__myCluster:
            try:
                print "Executing on " + h.getHostname()
                h.hostCommand(_command)
            except OSError:
                print "Remote command failed!!!"
    def sendFile(self,_file,_dest):
        for h in self.__myCluster:
            try:
                h.hostFile(_file,_dest)
            except:
                print "Sending remote file failed!!!"
    def searchForHost(self,_key):
        #returns node with hostname _key or returns null (None) if nothing is found
        for _host in self.__myCluster:
            if _key == _host.getHostname():
                return _host
            else:
                continue
        return None
    def findAllHosts(self,_key):
        #returns a list of all nodes with hostnames that start with _key
        result = []
        for _host in self.__myCluster:
            if _host.getHostname().startswith(_key):
                result.append(_host)
        return result
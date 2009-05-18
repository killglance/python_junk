#!/usr/bin/python

import sys
from cluster import Cluster
       
myHostFile = "/etc/hosts"

myCluster = Cluster()
myCluster.populateCluster(myHostFile)

#testCluster = Cluster("localhost")

#testCluster.remoteCommand(sys.argv[1])

for myHost in myCluster.findAllHosts("agent"):
    print myHost
#if not myCluster.searchCluster("blarg"):
#    print "Node not found"
myCluster.remoteCommand(sys.argv[1])
#myCluster.sendFile(sys.argv[1],sys.argv[2])
#!/usr/bin/python

import socket
import sys
from cluster import Cluster


var = "Hi there"

if isinstance(var,str):
    print "its a string"
else:
    print "Nope"
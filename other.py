#!/usr/bin/env python

import sys
import time

ts = "Other [" + time.ctime() + "] "

argc = len(sys.argv)
print(ts + "Have " + str(argc) + " command line arguments")
if argc > 1:
    for i in range(1, argc):
        print(ts+"Arg "+str(i)+" '"+sys.argv[i]+"'")

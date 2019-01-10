#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os, sys

path = '/tmp'

retval = os.getcwd()
print "Current work directory: %s" % retval

# switch dir
os.chdir(path)

retval = os.getcwd()
print "Current work directory: %s" % retval

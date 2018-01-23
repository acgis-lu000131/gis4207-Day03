#-------------------------------------------------------------------------------
# Name:     List02.py
# Purpose:
##Same as List01.py but pass in the workspace as an argument on the command line
##(sys.argv) as you did with Desribe03.py.  Add delayed import as you did with
##Describe04.py and use .Exists as you did in Describe05.py.
# Author:      David Viljoen
# Created:     22/01/2015
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import os
import sys

arcpy = None

def setArcPy():
    global arcpy
    if arcpy == None:
        import arcpy
        from arcpy import env

if len(sys.argv) != 2:
    print "Usage:  List02.py <WorkspaceName>"
    sys.exit()

setArcPy()

ws = sys.argv[1]
if not arcpy.Exists(ws):
    print ws + " does not exist"
    sys.exit()

arcpy.env.workspace = ws
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    print fc
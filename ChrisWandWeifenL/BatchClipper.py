#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chris
#
# Created:     23-01-2018
# Copyright:   (c) chris 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
arcpy=None
import os
from sys import argv
def importarcpy():
    global arcpy
    import arcpy
    from arcpy import env
    global env

#should convert to ..\..\ format so that it can be used on other computers
#0=targetdata 1=sites 2=output
workspaces=[ argv[1], argv[2], argv[3]]
working_folder= os.path.dirname(__file__)
os.chdir(working_folder)


importarcpy()
env.workspace = workspaces[0]

fclist= arcpy.ListFeatureClasses()

env.workspace=workspaces[1]
sitesfclist= arcpy.ListFeatureClasses()

for fc in fclist:
    for sitfc in sitesfclist:
        env.workspace=workspaces[2]
        sitename=sitfc.split('.')
        outputformat= workspaces[2]+"\\"+sitename[0]+"_"+fc
        infeature=fc
        clipfeature=sitfc
        clips= arcpy.Clip_analysis(os.path.join(workspaces[0]+"\\"+fc),os.path.join(workspaces[1]+"\\"+sitfc),outputformat)





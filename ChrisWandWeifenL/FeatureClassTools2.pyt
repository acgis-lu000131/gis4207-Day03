import arcpy
import sys


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "fctoolsPYT"

        # List of tool classes associated with this toolbox
        self.tools = [BasicDescribe, GetParameterAsText]



class BasicDescribe(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Basic Describe"
        self.description = "Basic description of certain data within a given feature class"
        self.canRunInBackground = False
        self.storeRelativePaths = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        inFC=arcpy.Parameter(
            displayName="InputFeatureClass",
            name="inFC",
            datatype="DEFeatureclass",
            parameterType="Required",
            direction="Input")
        params=[inFC]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        fc = parameters[0].valueAsText

        dsc = arcpy.Describe(fc)

        fmt = "%-11s: %s"

        arcpy.AddMessage( fmt % ("BaseName",dsc.BaseName))

        arcpy.AddMessage( fmt % ("CatalogPath", dsc.CatalogPath))

        arcpy.AddMessage( fmt % ("DataType",dsc.DataType))

class GetParameterAsText(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Get Parameter as Text"
        self.description = "Get a list of feature classes from a given workspace."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        inWS=arcpy.Parameter(
            displayName="InputWorkspace",
            name="inWS",
            datatype="DeFolder",
            parameterType="Required",
            direction="Input")
        params=[inWS]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        ws = parameters[0].valueAsText

        arcpy.env.workspace = ws

        fcList = arcpy.ListFeatureClasses()

        for fc in fcList:
            arcpy.AddMessage(fc)
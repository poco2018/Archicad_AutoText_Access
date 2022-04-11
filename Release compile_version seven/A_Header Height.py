
from pyexpat.errors import XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF
from archicad import ACConnection
import archicad
import sys

from archicad.releases.ac25.b3000types import PropertyDefinitionOrError
conn = ACConnection.connect()

assert conn

acc = conn.commands
act = conn.types
acu = conn.utilities


elements = acc.GetElementsByType('Door')
lib  = acu.GetBuiltInPropertyId ('IdAndCategories_LibraryPartName')
height = acu.GetBuiltInPropertyId ('General_Height')
headHeight = acu.GetUserDefinedPropertyId('Testing','head height')

doorIdArray = []
for element in elements:
    value = acc.GetPropertyValuesOfElements([element.elementId],[lib])
    if value[0].propertyValues[0].propertyValue.value == 'Simple Door Opening':
        doorIdArray.append(element.elementId)
        
parameters = {}
wallIdArray =[]
wallguidArray = []
EPVArray =[]
for xx in doorIdArray:
    doorguid = str(xx.guid)
    parameters["command"] = "GetWallRef"
    parameters["inParams"] = [doorguid,'10']
    response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','Utilities'),parameters)
    wallguid = response['outParams']
    ele = act.ElementId(wallguid)
    value = acc.GetPropertyValuesOfElements([xx,ele],[height])
    wallheight =value[1].propertyValues[0].propertyValue.value
    doorheight = value[0].propertyValues[0].propertyValue.value
    print(wallheight - doorheight)
    dif = wallheight - doorheight
    normalLen = act.NormalLengthPropertyValue(dif,type='length',status = 'normal')
    EPV =act.ElementPropertyValue(xx,headHeight, normalLen)
    EPVArray.append(EPV)
result = acc.SetPropertyValuesOfElements(EPVArray)
print(result)
sys.exit()


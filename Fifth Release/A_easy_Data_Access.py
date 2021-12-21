from importlib import import_module
from archicad import ACConnection
import archicad
import sys

conn = ACConnection.connect()

assert conn, f'Communication Link is not available -timed out'

acc = conn.commands
act = conn.types
acu = conn.utilities

id =        '<PROPERTY-7E221F33-829B-4FBC-A670-E74DABCE6289>' # Element ID
area =      "<PROPERTY-AC5CCA52-F79B-4850-92A9-BED7CB7C3847>" # Area
layer =     "<PROPERTY-25826253-26F2-4D30-BE1B-0FFBB1314903>" #Layer
perimeter = "<PROPERTY-F2C033C5-7F47-4BF0-BC39-57F4C7E36783>" #Perimeter

text = "Just some text for testing"
parameters = {}
parameters["command"] = "GetSelected"
parameters["inParams"] = ['API_ZoneID']
response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','Utilities'),parameters)
print(response)
#for xx in response['outParams2']:
   # print(xx)
#sys.exit()
val = str(response['outparams2'][0][0])
#print(val)
#sys.exit()
word =  'ID = ' + id +'\n\n' + 'Area: ' + area + "\n\nlayer = " + layer + "\n\nPerimeter: " + perimeter \
+ '\n\nSome Sample Text'
guid = val
#print(guid) 
parameters["command"] = "SetLabelText"
parameters["inParams"] = [guid,'API_LabelID',word]
response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','Utilities'),parameters)
#text =''
print(response)
sys.exit()
#text = response['outParams2'][0] # for GetQuantity wall,door,slab,window
#'''
#section for calcquanties
for xx in response['outParams2']:
   if len(xx) > 1:
      text += xx[0] + ' ' +xx[1] + '\n'
   else:
      text += xx[0] + '\n'
#'''
print(text)
parameters["command"] = "ChangLabelText"
parameters["inParams"] = [text,'4.5']
response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','Utilities'),parameters)
print(response)
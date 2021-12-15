from importlib import import_module
from archicad import ACConnection
import archicad
import sys

conn = ACConnection.connect()

assert conn, f'Communication Link is not available -timed out'

acc = conn.commands
act = conn.types
acu = conn.utilities

id =   '<PROPERTY-7E221F33-829B-4FBC-A670-E74DABCE6289>' # Element ID
area = "PROPERTY-AC5CCA52-F79B-4850-92A9-BED7CB7C3847" # Area
parameters = {}
parameters["command"] = "GetSelected"
parameters["inParams"] = ['CLIENTCOMPANY']
response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','Utilities'),parameters)

val = str(response['outparams2'][0][0])

guid = val
print(guid)
parameters["command"] = "GetQuantity"
parameters["inParams"] = [guid,'API_SlabID','perimeter']
response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','Utilities'),parameters)
print(response)

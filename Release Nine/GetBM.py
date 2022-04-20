
from archicad import ACConnection
import archicad
import sys

conn = ACConnection.connect()

assert conn, f'Communication Link is not available -timed out'

acc = conn.commands
act = conn.types
acu = conn.utilities

parameters = {}
parameters["command"] = "GetBMAtt"
#guid = str(elements[0].elementId.guid)
#print(guid)
parameters["inParams"] = ['Concrete - Topping']
response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','Utilities'),parameters)
#print(response['outparams2'])
#sys.exit()
for result in response['outparams2']:
    print(result)
from archicad import ACConnection
import archicad
import sys
conn = ACConnection.connect()

assert conn

acc = conn.commands
act = conn.types
acu = conn.utilities
parameters = {}
parameters["command"] = "GetParams"
parameters["inParams"] = ["API_ZoneID","Related Zone Number"]
response = acc.ExecuteAddOnCommand(act.AddOnCommandId('AdditionalJSONCommands','Utilities'),parameters)
print(response)
input("press close to exit")
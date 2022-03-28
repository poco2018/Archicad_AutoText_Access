from msilib.schema import AppId, Property
from multiprocessing import parent_process
from urllib.parse import parse_qsl
from xml.sax.handler import property_dom_node
from archicad import ACConnection
import archicad
import sys

conn = ACConnection.connect()

assert conn, f'Communication Link is not available -timed out'

acc = conn.commands
act = conn.types
acu = conn.utilities

wallelements = acc.GetElementsByType('Wall')

elemids =[]
for value in wallelements:
    elemids.append(value.elementId)


#sys.exit()
elementID = acu.GetBuiltInPropertyId('General_ElementID')
compositeId = acu.GetBuiltInPropertyId('construction_CompositeName')
fireratingId = acu.GetUserDefinedPropertyId('General Ratings','Fire Resistance Rating')
stcratingId = acu.GetUserDefinedPropertyId('General Ratings','STC Rating')
ids =[]
ids.append(compositeId)
ids.append(fireratingId)
ids.append(stcratingId)
propValues = acc.GetPropertyValuesOfElements(elemids,ids)
str1 = ''
EPVArray = []
for ind,elemProp in enumerate(propValues):
    str1 = ''
    for index,prop in enumerate(elemProp.propertyValues):
       
        if index == 0:
            app = ''
        else:
            app = '-'
        if (prop.propertyValue.type == 'string' or prop.propertyValue.type =='singleEnum'):
            if prop.propertyValue.status != 'userUndefined':
                if  isinstance(prop.propertyValue.value,str):
                    str1 += app + prop.propertyValue.value
                else:
                    str1 += app + prop.propertyValue.value.displayValue
            else:
                continue
        else:
            continue
        normalString = act.NormalStringPropertyValue(str1,type='string',status = 'normal')
        EPV =act.ElementPropertyValue(elemids[ind],elementID, normalString)
        EPVArray.append(EPV)
    #sys.exit()
result = acc.SetPropertyValuesOfElements(EPVArray)
print(result)

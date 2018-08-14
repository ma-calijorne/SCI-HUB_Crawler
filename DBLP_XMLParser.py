from xml.dom import minidom

sXML = ''

#with open("Data\dblp.xml") as myfile:
#    for line in myfile:
#        print (line.rstrip("\n"))
#        sXML = sXML + (line.rstrip("\n"))


#print sXML

from xml.etree import ElementTree as ET

parser = ET.iterparse("Data\dblp.xml")
tags = []

for event, element in parser:
    # element is a whole element
    try:
        tags.append(element.tag)
        element.clear()
    except:
        print 'Erro!'
        pass
    #if element.tag == 'yourelement':
         # do something with this element
         # then clean up


UNIQUETags = set(tags)

for eachUniqueTAG in UNIQUETags:
    print eachUniqueTAG
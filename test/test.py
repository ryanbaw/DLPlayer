'''
Created on 2016-3-1
Create a xml document
@author: ryan
'''
 
from xml.dom import minidom
 
doc = minidom.Document()
doc.appendChild(doc.createComment("This is a simple xml."))
cmdlist = doc.createElement("cmdlist")
doc.appendChild(cmdlist)
 
def addBook(newcmd):
    command = doc.createElement("command")
    command.setAttribute("id", newcmd["id"])
     
    param1 = doc.createElement("param1")
    param1.appendChild(doc.createTextNode(newcmd["param1"]))
    command.appendChild(param1)
     
    param2 = doc.createElement("param2")
    param2.appendChild(doc.createTextNode(newcmd["param2"]))
    command.appendChild(param2)

    param3 = doc.createElement("param3")
    param3.appendChild(doc.createTextNode(newcmd["param3"]))
    command.appendChild(param3)
 
    cmdlist.appendChild(command)
 
addBook({"id":"CMD_MUSIC_PLAY", "param1":"p1","param2":"p2","param3":"p3"})
addBook({"id":"CMD_MUSIC_PAUSE","param1":"p1","param2":"p2","param3":"p3"})
addBook({"id":"CMD_MUSIC_NEXT", "param1":"p1","param2":"p2","param3":"p3"})
addBook({"id":"CMD_MUSIC_PREV", "param1":"p1","param2":"p2","param3":"p3"})
 
f = file("command.xml","w")
doc.writexml(f)
f.close()

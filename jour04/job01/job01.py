##########################################################################
import argparse
from xml.dom.minidom import parse, parseString

# from xml.dom import getElementByTagName
rss_content=parse("domain.xml")


domaine = rss_content.getElementsByTagName("title")
rss_title = domaine[0].data

Traceback(most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: Element instance has no attribute 'data'

# def Reading():
#     read = open("output.txt" , "r")
#     print(read.read())
#     read.close()
# print()

# def GetDomain():
#     doc = open("domain.xml" , "r")
#     domaine = doc.getElementsByTagName("domain")
#     print(doc.read())
#     doc.close()
    
#     print( "Il y a " , len(doc) , "de balise domaine dans le fichier XML.") ## imprime le nb de balise "domaine" trouvés
# print()
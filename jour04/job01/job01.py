##########################################################################
import argparse
from xml.dom.minidom import parse, parseString

# rss_content=parse("domain.xml")


# def Reading():
#     read = open("output.txt" , "r")
#     print(read.read())
#     read.close()
# print()

def GetDomain():
    doc = parse("domain.xml")
    domaine = doc.getElementsByTagName("domain")
    # print(doc.read())
    # doc.close()
print(GetDomain())
    
# print( "Il y a " , len(doc) , "de balise domaine dans le fichier XML.") ## imprime le nb de balise "domaine" trouvés
# print()
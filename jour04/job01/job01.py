import xml.etree.ElementTree as ET # pour parser le fichier XML

tree = ET.parse('domain.xml') # on ouvre le fichier XML
root = tree.getroot() # on récupère la racine du fichier XML


# tree = ET.parse('domain.xml') # on ouvre le fichier XML

root.tag # on récupère le nom de la racine
root.attrib # on récupère les attributs de la racine



# for domain in root.findall('domain'):
    
#     name = domain.find('name').text
#     ext = domain.get('.com' , 'org' 'net')
#     print(name, ext)

for child in root: # on parcourt les enfants de la racine
    print(child.tag, child.attrib) # on affiche le nom de l'enfant et ses attributs
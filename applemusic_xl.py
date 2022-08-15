#   Setup tree { https://docs.python.org/3/library/xml.etree.elementtree.html }
import xml.etree.ElementTree as ET
tree = ET.parse('Library.xml')
root = tree.getroot
#   Finds the name of the song {}
def find_name():
    key = 'Name'
    tags = root().iter()
    songs = []
    for elem in tags:
        if key == elem.text:
            next_node = next(tags)
            songs.append(next_node.text)

    print(songs)

        

    

#   Find the artist of the song {}

#   Find the album name {}

find_name()
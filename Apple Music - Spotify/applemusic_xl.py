#   Setup tree { https://docs.python.org/3/library/xml.etree.elementtree.html }
import xml.etree.ElementTree as ET
library = input('What is the library name?') + '.xml'
tree = ET.parse(library)
root = tree.getroot
#   Finds the name of the song {https://www.datacamp.com/tutorial/python-xml-elementtree}
def find_name():
    tags = root().iter()
    key = 'Name'
    songs = []
    for elem in tags:
        if key == elem.text:
            next_elem = next(tags)
            songs.append(next_elem.text)
    del songs[-1]
    return songs

#   Find the artist of the song {https://www.datacamp.com/tutorial/python-xml-elementtree}
def find_artist():
    tags = root().iter()
    key = 'Artist'
    artists = []
    for elem in tags:
        if key == elem.text:
            next_elem = next(tags)
            artists.append(next_elem.text)
    return artists

#   Find the album name {https://www.datacamp.com/tutorial/python-xml-elementtree}
def find_album():
    tags = root().iter()
    key = 'Album'
    albums = []
    for elem in tags:
        if key == elem.text:
            next_elem = next(tags)
            albums.append(next_elem.text)
    return albums
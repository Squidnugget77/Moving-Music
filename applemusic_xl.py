#   Setup tree { https://docs.python.org/3/library/xml.etree.elementtree.html }
import xml.etree.ElementTree as ET
tree = ET.parse('Rock.xml')
root = tree.getroot
tags = root().iter()
#   Finds the name of the song {https://www.datacamp.com/tutorial/python-xml-elementtree}
def find_name():
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
    key = 'Artist'
    artists = []
    for elem in tags:
        if key == elem.text:
            next_elem = next(tags)
            artists.append(next_elem.text)
    return artists
#   Find the album name {https://www.datacamp.com/tutorial/python-xml-elementtree}
def find_album():
    key = 'Album'
    albums = []
    for elem in tags:
        if key == elem.text:
            next_elem = next(tags)
            albums.append(next_elem.text)
    return albums
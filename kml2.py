from os import path
from fastkml import kml
from pykml import parser
from lxml import etree, objectify
import xml.etree.ElementTree as ET
import sys

kml_file = r"c:\Users\jack\Desktop\test\Tracks.kml"

with open(kml_file, "rb") as f:
    root = parser.parse(f).getroot()
    # root.Document.name.text = "test"
    for flyto in root.Document.Folder[
        "{http://www.google.com/kml/ext/2.2}Tour"
    ].Playlist.FlyTo:
        lookat = flyto["{http://www.opengis.net/kml/2.2}LookAt"]
        lookat.tilt = float(0)
        lookat.heading = float(0)

objectify.deannotate(root, cleanup_namespaces=True, xsi_nil=True)       
kml_str = etree.tostring(etree.ElementTree(root), pretty_print=True, encoding='utf8')
output_file = kml_file[:-4] + "_modified.kml"
with open(output_file, "wb") as f:
    f.write(kml_str)

import glob
import os
import PIL
from PIL import Image

print "image smaller en directorios y subfdirectorios"
print "Finding..."

for (dir, _, files) in os.walk("./"):
    for f in files:
        path = os.path.join(dir, f)
        if  os.stat(path).st_size > 900000:
            print path, f, os.stat(path).st_size
            basewidth = 800
            img = Image.open(str(path))
            wpercent = (basewidth / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
            img.save(str(path))

"""Software para minificar Archivos jpeg en directorios y subfdirectorios"""
"""Credito Jorge Fernandez"""
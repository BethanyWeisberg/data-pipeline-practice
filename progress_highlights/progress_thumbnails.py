from PIL import Image
import glob, os
import re

size = 750, 750

for infile in glob.glob("*.png"):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        rgb_im = im.convert('RGB')
        rgb_im.thumbnail(size)
        rgb_im.save(re.sub(".png","",infile,count=1) + "_thumbnail.jpg", "JPEG")
        os.remove(infile)
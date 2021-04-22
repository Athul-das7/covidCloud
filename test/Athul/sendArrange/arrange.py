import os
from PIL import Image

current_path = os.getcwd()
for root, dirs, files in os.walk(current_path, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        #if os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff":
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                print ("A jpeg file already exists for %s" % name)
            # If a jpeg with the name does *NOT* exist, covert one from the tif.
            else:
                outputfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
                try:
                    im = Image.open(os.path.join(root, name))
                    print ("Converting jpeg for %s" % name)
                    im.thumbnail(im.size)
                    o = outputfile.split('\\')
                    #//o = 'D:\\Programming\\miniproject\\covidCloud\\test\\Athul\\sendArrange\\FINAL'+outputfile
                    o=outputfile[:61]+"FINAL\\"+o[-1]
                    im.save(o, "JPEG", quality=100)
                except Exception:
                    print ("hehehahaha")
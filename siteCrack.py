#I DON'T  GET THE RISK FOR ANYTHING
#.sis version comes slowly
import urllib
import os
import appuifw

SAVEDIR  = appuifw.query(u"Path to file:", "text")
os.path.join(SAVEDIR)
if not os.path.isdir(SAVEDIR):
    os.makedirs(SAVEDIR)

targetf = appuifw.query(u"Name the file:", "text")
try:
    f=open(targetf,'rt')
    try:
        content = f.read()
        config=eval(content)
        f.close()
    except:
        print 'Can not read file'
except:
    print 'Can not open file'

urltarget = appuifw.query(u"The target url:", "text")
target = urllib.urlopen(urltarget)
data = target.read()
file = open(targetf, 'wb')
file.write(data, SAVEDIR)
file.close
print('The file was created:'), targetf

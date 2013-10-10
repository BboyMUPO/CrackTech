#I don't get the risk for anything
import os
import appuifw

SAVEDIR = appuifw.query(u"Path for the files:", "text")
if not os.path.isdir(SAVEDIR):
    os.makedirs(SAVEDIR)

os.path.join(SAVEDIR)

targetf = 'C:\\private\10202be9\persists\cccccc00.cre'
f=open(targetf,'rt')
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

file = open(targetf, 'wb')
file.write(targetf, SAVEDIR)
file.close

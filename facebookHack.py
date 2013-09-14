import urllib
import md5
import appuifw

def crack():
    your_list = 'qwertzuiopasdfghjklíyxcvbnm' #latters you want to use in brute-force attack
    complete_list = []
    for current in xrange(2): #how long the password is default 2
        a = [i for i in your_list]
        for y in xrange(current):
            a = [x+i for i in your_list for x in a]
        complete_list = complete_list+a

target = appuifw.qurey(u"Facebook id:", "text")
urllib.urlopen(target)
password = crack()
print(password)
#XD feltörök minden faszt facen peti v akarki aki ezt olvassa es magyar XD

#I DON'T GET THE RISK FOR ANYTHING

s = "a" #test password
chars = [u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"i", u"j", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"z", u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9"]

def brute(latters):
    for i in latters:
        asd = i
        print(asd)
        if asd == s:
            print('PASSWORD FOUND:'),asd
            return 0
            
print"=========="
print"[BboyMUPO]"
print"=========="

print"BRUTE FORCE!"

print"Chacked passwords:"

brute(chars)

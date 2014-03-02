s = "afv"

def brute4(latters):
    for i in latters:
        for a in latters:
            for l in latters:
                for p in latters:
                    asd = i+a+l+p
                    print(asd)
                    if asd == s:
                        print('PASSWORD FOUND:'),asd
                        return 0
                        

def brute3(latters):
    for i in latters:
        for a in latters:
            for l in latters:
                asd = i+a+l
                print(asd)
                if asd == s:
                    print('PASSWORD FOUND:'),asd
                    return 0


def brute(latters):
    for i in latters:
        asd = i
        print(asd)
        if asd == s:
            print('PASSWORD FOUND:'),asd
            return 0

def brute2(latters):
    for i in latters:
        for a in latters:
            asd = i+a
            print(asd)
            if asd == s:
                print('PASSWORD FOUND:'),asd
                return 0


def brute5(latters):
    for i in latters:
        for a in latters:
            for l in latters:
                for p in latters:
                    for s in latters:
                        asd = i+a+l+p+s
                        print(asd)
                        if asd == s:
                            print('PASSWORD FOUND:'),asd
                            return 0

def brute6(letters):
    for i in latters:
        for a in latters:
            for l in latters:
                for p in latters:
                    for s in latters:
                        for e in latters:
                            asd = i+a+l+p+s+e
                            print(asd)
                            if asd == s:
                                print('PASSWORD FOUND:'),asd
                                return 0

def brute7(letters):
    for i in latters:
        for a in latters:
            for l in latters:
                for p in latters:
                    for s in latters:
                        for e in latters:
                            for u in latters:
                                asd = i+a+l+p+s+e+u
                                print(asd)
                                if asd == s:
                                    print('PASSWORD FOUND:'),asd
                                    return 0


def brute8(letters):
    for i in latters:
        for a in latters:
            for l in latters:
                for p in latters:
                    for s in latters:
                        for e in latters:
                            for u in latters:
                                for r in latters:
                                    asd = i+a+l+p+s+e+u+r
                                    print(asd)
                                    if asd == s:
                                        print('PASSWORD FOUND:'),asd
                                        return 0

print"=========="
print"[BboyMUPO]"
print"=========="

print"BRUTE FORCE!"
print""

print"Chacked passwords:"

brute([u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"i", u"j", u"j", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"0"])
raw_input()
brute2([u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"i", u"j", u"j", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"0"])
raw_input()
brute3([u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"i", u"j", u"j", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"0"])
raw_input()
brute4([u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"i", u"j", u"j", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"0"])
raw_input()
brute5([u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"i", u"j", u"j", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"0"])
raw_input()
brute6([u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"i", u"j", u"j", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"0"])
raw_input()
brute7([u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"i", u"j", u"j", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"0"])
raw_input()
brute8([u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"i", u"j", u"j", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r", u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"0"])

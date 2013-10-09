#I DON'T GET THE RISK FOR ANYTHING

your_list = 'qwertzuiopasdfghjklíyxcvbnm' #latters you want to use in brute-force attack
complete_list = []
for current in xrange(2): #how long the password is default 2
    a = [i for i in your_list]
    for y in xrange(current):
        a = [x+i for i in your_list for x in a]
    complete_list = complete_list+a

testpass = ad
pass = complete_list

if pass == testpass:
    print('match:'), pass

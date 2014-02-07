#I DON'T  GET THE RISK FOR ANYTHING
import urllib

print"=========="
print"[BboyMUPO]"
print"=========="

print"SOURCE GRAB!"

dir = 'C://source.txt'

file = open(dir, 'w')

print"Enter the url address that's source you want to grab:"
url = raw_input()

file.write(urllib.urlopen(url).read())

print"Source sucessfully grabbed."

file.close

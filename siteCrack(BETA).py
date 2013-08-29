#I DON'T  GET THE RISK FOR ANYTHING
import urllib

target = urllib.urlopen('http://ctabustracker.com/bustime/.map/getBusesForRoute.jsp?route=22') #It's an example url
data = target.read()
file = open('rt22.xml', 'wb') #rt22.xml is the name of the created file
file.write(data)
file.close
print"rt22.xml sucesfully created."

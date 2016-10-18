from math import *

(a,b)=(int(input("Input side {}:".format(_))) for _ in range(2))

print "{}°".format(int(floor((atan2(a,b)*180/pi)+0.5)))

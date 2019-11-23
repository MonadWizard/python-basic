import time
import calendar
import os


a = '\n_________________________________________\n'
print(time)
print(a, time.time)
print(a, time.asctime(time.localtime(time.time())))
print(a, time.asctime(time.localtime(time.clock())))
print(a , time.strftime('%X %x %Z'))


print(a, time.gmtime())

print(a, a, time.strptime("30 Nov 00", "%d %b %y"))

os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0' #...............................?????
#time.tzset()
#print(a , time.strftime('%X %x %Z'))

#os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
#time.tzset()
#print(a,a , time.strftime('%X %x %Z'))







from time import gmtime, strftime
print(a, strftime('%a, %d %b %Y %H:%M:%S +0000', gmtime()))


print(calendar.month(2018, 9))

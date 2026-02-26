h = int(input('enter time in hours:'))
m = int(input('enter time in minutes:'))
s = int(input('enter time in seconds:'))

#1 min = 60 sec, 1 hr= 60 min, 60 min = 3600 sec
# now example is time in sec -
totaltime  = (h*3600 +m*60+s)

print('Totaltime in sec is',totaltime)

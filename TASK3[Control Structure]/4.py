import sys

month = sys.argv[1]
date = int(sys.argv[2])

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'March') and (date > 19):
	season = 'spring'
elif (month == 'June') and (date > 20):
	season = 'summer'
elif (month == 'September') and (date > 21):
	season = 'autumn'
elif (month == 'December') and (date > 20):
	season = 'winter'

print("Season is",season)

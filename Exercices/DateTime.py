﻿# import datetime 
# now = datetime.datetime.now() 

import datetime
now = datetime.datetime.now(datetime.timezone.utc)
# from exipfind import htmltext
# from first_script import (x)
# import pytz
# from datetime import datetime
# now = datetime.utcnow().replace(tzinfo=pytz.utc)

# # print ("Current date and time using str method of datetime object:" )

# print str(now)  
# print ("Current date and time using instance attributes:" )
# print ("Current year: %d" % now.year )
# print ("Current month: %d" % now.month) 
# print ("Current day: %d" % now.day )
# print ("Current hour: %d" % now.hour) 
# print ("Current minute: %d" % now.minute ) 
# print ("Current second: %d" % now.second )
# print ("Current microsecond: %d" % now.microsecond )


# print(htmltext)
print (" \n Current date and time :") 
print (now.strftime("   %Y-%m-%d %H:%M:%S"))




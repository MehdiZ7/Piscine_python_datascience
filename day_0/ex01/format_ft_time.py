import time
import datetime

#gets the seconds since 1970
epoch = time.time()

#gets the date
date = datetime.date.today()

#use the f-string to display what we need
print(f"Seconds since January 1, 1970: {epoch:,.4f} or {epoch:.2e} in scientific notation")
print(f"{date.strftime('%b %d %Y')}")

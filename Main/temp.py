import datetime
from datetime import date
date_str = '29-12-2017' # The date - 29 Dec 2017
format_str = '%d-%m-%Y' # The format
datetime_obj = datetime.datetime.strptime(date_str, format_str)
end_date = datetime_obj + datetime.timedelta(days=7)
print(date.today())
print((datetime.datetime.now()-datetime_obj).days)

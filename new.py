import time
from datetime import datetime

# function to return the timestamp of a date given
def returnTimestamp(string):
    element = datetime.strptime(string,"%d/%m/%Y")
    tuple = element.timetuple()
    timestamp = time.mktime(tuple)

    return (timestamp)

# function to return the date of a given timestamp
def returnDate(timestamp):
    return datetime.fromtimestamp(timestamp)

# the actual formula used in the article to find out when to propose
def proposal_date(A, B):
    proposal_date = (returnTimestamp(A) - 0.1 * returnTimestamp(B)) / 0.9

    return returnDate(proposal_date)

date_date = "{date}/{month}/{year}"
dob = "12/02/2004" #that's my birth date

pDate = proposal_date(date_date, dob)
print(pDate)

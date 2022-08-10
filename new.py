import time
from datetime import datetime

def returnTimestamp(string):
    element = datetime.strptime(string,"%d/%m/%Y")
    tuple = element.timetuple()
    timestamp = time.mktime(tuple)

    return (timestamp)

def returnDate(timestamp):
    return datetime.fromtimestamp(timestamp)

def proposal_date(A, B):
    proposal_date = (returnTimestamp(A) - 0.1 * returnTimestamp(B)) / 0.9

    return returnDate(proposal_date)

date_date = "{date}/{month}/{year}"
dob = "12/02/2004" #that's my birth date

pDate = proposal_date(date_date, dob)
print(pDate)
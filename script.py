import pikepdf
import os.path
import time
from datetime import datetime, timedelta

start_date_string = "01-01-1900"
end_date_string = "01-01-2000"
date_formatter = "%d%m%Y"

def current_milli_time():
    return round(time.time() * 1000)

def checkLastElem(str,check):
    chars = list(str)
    for char in chars:
        if char != check:
            return False
    return True

def test(pwd,f):
    try:
        with pikepdf.open(file, password=pwd) as pdf:
            f[0] = True
            f[1] = pwd
    except:
        pass
    finally:
        print("Tested: ",pwd)

def genDays():
    start_date = datetime.strptime(start_date_string, "%d-%m-%Y")
    end_date = datetime.strptime(end_date_string, "%d-%m-%Y")
    date_list = []
    current_date = start_date

    while current_date < end_date:
        date_list.append(current_date.strftime(date_formatter))
        current_date += timedelta(days=1)
    
    return date_list

dates = genDays()
found = [False,None]
file = "file.pdf"

if os.path.exists(file) != True:
    print("The file does not exist")
    exit()

print("Starting...")

startAt = current_milli_time()
for date in dates:
    test(date, found)
    if found[0] == True:
            print("Password found:", found[1])
            break

print("Time spent: ", (current_milli_time() - startAt))

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:04:29 2019

@author: Alicia
"""

#Regex for date file: \['([0-9]+)'\],\['[A-z][A-z][A-z] ([A-z][A-z][A-z]) ([0-9][0-9]) ([0-9][0-9]:[0-9][0-9]:[0-9][0-9]) \+[0-9][0-9][0-9][0-9] ([0-9][0-9][0-9][0-9]), replace with: \1,\5-\2-\3,\4
#Date to number: Aug --> 08, Apr --> 04, etc.
#Three columns: tweet_id, create_date, create_time (PK create_date,create_time)
#

#Using regex to insert a json key (id_str, or tweet id) before each  line in the jsonlines file
#Three files are read, of which three files are created. Regex matches whole line as well as \1 (id string), and script prints '"\1":' followed by full line and a comma. 
import re

#atRAE = open("AtRAEinforma2.json","r",encoding="utf-8")
#RAE = open("@RAEInforma.json","r",encoding="utf-8")

filename = "Please enter the file name as 'filename.csv' or 'filename.txt': "
filenick = str(filename)+"_cleaned.txt"
data = open(filename,"r",encoding="utf-8")
out = open(filenick,"a+",encoding="utf-8")

def date_time(data,out)
	count = 0
    for line in data:
        linea = re.search("\['[A-z][A-z][A-z] ([A-z][A-z][A-z]) ([0-9][0-9]) ([0-9][0-9]:[0-9][0-9]:[0-9][0-9]) \+[0-9][0-9][0-9][0-9] ([0-9][0-9][0-9][0-9])(.*)$\n", str(line))
        month = linea.group(1)
        if month == "Aug":
            month = "08"
        elif month == "Sep":
            month = "09"
        elif month == "Oct":
            month = "10"
        elif month == "Nov":
            month = "11"
        elif month == "Dec":
            month = "12"
        elif month == "Jan":
            month = "01"
        elif month == "Feb":
            month = "02"
        elif month == "Mar":
            month = "03"
        elif month == "Apr":
            month = "04"
        elif month == "May":
            month = "05"
        elif month == "Jun":
            month = "06"
        elif month == "Jul":
            month = "07"
        date = str(linea.group(4))+"-"+month+"-"+str(linea.group(2))+","+str(linea.group(3))+","+str(linea.group(5))+","+"\n"
        out.write(date)
        count = count + 1
        if count % 10000 == 0:
            print(count)
        else:
            continue

date_time(filenamme)
print("Finished cleaning" + str(filename))
exit()
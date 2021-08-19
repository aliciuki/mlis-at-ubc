# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:43:30 2019

@author: Alicia
"""
import csv
import jsonlines
import os

jsonllist = [files for files in os.listdir("C:\\Users\\Alicia\\Dropbox\\RAE\\JSONparsing\\UsersJSONL")]

def getcsv(jsonllist):
    for i in jsonllist:
        with jsonlines.open("C:\\Users\\Alicia\\Dropbox\\RAE\\JSONparsing\\UsersJSONL\\"+str(i),'r') as reader:
            counter3 = 0
            for tweet in reader:
                usr_id = str(tweet.get('id_str'))
                screen_name = str(tweet.get('screen_name'))
                usr_name = str(tweet.get('name'))
                loc = str(tweet.get('location'))
                desc = str(tweet.get('description'))
                foll = str(tweet.get('followers_count'))
                frie = str(tweet.get('friends_count'))
                listed = str(tweet.get('listed_count'))
                faves = str(tweet.get('favourites_count'))
                geo = str(tweet.get('geo_enabled'))
                veri = str(tweet.get('verified'))
                date = str(tweet.get('created_at'))
                twts = str(tweet.get('statuses_count'))
                lang = str(tweet.get('lang'))
                row = (usr_id + screen_name + usr_name + loc + desc + foll + frie + listed + faves + geo + veri + date + twts + lang)
                with open('users3.csv', 'a+',encoding="utf-8") as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(row)
                counter3 = counter3 + 1
                if counter3 % 1000 == 0:
                    print("Line "+str(counter3)+"of users3_flat.csv")
        return

getcsv(jsonllist)






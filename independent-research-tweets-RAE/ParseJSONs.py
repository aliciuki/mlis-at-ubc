# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:43:30 2019

@author: Alicia
"""
import csv
import jsonlines
import os

jsonl = [files for files in os.listdir("C:\\Users\\Alicia\\Dropbox\\RAE\\JSONdata\\OriginalTwitterJSONs")]
users = [files for files in os.listdir("C:\\Users\\Alicia\\Dropbox\\RAE\\JSONdata\\UsersJSONL")]
tweets = [files for files in os.listdir("C:\\Users\\Alicia\\Dropbox\\RAE\\JSONdata\\TweetsJSONL")]
entities = [files for files in os.listdir("C:\\Users\\Alicia\\Dropbox\\RAE\\JSONdata\\EntitiesJSONL")]
hashtags = [files for files in os.listdir("C:\\Users\\Alicia\\Dropbox\\RAE\\JSONdata\\HashtagsJSONL")]
mentions = [files for files in os.listdir("C:\\Users\\Alicia\\Dropbox\\RAE\\JSONdata\\MentionsJSONL")]


def getusers(f):
        for i in f:
            with jsonlines.open(f) as reader:
                counter = 0
                for tweet in reader:
                    user = tweet.get('user')
                    with jsonlines.open("users.jsonl") as writer:
                        writer.write(user)
                        counter = counter + 1
                        if counter % 1000 == 0:
                            print("Line "+str(counter)+"of "+str(f))
        return



def getentities(file):
    for i in file:
        with jsonlines.open(file) as reader:
            counter = 0
            for tweet in reader:
                id_str = tweet.get('id_str')
                entity = tweet.get('entities')
                with jsonlines.open("C:\\Users\\Alicia\\Dropbox\\RAE\\JSONdata\\EntitiesJSONL\\entities.jsonl") as writer:
                    entities = str(id_str)+","+str(entity)+'\n'
                    writer.write(entities)
                    counter = counter + 1
                    if counter % 1000 == 0:
                        print("Line "+str(counter)+"of "+str(file))
        return

def gettweets(t):
    for i in t:
        with jsonlines.open(t) as reader:
            counter2 = 0
            for tweet in reader:
                date = tweet.get('created_at')
                id_str = tweet.get('id_str')
                full_text = tweet.get('full_text')
                source = tweet.get('source')
                reply_s_id = tweet.get('in_reply_to_status_id_str')
                reply_u_id = tweet.get('in_reply_to_user_id_str')
                reply_sname = tweet.get('in_reply_to_screen_name')
                tw_sname = tweet.get('user', {}).get('screen_name')
                tw_author = tweet.get('user', {}).get('id_str')
                qtd_s_id = tweet.get('quoted_status_id_str')
                rt_s_id = tweet.get('retweeted_status.id_str')
                is_q = tweet.get('is_quote_status')
                quote_c = tweet.get('quote_count')
                reply_c = tweet.get('reply_count')
                rt_c = tweet.get('retweet_count')
                fave_c = tweet.get('favorite_count')
                t = dict()
                t.append(date)
                t.append(id_str)
                t.append(tw_author)
                t.append(full_text)
                t.append(source)
                t.append(reply_s_id)
                t.append(reply_u_id)
                t.append(reply_sname)
                t.append(tw_sname)
                t.append(tw_author)
                t.append(qtd_s_id)
                t.append(rt_s_id)
                t.append(is_q)
                t.append(quote_c)
                t.append(reply_c)
                t.append(rt_c)
                t.append(fave_c)
                with jsonlines.open('tweets.jsonl') as writer:
                    writer.write(t)
                    counter2 = counter2 + 1
                    if counter2 % 5000 == 0:
                        print("Line "+str(counter2)+" of "+str(t))
    return

def places(p):
    with jsonlines.open(p) as reader:
        counter1 = 0
        for tweet in reader:
            id_str = tweet.get('id_str')
            place = tweet.get('place')
            tw_author = tweet.get('user', {}).get('id_str')
            pla_row = dict()
            pla_row.append(id_str)
            pla_row.append(place)
            pla_row.append(tw_author)
            with jsonlines.open('places.jsonl') as writer:
                writer.write(pla_row)
            counter1 = counter1 + 1
            if counter1 % 5000 == 0:
                print("Line "+str(counter1)+" of "+str(p))
    return

def userscsv(jsonllist):
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




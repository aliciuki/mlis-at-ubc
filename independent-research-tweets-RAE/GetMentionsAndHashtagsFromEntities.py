# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 23:01:36 2019

@author: Alicia

Reads a JSONL containing the Twitter ENTITY object and writes the HASHTAGS and the MENTIONS to separate JSONL files.

"""

import jsonlines
"""
These guys count lines so I can know what's happening
"""

linecount1 = 0
linecount2 = 0
linecount3 = 0
counter1 = 0
counter2 = 0
counter3 = 0

"""
This section extracts and writes HASHTAGS from 3 input and to 3 output JSONL files.
"""

with jsonlines.open('hashtags3.jsonl', mode='w') as writer:     
    with jsonlines.open("raeconsultas.jsonl") as reader:
        for tweet in reader:
            htweet = []
            id_str = tweet.get('id_str')
            entity = tweet.get('entities')
            hsh = entity.get('hashtags', {})
            try:
                htweet.append(id_str)
            except:
                print("Appending 'id_str' to 'htweet' (list) didn't work")
            try:
                htweet.append(hsh)
            except:
                print("Appending 'hsh' to 'htweet' (list) didn't work")
            try:
                writer.write(htweet)
            except:
                print("Writing to 'hashtags3.json' did not work.")            
            counter3 = counter3 + 1
            if counter2 % 1000 == 0:
                print("Line "+str(counter3)+" of raeconsultas hashtags.")                
with jsonlines.open('hashtags2.jsonl', mode='w') as writer:   
    with jsonlines.open("ATRAEInforma2.jsonl") as reader:
        for tweet in reader:
            htweet = []
            id_str = tweet.get('id_str')
            entity = tweet.get('entities')
            hsh = entity.get('hashtags', {})
            try:
                htweet.append(id_str)
            except:
                print("Appending 'id_str' to 'htweet' (list) didn't work")
            try:
                htweet.append(hsh)
            except:
                print("Appending 'hsh' to 'htweet' (list) didn't work")
            try:
                writer.write(htweet)
            except:
                print("Writing to 'hashtags2.json' did not work.")            
            counter2 = counter2 + 1
            if counter2 % 1000 == 0:
                print("Line "+str(counter2)+" of ATRAEInforma2 hashtags.")
with jsonlines.open('hashtags1.jsonl', mode='w') as writer:   
    with jsonlines.open("RAEInforma.jsonl") as reader:
        for tweet in reader:
            htweet = []
            id_str = tweet.get('id_str')
            entity = tweet.get('entities')
            hsh = entity.get('hashtags', {})
            try:
                htweet.append(id_str)
            except:
                print("Appending 'id_str' to 'htweet' (list) didn't work")
            try:
                htweet.append(hsh)
            except:
                print("Appending 'hsh' to 'htweet' (list) didn't work")
            try:
                writer.write(htweet)
            except:
                print("Writing to 'hashtags1.json' did not work.")            
            counter1 = counter1 + 1
            if counter2 % 1000 == 0:
                print("Line "+str(counter1)+" of RAEInforma hashtags.")
"""
This section extracts and writes MENTIONS from 3 input and to 3 output JSONL files.
"""
with jsonlines.open('mentions3.jsonl', mode='w') as writer:     
    with jsonlines.open("raeconsultas.jsonl") as reader:
        for tweet in reader:
            mtweet = []
            id_str = tweet.get('id_str')
            entity = tweet.get('entities')
            men = entity.get('user_mentions', {})
            try:
                mtweet.append(id_str)
            except:
                print("Appending 'id_str' to 'htweet' (list) didn't work")
            try:
                mtweet.append(men)
            except:
                print("Appending 'men' to 'mtweet' (list) didn't work")
            try:
                writer.write(mtweet)
            except:
                print("Writing to 'hashtags2.json' did not work.")            
            linecount3 = linecount3 + 1
            if linecount3 % 1000 == 0:
                print("Line "+str(linecount3)+" of raeconsultas mentions.")
with jsonlines.open('mentions2.jsonl', mode='w') as writer:   
    with jsonlines.open("ATRAEInforma2.jsonl") as reader:
        for tweet in reader:
            mtweet = []
            id_str = tweet.get('id_str')
            entity = tweet.get('entities')
            men = entity.get('user_mentions', {})
            try:
                mtweet.append(id_str)
            except:
                print("Appending 'id_str' to 'htweet' (list) didn't work")
            try:
                mtweet.append(men)
            except:
                print("Appending 'men' to 'mtweet' (list) didn't work")
            try:
                writer.write(mtweet)
            except:
                print("Writing to 'mentions2.jsonl' did not work.")            
            linecount2 = linecount2 + 1
            if linecount2 % 1000 == 0:
                print("Line "+str(linecount2)+" of ATRAEInforma2 mentions.")
with jsonlines.open('mentions1.jsonl', mode='w') as writer:   
    with jsonlines.open("RAEInforma.jsonl") as reader:
        for tweet in reader:
            mtweet = []
            id_str = tweet.get('id_str')
            entity = tweet.get('entities')
            men = entity.get('user_mentions', {})
            try:
                mtweet.append(id_str)
            except:
                print("Appending 'id_str' to 'htweet' (list) didn't work")
            try:
                mtweet.append(men)
            except:
                print("Appending 'men' to 'mtweet' (list) didn't work")
            try:
                writer.write(mtweet)
            except:
                print("Writing to 'mentions1.json' did not work.")            
            linecount1 = linecount1 + 1
            if linecount1 % 1000 == 0:
                print("Line "+str(linecount1)+" of RAEInforma mentions.")

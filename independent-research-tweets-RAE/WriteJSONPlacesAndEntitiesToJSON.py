# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:42:19 2019

@author: Alicia
"""
import jsonlines

placefile = 'RAEPla0.jsonl'
entfile = 'RAEEnt0.jsonl'

with jsonlines.open('RAEInforma.jsonl') as reader:
    counter1 = 0
    for tweet in reader:
        id_str = tweet.get('id_str')
        place = tweet.get('place')
        tw_author = tweet.get('user', {}).get('id_str')
        pla_row = dict()
        pla_row.append(id_str)
        pla_row.append(place)
        pla_row.append(tw_author)
        with jsonlines.open('RAEInforma.jsonl') as writer:
			writer.write(pla_row)
        counter1 = counter1 + 1
        if counter1 % 5000 == 0:
            print("Line "+str(counter1)+" of "+str(placefile))

with jsonlines.open('RAEInforma.jsonl') as reader:
    counter2 = 0
    for tweet in reader:
        id_str = tweet.get('id_str')
        tw_author = tweet.get('user', {}).get('id_str')
        entity = tweet.get('entities')
		ent_row = dict()
		ent_row.append(id_str)
		ent_row.append(tw_author)
		ent_row.append(ent)
		with jsonlines.open('RAEInforma.jsonl') as writer:
			writer.write(ent_row)
        counter2 = counter2 + 1
        if counter2 % 5000 == 0:
            print("Line "+str(counter2)+" of "+str(entfile))
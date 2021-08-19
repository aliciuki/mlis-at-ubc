# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 19:21:19 2019

@author: Alicia
"""

import jsonlines
import csv

with jsonlines.open('RAEInforma.jsonl') as reader:
    counter1 = 0
    for tweet in reader:
        text = tweet.get('full_text')
        textfile = open('RAE_texts.txt','a+',encoding='utf-8')
        textfile.write(str(text)+"\n")
        counter1 = counter1 + 1
        if counter1 % 5000 == 0:
            print("Line "+str(counter1)+" of RAE_texts.txt")
with jsonlines.open('ATRAEInforma2.jsonl') as reader:
    counter1 = 0
    for tweet in reader:
        text = tweet.get('full_text')
        textfile = open('ATRAE_texts.txt','a+',encoding='utf-8')
        textfile.write(str(text)+"\n")
        counter1 = counter1 + 1
        if counter1 % 5000 == 0:
            print("Line "+str(counter1)+" of ATRAE_texts.txt")
with jsonlines.open('raeconsultas.jsonl') as reader:
    counter1 = 0
    for tweet in reader:
        text = tweet.get('full_text')
        textfile = open('raeconsultas_texts.txt','a+',encoding='utf-8')
        textfile.write(str(text)+"\n")
        counter1 = counter1 + 1
        if counter1 % 5000 == 0:
            print("Line "+str(counter1)+" of raeconsultas_texts.txt")
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:06:47 2019

@author: Alicia
"""

import jsonlines
import ast

# Reads a text file (or csv) that is formatted as multiple Python dictionaries (one each line of text)
# and writes it into a JSONL.

with jsonlines.open('users3.jsonl', mode='w') as writer:
    with open('users3.csv','r',encoding='utf-8') as s:
        count3 = 0
        for l in s:
            dictu = []
            try:
                dictionary = ast.literal_eval(l)
            except:
                print("eval didn't work")
            try:
                dictu.append(dictionary)
            except:
                print("Appending dictionary didn't work")
            try:
                writer.write(dictu)
            except:
                print("Writing dictionary into jsonlines outfile didn't work")
            count3 = count3 + 1
            if count3 % 1000 == 0:
                print("Line "+str(count3)+" of users3.csv")

with jsonlines.open('users2.jsonl', mode='w') as writer:
    with open('users2.csv','r',encoding='utf-8') as s:
        count2 = 0
        for l in s:
            dictu = []
            try:
                dictionary = ast.literal_eval(l)
            except:
                print("eval didn't work")
            try:
                dictu.append(dictionary)
            except:
                print("Appending dictionary didn't work")
            try:
                writer.write(dictu)
            except:
                print("Writing dictionary into jsonlines outfile didn't work")
            count2 = count2 + 1
            if count2 % 1000 == 0:
                print("Line "+str(count2)+" of users2.csv")

with jsonlines.open('users.jsonl', mode='w') as writer:
    with open('users.csv','r',encoding='utf-8') as s:
        count = 0
        for l in s:
            dictu = []
            try:
                dictionary = ast.literal_eval(l)
            except:
                print("eval didn't work")
            try:
                dictu.append(dictionary)
            except:
                print("Appending dictionary didn't work")
            try:
                writer.write(dictu)
            except:
                print("Writing dictionary into jsonlines outfile didn't work")
            count = count + 1
            if count % 1000 == 0:
                print("Line "+str(count)+" of users.csv")
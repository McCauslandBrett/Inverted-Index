#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:29:44 2019
References: https://stackabuse.com/read-a-file-line-by-line-in-python/
@author: Brettmccausland
"""

import math
import glob
import errno
import os

import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import operator
from operator import itemgetter, attrgetter
from sklearn.preprocessing import Imputer
from sklearn.cross_validation import train_test_split

import pandas as pd
from collections import namedtuple
import pandas as pd


class term:
    def __init__(self,numdocs,postings):
        self.numdocs=numdocs
        self.postings=postings
        
    def insertposting(self,post):
        self.postings.insert(0,post)
    def incrdocfreq(self,fname):
        for t in self.postings:
          if fname in t:
              t[1]=t[1]+1
    def existposting(self,fname):
        for t in self.postings:
          if fname in t:
              return True
        return False
    def incrnumdoc(self):
        self.numdocs+=1
        

def load_stops(stopwords,path):

 spath = path + "/*.txt"
 files = glob.glob(spath)
 for fname in files:
     with open(fname) as f: #file
         cnt = 0
         for line in f:
             line_process(line.strip().split(' '), stopwords)
             cnt += 1

def line_process(line, stopwords):
   for word in line:
       stopwords.insert(0,word.lower())

# dict_term={term,#docs,postings{fname,docFreq}}

def word_count(line, dict_terms,dict_docs,fname):
   for word in line:
       if word not in stopwords:
           dict_docs[fname] += 1
           if word.lower() in dict_terms:
               curterm= dict_terms[word.lower()]
               if curterm.existposting(fname):
                   curterm.incrdocfreq(fname)
               else:
                   curterm.incrnumdoc()
                   post={fname,1}
                   curterm.insertposting(post)
               print(" ")
               #dict_terms[word.lower()] += 1
           else:
               postings=[]
               postings.insert(0,{fname,1})
               t =term(1,postings)
               dict_terms[word.lower()] = t

def loadWcountWDoc(dict_terms,dict_docs,path):
 filenum= 1
 spath = path + "/*.txt"
 files = glob.glob(spath)
 for fname in files:
     filename="file" + str(filenum)
     filenum+=1
     dict_docs[filename] = 0
     with open(fname) as f: #file
         for line in f:
             word_count(line.strip().split(' '),dict_terms,dict_docs, filename)



# load stop words
stopwords=[]
path1="s"
load_stops(stopwords,path1)

# load distionary with counts

dict_terms={}
dict_docs={}
path2="data"
letssee=[]
loadWcountWDoc(dict_terms,dict_docs,path2)


















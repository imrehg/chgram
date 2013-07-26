#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import operator

maxn = 3

ngram = {}
for i in range(1, maxn+1):
    ngram[i] = {}

skipped = [u'，', u'。', u'」', u'「', u'、',
           u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9',
           ]

def parse(text):
    lastchar = u''
    for ch in text:
        if ch in skipped:
            lastchar = u''
            continue

        if ch in ngram[1]:
            # print "Found: ", ch
            ngram[1][ch] += 1
        else:
            ngram[1][ch] = 1



        lastchar += ch

def pullfile(filename):
    f = open(filename, 'r')
    for line in f.readlines():
        parse(line.decode('utf-8'))

    sorted_x = sorted(ngram[1].iteritems(), key=operator.itemgetter(1))
    sorted_x.reverse()
    for i in range(20):
        print "%s : %d " %(sorted_x[i][0], sorted_x[i][1])


fn = "wikipedia/taiwan.txt"
pullfile(fn)


    

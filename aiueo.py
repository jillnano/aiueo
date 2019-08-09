#!/usr/bin/python
#coding=UTF-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import re
# import json
import random

pyPath = os.path.dirname(os.path.realpath(__file__))

pLine = re.compile(r'<div class="para" label-module="para">(.{1,3})</div>')
html = open(os.path.join(pyPath, '50.html'), 'r').read()
html = html.decode('utf8')
allList = pLine.findall(html)
# print len(allList)
titleList = [u'清音', u'拨音', u'浊音', u'半浊音', u'拗音']
aiueoDict = {}
num = 0
title = None
for i in allList:
	if i in titleList:
		title = i
		aiueoDict.setdefault(i, [])
	else:
		num = num + 1
		if num == 1:
			aiueoDict[title].append([])
		aiueoDict[title][-1].append(i)
		if num == 3:
			num = 0
# print json.dumps(aiueoDict)

testType = raw_input('type 读音; 假名; 单词: ')
count = 0
right = 0
if testType == '1':
	title = raw_input('title %s: '%('; '.join(titleList)))
	data = []
	for t in title:
		if t.isdigit():
			data.extend(aiueoDict[titleList[int(t) - 1]])
	questionList = []
	for qLine in data:
		questionList.extend([[qLine[0], qLine[2]], [qLine[1], qLine[2]]])
	random.shuffle(questionList)
	for q, a in questionList:
		count += 1
		ret = raw_input(q + ': ')
		if ret == a:
			right += 1
			print 'right:', ' / '.join([q, a])
		else:
			print '\033[1;31merror\033[0m:', ' / '.join([q, a])
		print 'all: %s; right: %s; score: %.2f'%(count, right, (float(right) / count) * 100)
elif testType == '2':
	title = raw_input('title %s: '%('; '.join(titleList)))
	data = []
	for t in title:
		if t.isdigit():
			data.extend(aiueoDict[titleList[int(t) - 1]])
	while True:
		count += 1
		qLine = random.choice(data)
		q = qLine[-1]
		ret1 = raw_input(u'平假名%s: '%q)
		ret2 = raw_input(u'片假名%s: '%q)
		if ret1 in qLine and ret2 in qLine:
			right += 1
			print 'right:', ' / '.join(qLine)
		else:
			print '\033[1;31merror\033[0m:', ' / '.join(qLine)
		print 'all: %s; right: %s; score: %.2f'%(count, right, (float(right) / count) * 100)
elif testType == '3':
	wordList = open(os.path.join(pyPath, '新编日语修订版第一册单词(含词例全).csv'), 'r').readlines()
	wordList = filter(lambda x: x.split(',')[2].strip(), wordList)
	wordList = [(i.split(',')[0].strip(), i.split(',')[1].strip(), i.split(',')[2].strip(), i.split(',')[4].strip()) for i in wordList]
	random.shuffle(wordList)
	for i in wordList:
		raw_input(' | '.join(i))
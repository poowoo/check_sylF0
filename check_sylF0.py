# -*- coding: utf8 -*-
import sys
import os
from enum import Enum

#Tags = Enum('tags','index syl begin end accent lf0')
class Tags(Enum):
	index = 0
	syl = 1
	begin = 2
	end = 3
	accent = 4
	lf0 = 5
#Usage: filename log
def check_toks(toks):

	if len(toks) != 6:
		return -1
	if float(toks[2]) == float(toks[3]) == 0.0:
		return -1

def check_F0_exist(F0s):	

	for F0 in F0s:		
		if F0.isnumeric() == False:
			return -1
	return 0

def get_dur(toks):
	
	dur = float(toks[Tags.end.value]) - float(toks[Tags.begin.value])
	return dur

def get_lf0s_avg(toks):

	lf0s = toks[Tags.lf0.value].split("-")
	lf0s_avg = 0

	for lf0 in lf0s:
		lf0s_avg += float(lf0)
	return float(lf0s_avg)/float(len(lf0s))

def get_lf0s_slope_avg(toks):

	lf0s = toks[Tags.lf0.value].split("-")
	lf0s_slopes = []
	lf0s_slope_avg = 0
	
	for lf0 in lf0s:		
		if lf0s.index(lf0) + 1 < len(lf0s):			
			lf0s_slopes.append(abs(int(lf0) - int(lf0s[lf0s.index(lf0) + 1])))

	for lf0_slope in lf0s_slopes:
		lf0s_slope_avg += lf0_slope
	
	return float(lf0s_slope_avg)/float(len(lf0s_slopes))

if __name__ == '__main__':	
	
	#out = open(sys.argv[2], mode='a', encoding='utf8')
	with open('Utt_00001.SylF0', mode='r', encoding='utf-16-le') as file:
		
		lines = file.readlines()						
		lf0s_avg = []
		durs = []
		lf0s_slope_avg = []
		i = 0
		while i < len(lines):
			line = lines[i].strip()				
			toks = [x for x in line.split(" ") if x != '']
			if check_toks(toks) == -1:
				break
			durs.append(get_dur(toks))
			lf0s_avg.append(get_lf0s_avg(toks))
			lf0s_slope_avg.append(get_lf0s_slope_avg(toks))
			i += 1
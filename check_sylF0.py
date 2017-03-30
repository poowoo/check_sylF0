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
			lf0_slope = abs(int(lf0) - int(lf0s[lf0s.index(lf0) + 1]))		
			lf0s_slopes.append(lf0_slope)
			lf0s_slope_avg += lf0_slope	
	
	return float(lf0s_slope_avg)/float(len(lf0s_slopes))

def cal_avg_dur(durs):

	avg_dur = 0
	for phone_dur in durs:
		avg_dur += phone_dur

	return float(avg_dur)/float(len(durs))

def cal_avg_lf0s_avg(lf0s_avgs):

	avg_lf0s_avg = 0
	for phone_lf0_avg in lf0s_avgs:
		avg_lf0s_avg += phone_lf0_avg

	return float(avg_lf0s_avg)/float(len(lf0s_avgs))
	
def cal_avg_lf0s_slope_avg(lf0s_slope_avgs):

	avg_lf0s_slope_avg = 0
	for phone_lf0s_slope_avg in lf0s_slope_avgs:
		avg_lf0s_slope_avg += phone_lf0s_slope_avg

	return float(avg_lf0s_slope_avg)/float(len(lf0s_slope_avgs))
	
if __name__ == '__main__':	
	
	#out = open('test.txt', mode='w', encoding='utf8')
	with open('Utt_00001.SylF0', mode='r', encoding='utf-16-le') as file:
		syls = []
		lf0s_avg = []
		durs = []
		lf0s_slope_avg = []
		avg_dur = 0
		avg_lf0s_avg = 0
		avg_lf0s_slope_avg = 0
		i = 0
		emotion = 0
		lines = file.readlines()						
		lines[0] = lines[0][1:] # remove BOM
		while i < len(lines):
			
			line = lines[i].strip()				
			toks = [x for x in line.split(" ") if x != '']
			if check_toks(toks) == -1:
				break
			syls.append(toks[Tags.syl.value])
			durs.append(get_dur(toks))
			lf0s_avg.append(get_lf0s_avg(toks))
			lf0s_slope_avg.append(get_lf0s_slope_avg(toks))
			i += 1

		avg_dur = cal_avg_dur(durs)
		avg_lf0s_avg = cal_avg_lf0s_avg(lf0s_avg)
		avg_lf0s_slope_avg = cal_avg_lf0s_slope_avg(lf0s_slope_avg)
		i = 0
		print('syls' + '\t \t' + 'durs' + '\t' + 'lf0s_avg[i]'  + '\t' + 'lf0s_slope_avg')
		while i < len(lines):

			#if durs[i] > avg_dur * 1.25 or durs[i] < avg_dur * 0.75:
			#	emotion = 1

			if lf0s_avg[i] > (avg_lf0s_avg * 1.25):
				emotion = 1

			if lf0s_slope_avg[i] > (avg_lf0s_slope_avg * 1.25):
				emotion = 1

			if emotion == 1:
				print(syls[i] + '\t*\t' + str(round(durs[i],4)) + '\t' + str(round(lf0s_avg[i],4))  + '\t' +  str(round(lf0s_slope_avg[i],4)))
				emotion = 0
			else:
				print(syls[i] + '\t \t' + str(round(durs[i],4)) + '\t' + str(round(lf0s_avg[i],4))  + '\t' +  str(round(lf0s_slope_avg[i],4)))

			i += 1
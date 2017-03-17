# -*- coding: utf8 -*-
import sys
import os

#Usage: filename log
def check_toks(F0s):

	if len(toks) != 6:
		return -1
	if float(toks[2]) == float(toks[3]) == 0.0:
		return -1

def check_F0_exist(F0s):	

	for F0 in F0s:		
		if F0.isnumeric() == False:
			return -1
	return 0

if __name__ == '__main__':	
	
	out = open(sys.argv[2], mode='a', encoding='utf8')
	with open(sys.argv[1], mode='r', encoding='utf-16-le') as file:
		
		lines = file.readlines()		
		check = 0
		i = 0	
		while i < len(lines):
			line = lines[i].strip()				
			toks = [x for x in line.split(" ") if x != '']
			if check_toks(toks) == -1:
				out.write("error: in " + sys.argv[1] + " line: " + str(i) + " syllables: " + str(toks)+"\n")				
				check = -1
			else:
				F0 = toks[-1].split("-")
				if check_F0_exist(F0) == -1:								
					out.write("error: in " + sys.argv[1] + " line: " + str(i) + " syllables: " + str(toks)+"\n")				
					check = -1			
						
			i += 1
		if check == 0:
			out.write(sys.argv[1] + " is correct\n")			
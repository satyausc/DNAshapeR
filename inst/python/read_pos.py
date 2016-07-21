import sys
from collections import defaultdict
def parse_position_and_seq_names (filename):
	position_list = defaultdict (list)
	pos_names = []
	f = open (filename, "r");
	tmppos = ""
	for line in f:
		line = line.strip()
		if line == "":
			continue 
		elif ">" in line:
			pos_name = line[1:]
			for seq in f:
				seq = seq.strip()
				if seq == "":
					continue
				if ">" in seq:
					position_list[pos_name].append(tmppos)
					tmppos = ""
					pos_names.append(pos_name)
					pos_name = seq [1:]
				else:
					tmppos = tmppos + seq

			position_list[pos_name].append(tmppos)	
			pos_names.append(pos_name)
		else:
			pos_name = "1"
			position_list[pos_name].append(line)
			for l in f:
				l = l.strip()
				position_list[pos_name].append(l)
			
	return position_list, pos_names



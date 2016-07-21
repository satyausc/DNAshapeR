import sys

def structure_parameter_prediction (filename):
	sequence_list = defaultdict (list)
	seq_names = []
	f = open (filename, "r");
	tmpseq = ""
	for line in f:
		line = line.strip()
		if line == "":
			continue 
		elif ">" in line:
			seq_name = line[1:]
			#MGW.write("%s\n"%line)
			#ProT.write("%s\n"%line)
			#Roll.write("%s\n"%line)
			#HelT.write("%s\n"%line)
			for seq in f:
				seq = seq.strip()
				if seq == "":
					continue
				if ">" in seq:
					sequence_list[seq_name].append(tmpseq)
					isvalid = check (sequence_list[seq_name][0])
					if isvalid == False: 
						sequence_list[seq_name] = "invalid"
					tmpseq = ""
					seq_names.append(seq_name)
					seq_name = seq [1:]
				else:
					seq = seq.upper()
					tmpseq = tmpseq + seq

			sequence_list[seq_name].append(tmpseq)	
			seq_names.append(seq_name)
		else:
			seq_name = "1"
			line = line.upper()
			sequence_list[seq_name].append(line)
			for l in f:
				l = l.strip()
				l = l.upper()
				sequence_list[seq_name].append(l)
			isvalid = check(sequence_list[seq_name][0])
			seq_names.append(seq_name)
			if isvalid == False: 
				sequence_list["1"] = "invalid"
			
	return sequence_list, seq_names



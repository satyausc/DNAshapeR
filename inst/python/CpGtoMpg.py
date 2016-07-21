import sys
import os.path  
from collections import defaultdict 
def CpGtoMpg (filename, pos_fasta, out_filename): 
	if out_filename == "": 
		extension = os.path.splitext(filename)[1]
		fname = os.path.splitext(filename)[1]
		out_filename 
	if pos_fasta != "": 
		sequence_list, seq_names = structure_parameter_prediction (filename)
		pos_list, pos_names	 = parse_position_and_seq_names (pos_fasta)
		
		ofp = open (out_filename, "w")
		
		for seq_name in seq_names:
			if seq_name in pos_names: 
				pos_name = seq_name
				indices_to_be_converted_to_M = map (int, pos_list[pos_name][0].split(',')) 
				tmp_seq = list (sequence_list[pos_name][0])
				for idx in indices_to_be_converted_to_M:
					tmp_seq[idx-1] = 'M'
					tmp_seq[idx] = 'g'
				seq = ''.join (tmp_seq)
				ofp.write(">"+pos_name+"\n")
				ofp.write(seq+"\n")
			else: 
				ofp.write(">"+seq_name+"\n")
				ofp.write(sequence_list[seq_name][0]+"\n")
		message = "## A new file " + out_filename + " containing Mpg step(s) in sequence(s) at specified positions"
		ofp.close ()
		return message
	else: 
		sequence_list, seq_names = structure_parameter_prediction (filename)
		ofp = open (out_filename, "w")
		for seq_name in seq_names: 
			sequence_list[seq_name][0] = sequence_list[seq_name][0].replace("CG", "Mg")
			ofp.write (">"+seq_name+"\n")
			ofp.write (sequence_list[seq_name][0]+"\n") 
		message = "## A new file " + out_filename + " containing Mpg step(s) in sequence(s) at specified positions"
		ofp.close ()
		return message

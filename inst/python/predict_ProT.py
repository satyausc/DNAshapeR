import sys

def predict_ProT (sequence, keys_query_table, sequence_len, QueryTable):
	prot_at_positions = []
	prot_at_positions.append('NA')
	prot_at_positions.append('NA')
	length = sequence_len
	for i in range (0,length - 4 ):
		pentamer = sequence[i:i+5]
		rev_pentamer = revcompl (pentamer)
		if pentamer in keys_query_table:
			
			prot_at_positions.append('%.2f' % QueryTable[pentamer][6])
		elif rev_pentamer in keys_query_table: 
			prot_at_positions.append('%.2f' % QueryTable[rev_pentamer][6])
		else:
			prot_at_positions.append('0.0')
	prot_at_positions.append ('NA')
	prot_at_positions.append ('NA')
	return prot_at_positions



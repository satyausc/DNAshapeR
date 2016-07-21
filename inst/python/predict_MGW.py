import sys

def predict_MGW (sequence, keys_query_table, sequence_len, QueryTable):
	mgw_at_positions = []
	mgw_at_positions.append('NA')
	mgw_at_positions.append('NA')
	length = sequence_len
	for i in range (0,length - 4 ):
		pentamer = sequence[i:i+5]
		rev_pentamer = revcompl (pentamer)
		if pentamer in keys_query_table:
			
			mgw_at_positions.append('%.2f' % QueryTable[pentamer][0])
		elif rev_pentamer in keys_query_table: 
			mgw_at_positions.append('%.2f' % QueryTable[rev_pentamer][0])
		else:
			mgw_at_positions.append('0.0')
	mgw_at_positions.append ('NA')
	mgw_at_positions.append ('NA')
	return mgw_at_positions



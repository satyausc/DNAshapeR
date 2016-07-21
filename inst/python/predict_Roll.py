import sys

def predict_Roll (sequence, keys_query_table, sequence_len, QueryTable):
	roll_at_positions = []
	roll_at_positions.append('NA')
	first_pentamer = sequence[0:5]
	rev_first_pentamer = revcompl(first_pentamer)
	length = sequence_len
	if first_pentamer in keys_query_table: 
		roll_at_positions.append('%.2f' % QueryTable[first_pentamer][15])
	elif rev_first_pentamer in keys_query_table:
		roll_at_positions.append('%.2f' % QueryTable[rev_first_pentamer][18])
		
	else:
		roll_at_positions.append('0.0')
	for j in range (2, length - 1  ):
		if j == length - 2:
			roll_at_positions.append ('NA')	
			continue
		if j == length - 3: 
			f1_index = j - 2
			last_pentamer = sequence [f1_index:f1_index+5]
			rev_last_pentamer = revcompl(last_pentamer)
			if last_pentamer in keys_query_table:
				roll_at_positions.append('%.2f' % QueryTable[last_pentamer][18])
			elif rev_last_pentamer in keys_query_table: 
				roll_at_positions.append('%.2f' % QueryTable[rev_last_pentamer][15])
			else:
				roll_at_positions.append('0.0')
			continue
		else:
			f1_index = j -1 
			f2_index = j -2 
			flag1 = True
			flag2 = True
			pentamer1 = sequence [f1_index: f1_index + 5]	
			pentamer2 = sequence [f2_index: f2_index + 5]	
			rev_pentamer1 = revcompl(pentamer1)
			rev_pentamer2 = revcompl(pentamer2)
			
			if pentamer1 in keys_query_table:
				value1 = QueryTable[pentamer1][15]
				#print value1
			elif rev_pentamer1 in keys_query_table: 
				value1 = QueryTable[rev_pentamer1][18]
			else:
				flag1 = False
				value1 = 0.0 
			if pentamer2 in keys_query_table:
				value2 = QueryTable[pentamer2][18]
			elif rev_pentamer2 in keys_query_table: 
				value2 = QueryTable[rev_pentamer2][15]
			else:
				flag2 = False
				value2 = 0.0 
		if flag1 and flag2: 
			value = (value1 + value2)/2
			roll_at_positions.append('%.2f' % value)
		elif flag1 and not flag2:
			roll_at_positions.append('%.2f' % value1)
		elif not flag1 and flag2: 
			roll_at_positions.append('%.2f' % value2)
		elif not flag1 and not flag2:
			roll_at_positions.append('0.0')
				 
	return roll_at_positions



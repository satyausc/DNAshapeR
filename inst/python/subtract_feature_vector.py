def subtract_feature_vector (feature_vector_1, feature_vector_2):
	delta = []	
	for idx in range (0,len(feature_vector_1)): 
		val1 = autoconvert(feature_vector_1[idx]) 
		val2 = autoconvert(feature_vector_2[idx]) 	
		if (type (val1) == str)   or (type (val2) == str ) : 
			delta.append (val1)	
		else: 
			delta_val = val1 - val2 
			delta.append ('%.2f' % delta_val)
	return delta


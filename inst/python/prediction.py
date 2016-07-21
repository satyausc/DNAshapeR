from collections import defaultdict
import os.path
def prediction (filename,
                width=30,
                delim=",",
                query_table = "QueryTable.methyl-DNAshape_with_M_and_g.dat"): 
	outfile_MGW = filename + "_unmeth.MGW"
	outfile_ProT = filename + "_unmeth.ProT"
	outfile_Roll = filename + "_unmeth.Roll"
	outfile_HelT = filename + "_unmeth.HelT"
	outfile_MGW_M = filename + "_meth.MGW"
	outfile_ProT_M = filename + "_meth.ProT"
	outfile_Roll_M = filename + "_meth.Roll"
	outfile_HelT_M = filename + "_meth.HelT"
	Delta_file_MGW = filename + "_Delta.MGW"
	Delta_file_ProT = filename + "_Delta.ProT"
	Delta_file_Roll = filename + "_Delta.Roll"
	Delta_file_HelT = filename + "_Delta.HelT"
	MGW =  open (outfile_MGW, "w") 
	ProT = open (outfile_ProT, "w")
	Roll = open (outfile_Roll, "w")
	HelT = open (outfile_HelT, "w")
	MGW_M =  open (outfile_MGW_M, "w") 
	ProT_M = open (outfile_ProT_M, "w")
	Roll_M = open (outfile_Roll_M, "w")
	HelT_M = open (outfile_HelT_M, "w")
	Delta_MGW =  open (Delta_file_MGW, "w") 
	Delta_ProT = open (Delta_file_ProT, "w")
	Delta_Roll = open (Delta_file_Roll, "w")
	Delta_HelT = open (Delta_file_HelT, "w")

	QueryTable = defaultdict(list)
		
	sequence_list, seq_names = structure_parameter_prediction (filename)
	QueryTable = load_query_table(query_table)
	keys_query_table = QueryTable.keys()
	
	########################
	# unmethylated calculation
	#
	########################
	for keys in seq_names:
		Delta_MGW_prediction = [] 
		Delta_ProT_prediction = [] 
		Delta_Roll_prediction = [] 
		Delta_HelT_prediction = [] 
		if len(sequence_list[keys][0]) < 5 or sequence_list[keys][0] == "invalid":
			#print ">",keys,"\n","sequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M )"
			MGW.write (">%s\nsequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M)\n"%keys)
			ProT.write(">%s\nsequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M)\n"%keys)
			Roll.write(">%s\nsequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M)\n"%keys)
			HelT.write(">%s\nsequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M)\n"%keys)
		
			#print ">",keys,"\n","sequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M )"
			MGW_M.write (">%s\nsequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M)\n"%keys)
			ProT_M.write(">%s\nsequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M)\n"%keys)
			Roll_M.write(">%s\nsequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M)\n"%keys)
			HelT_M.write(">%s\nsequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M)\n"%keys)
			
			Delta_MGW.write (">%s\nsequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M)\n"%keys)
			Delta_ProT.write(">%s\nsequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M)\n"%keys)
			Delta_Roll.write(">%s\nsequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M)\n"%keys)
			Delta_HelT.write(">%s\nsequence length is less than five or sequence is invalid (contains letters other than A,C,G,T,M)\n"%keys)
	
		else: 
			sequence = sequence_list[keys][0]
			sequence = sequence.replace("M","C")
			sequence_len = len(sequence)
			MGW_prediction  =  predict_MGW   (sequence, keys_query_table, sequence_len, QueryTable) 
			ProT_prediction =  predict_ProT  (sequence, keys_query_table, sequence_len, QueryTable)
			Roll_prediction =  predict_Roll  (sequence, keys_query_table, sequence_len, QueryTable)
			HelT_prediction =  predict_Twist  (sequence, keys_query_table, sequence_len, QueryTable)
	
			MGW.write (">%s\n"%keys)
			MGW_prediction = [MGW_prediction[i:i+width ] for i in range (0,sequence_len, width )]
			for i in MGW_prediction: 
				MGW.write("%s"%delim.join(i) + "\n")
			ProT.write (">%s\n"%keys)
			ProT_prediction = [ProT_prediction[i:i+width ] for i in range (0,sequence_len, width )]
			for i in ProT_prediction: 
				ProT.write("%s"%delim.join(i) + "\n")
			Roll.write (">%s\n"%keys)
			Roll_prediction = [Roll_prediction[i:i+width ] for i in range (0,sequence_len, width )]
			for i in Roll_prediction: 
				Roll.write("%s"%delim.join(i) + "\n")
			HelT.write (">%s\n"%keys)
			HelT_prediction = [HelT_prediction[i:i+width ] for i in range (0,sequence_len, width )]
			for i in HelT_prediction: 
				HelT.write("%s"%delim.join(i) + "\n")
				
    	#####################
    	#
    	#
    	#Methylated calculation with CG in center
    	#
    	####################
			if "M" not in sequence: 
				sequence = sequence.replace("CG","Mg")
			else: 
				sequence = sequence.replace("MG", "Mg")
			sequence_len = len(sequence)
			MGW_M_prediction =   predict_MGW_M   (sequence, keys_query_table, sequence_len, QueryTable) 
			ProT_M_prediction =  predict_ProT_M  (sequence, keys_query_table, sequence_len, QueryTable)
			Roll_M_prediction =  predict_Roll_M  (sequence, keys_query_table, sequence_len, QueryTable)
			HelT_M_prediction = predict_Twist_M  (sequence, keys_query_table, sequence_len, QueryTable)
	
			MGW_M.write (">%s\n"%keys)
			MGW_M_prediction = [MGW_M_prediction[i:i+width ] for i in range (0,sequence_len, width )]
			for i in MGW_M_prediction: 
				MGW_M.write("%s"%delim.join(i) + "\n")
			ProT_M.write (">%s\n"%keys)
			ProT_M_prediction = [ProT_M_prediction[i:i+width ] for i in range (0,sequence_len, width )]
			for i in ProT_M_prediction: 
				ProT_M.write("%s"%delim.join(i) + "\n")
			Roll_M.write (">%s\n"%keys)
			Roll_M_prediction = [Roll_M_prediction[i:i+width ] for i in range (0,sequence_len, width )]
			for i in Roll_M_prediction: 
				Roll_M.write("%s"%delim.join(i) + "\n")
			HelT_M.write (">%s\n"%keys)
			HelT_M_prediction = [HelT_M_prediction[i:i+width ] for i in range (0,sequence_len, width )]
			for i in HelT_M_prediction: 
				HelT_M.write("%s"%delim.join(i) + "\n")
			
			for i in range (0, len (MGW_prediction)) : 
				tmp = subtract_feature_vector (MGW_M_prediction[i] , MGW_prediction[i]) 
				Delta_MGW_prediction.append (tmp) 
			for i in range (0, len (ProT_prediction)) : 
				tmp = subtract_feature_vector (ProT_M_prediction[i] , ProT_prediction[i]) 
				Delta_ProT_prediction.append (tmp) 
			for i in range (0, len (Roll_prediction)) : 
				tmp = subtract_feature_vector (Roll_M_prediction[i] , Roll_prediction[i]) 
				Delta_Roll_prediction.append (tmp) 
			for i in range (0, len (HelT_prediction)) : 
				tmp = subtract_feature_vector ( HelT_M_prediction[i] , HelT_prediction[i]) 
				Delta_HelT_prediction.append (tmp) 
			
			Delta_MGW.write (">%s\n"%keys)
			for i in Delta_MGW_prediction: 
				Delta_MGW.write("%s"%delim.join(i) + "\n")
			Delta_ProT.write (">%s\n"%keys)
			for i in Delta_ProT_prediction: 
				Delta_ProT.write("%s"%delim.join(i) + "\n")
			Delta_Roll.write (">%s\n"%keys)
			for i in Delta_Roll_prediction: 
				Delta_Roll.write("%s"%delim.join(i) + "\n")
			Delta_HelT.write (">%s\n"%keys)
			for i in Delta_HelT_prediction: 
				Delta_HelT.write("%s"%delim.join(i) + "\n")
	return "Done"

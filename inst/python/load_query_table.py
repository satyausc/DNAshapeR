import sys

def load_query_table (filename):
	q_table = defaultdict(list)
	with open (filename, "r") as f:
		for line in f:
			line = line.strip()
			linelist = [item for item in line.split() if item ]
			pentamer = linelist[0]
			linelist = linelist[1:]
			for i, item in enumerate(linelist):
				q_table[pentamer].append(autoconvert(item))
	return q_table


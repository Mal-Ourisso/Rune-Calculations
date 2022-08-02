
def getLine(csv_file):
	line = csv_file.readline()
	if line:
		return line.replace("\n", "").split(",")

with open("stats_relations.csv", "r") as stats_relations:
	header = getLine(stats_relations)
	print(header)
	while True:	
		line = getLine(stats_relations)
		if not line:
			break
		print(line)

import csv
reader = csv.reader(open("dht22.csv"), delimiter=";")
for row in reader:
	print(row)
#alternativ einzelne Spalten auslesen
#for (k,v) in row.items():
	#columns[k].append(v)
#print(columns["timestamp"]
#print(columns["temperature"]

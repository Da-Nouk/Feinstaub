import csv
reader = csv.reader(open("dht22.csv"), delimiter=";")
for row in reader:
	print(row)

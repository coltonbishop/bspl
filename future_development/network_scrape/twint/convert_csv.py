import sys
import csv

csv.field_size_limit(sys.maxsize)

file = "ny_1km.csv"
i = 0 
with open(file, newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	data = []
	for row in spamreader:
		if i == 0:
			field_names = row[0].split(",")
			print(len(field_names))
			i += 1
		elif i % 100 and i < 10000:
			data.append(row)
			print(row)
			input("continue?")
			i += 1

with open('data.csv', 'w', newline='') as csvfile:

	writer = csv.DictWriter(csvfile, fieldnames=field_names)

	writer.writeheader()

	for dat in data:
		dic = {}
		i = 0
		for field in field_names:
			dic[field] = dat[i]
		writer.writerow(dic)
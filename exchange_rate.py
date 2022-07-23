import csv, requests

# URL for data parcing
url = 'https://www.akchabar.kg/ru/exchange-rates/'

# Data collecting
response = requests.get(url)
response.raise_for_status()

with open('collected_data.txt','wb') as f:
	for chunk in response.iter_content(100000):
		f.write(chunk)

# Proccessing the collected data
with open ('collected_data.txt') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter = ',')
	data=list(csv_reader)
	for index, column in enumerate(data):
		print(index,column)

# Save the proccessed data to csv file
with open('exchange-rates.csv','w',newline='') as f:
	csv_writer = csv.writer(f)
	csv_writer.writerow([data[144][0][29:37],data[145][0][33:36],
		data[145][0][40:45],data[145][1][0:5],data[146][0][33:36],
		data[146][0][41:45],data[146][1][0:5],data[147][0][33:36],
		data[147][0][40:45],data[147][1][0:5],data[148][0][33:36],
		data[148][0][40:45],data[148][1][0:5]])
	csv_writer.writerow([data[153][0][29:33],data[154][0][33:36],
		data[154][0][40:45],data[154][1][0:5],data[155][0][33:36],
		data[155][0][41:45],data[155][1][0:5],data[156][0][33:36],
		data[156][0][40:45],data[156][1][0:5],data[157][0][33:36],
		data[157][0][40:45],data[157][1][0:5]])
	csv_writer.writerow([data[162][0][29:32],data[163][0][33:36],
		data[163][0][40:45],data[163][1][0:5],data[164][0][33:36],
		data[164][0][41:45],data[164][1][0:5],data[165][0][33:36],
		data[165][0][40:45],data[165][1][0:5],data[166][0][33:36],
		data[166][0][40:45],data[166][1][0:5]])
	csv_writer.writerow([data[171][0][29:35],data[172][0][33:36],
		data[172][0][40:45],data[172][1][0:5],data[173][0][33:36],
		data[173][0][41:45],data[173][1][0:5],data[174][0][33:36],
		data[174][0][40:45],data[174][1][0:5],data[175][0][33:36],
		data[175][0][40:45],data[175][1][0:5]])
	csv_writer.writerow([data[180][0][29:32],data[181][0][33:36],
		data[181][0][40:45],data[181][1][0:5],data[182][0][33:36],
		data[182][0][41:45],data[182][1][0:5],data[183][0][33:36],
		data[183][0][40:45],data[183][1][0:5],data[184][0][33:36],
		data[184][0][40:45],data[184][1][0:5]])
	csv_writer.writerow([data[189][0][29:34],data[190][0][33:36],
		data[190][0][40:45],data[190][1][0:5],data[191][0][33:36],
		data[191][0][41:45],data[191][1][0:5],data[192][0][33:36],
		data[192][0][40:45],data[192][1][0:5],data[193][0][33:36],
		data[193][0][40:45],data[193][1][0:5]])
	csv_writer.writerow([data[200][0][29:34],data[201][0][33:36],
		data[201][0][40:45],data[201][1][0:5],data[202][0][33:36],
		data[202][0][41:45],data[202][1][0:5],data[203][0][33:36],
		data[203][0][40:45],data[203][1][0:5],data[204][0][33:36],
		data[204][0][40:45],data[204][1][0:5]])
	csv_writer.writerow([data[209][0][29:38],data[210][0][33:36],
		data[210][0][40:45],data[210][1][0:5],data[211][0][33:36],
		data[211][0][41:45],data[211][1][0:5],data[212][0][33:36],
		data[212][0][40:45],data[212][1][0:5],data[213][0][33:36],
		data[213][0][40:45],data[213][1][0:5]])
	csv_writer.writerow([data[218][0][29:37],data[219][0][33:36],
		data[219][0][40:45],data[219][1][0:5],data[220][0][33:36],
		data[220][0][41:45],data[220][1][0:5],data[221][0][33:36],
		data[221][0][40:45],data[221][1][0:5],data[222][0][33:36],
		data[222][0][40:45],data[222][1][0:5]])
	csv_writer.writerow([data[226][0][21:25],data[227][0][32:39],
		data[228][0][33:40],data[229][0][32:37],data[230][0][32:38]])
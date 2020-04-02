import requests
import csv
from datetime import datetime

fields = ['Date', 'Price']
date = []
date_monthwise = []
price = []
price_monthwise = []
rows =[]
rows_monthwise =[]

response = requests.get("https://api.eia.gov/series/?api_key=b808259a4fc11613193992a8b56196cb&series_id=NG.RNGWHHD.D")
print(response.status_code)
pass_times = response.json()['series']
for d in pass_times:
    data = d['data']

for x_row in data:
    datetimeobject = datetime.strptime(x_row[0],'%Y%m%d')
    newformat = datetimeobject.strftime('%d-%m-%Y')



    date.append(newformat)
    price.append(x_row[1])
i = 0
for x_row in date:
    rows.append([x_row,price[i]])
    i = i + 1
# name of csv file
filename = "data/Pricerecord_datewise.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)

response_monthwise= requests.get("https://api.eia.gov/series/?api_key=b808259a4fc11613193992a8b56196cb&series_id=NG.RNGWHHD.M")
print(response_monthwise.status_code)
pass_times_monthwise = response_monthwise.json()['series']
for d in pass_times_monthwise:
    data_monthwise = d['data']

for x_row in data_monthwise:
    datetimeobject = datetime.strptime(x_row[0], '%Y%m')
    newformat = datetimeobject.strftime('%d-%m-%Y')
    date_monthwise.append(newformat)
    price_monthwise.append(x_row[1])
i = 0
for x_row in date_monthwise:
    rows_monthwise.append([x_row, price_monthwise[i]])
    i = i + 1
# name of csv file
filename_monthwise = "data/Pricerecord_monthwise.csv"

# writing to csv file
with open(filename_monthwise, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows_monthwise)








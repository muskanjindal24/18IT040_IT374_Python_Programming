import csv

reader = csv.reader(open('employee_entries.csv', 'r'), delimiter=',')
writer = csv.writer(open('employee_details.csv', 'w'), delimiter=' ')
for row in reader:
    writer.writerow(row)


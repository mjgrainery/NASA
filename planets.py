## Script that imports data from 'exoplanets.csv' and then determines the average age of a star that the exoplanets rotate around. 

import csv

# File Name #
file = 'exoplanets.csv'
final_list = []

with open(file) as f:
    reader = csv.reader(f)
    new_list = []
    for row in reader:
        if '#' in row[0] or 'rowid' in row[0]:
            pass;
        else:#if 'Cet' in row[1]:
            if len(row[233]) > 1:
                #print(row[1] + " Year of Discovery: " + row[154] + " Stellar Age: " + row[233])
                new_list.append(row[0])
                new_list.append(row[3])
                new_list.append(" Year of Discovery: " + row[154])
                new_list.append(" Stellar age: " + row[233])

                final_list.append(new_list)
                new_list = []

sorted_list = sorted(final_list, key=lambda x: x[3])

avg_age_list = []

for stars in sorted_list:
    if float(stars[3][13:]) > 80:
        pass
    else:
        avg_age_list.append(float(stars[3][13:]))

avg_star_age = sum(avg_age_list)/len(avg_age_list)
print(avg_star_age)

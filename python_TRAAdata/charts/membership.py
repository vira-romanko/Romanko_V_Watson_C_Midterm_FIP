import csv
import numpy as np
import matplotlib.pyplot as plt

year = []
memberships = []


with open("C:/Users/acade/Documents/Watson_A_Romanko_Vira_TRAAdata_Python/data/memberships.csv") as csvfile:
    reader = csv.reader (csvfile, delimiter=",")

    line_count = 0
    for row in reader:
        if line_count is 0:
            line_count +=1
        else:
            year.append(row[0])
            memberships.append(row[1])

        line_count +=1


x = [len(year)]
y = [len(memberships)]


plt.plot(year, memberships, color='#5d7032')
plt.xlabel('Year')
plt.ylabel('Memberships')
plt.title('Membership growth in the TRAA over the years')
plt.show()





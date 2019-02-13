import csv
import numpy as np
import matplotlib.pyplot as plt

troutReleased = []
yearList = []

with open("C:/Users/acade/Documents/Watson_A_Romanko_Vira_TRAAdata_Python/data/eggs.csv") as csvfile:
    reader = csv.reader (csvfile, delimiter=",")
    line_count = 0
    for row in reader:
        if line_count is 0:
            line_count +=1
        else:
            troutReleased.append(row[3])
            yearList.append(row[1])

        line_count +=1

graphYearlist = []
graphTrout = []

for i in range(len(yearList)):
    if i%2 == 0:
        year = yearList[i]
        releasedTrout = int(troutReleased[i].replace(',','')) + int(troutReleased[i-1].replace(',',''))
        graphYearlist.append(year)
        graphTrout.append(releasedTrout)


y_pos = np.arange(len(graphTrout))

plt.title('Trout hatched and released by the TRAA')
plt.ylabel('Eggs hatched and released')
plt.xlabel('Year')
plt.bar(y_pos, graphTrout, color=('#9bbe4b'))
plt.xticks(y_pos, graphYearlist)
plt.show()

        














    
    

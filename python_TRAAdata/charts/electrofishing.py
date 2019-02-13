import csv
import numpy as np
import matplotlib.pyplot as plt

fishCaught = []
creekName = []


with open("C:/Users/acade/Documents/Watson_A_Romanko_Vira_TRAAdata_Python/data/electrofishing.csv") as csvfile:
    reader = csv.reader (csvfile, delimiter=",")

    line_count = 0
    for row in reader:
        if line_count is 0:
            line_count +=1
        else:
            creekName.append(row[0])
            fishCaught.append(row[2])



y_pos = np.arange(len(fishCaught))


plt.title('Fish caught in Thames River creeks in 2018')
plt.ylabel('Fish caught')
plt.xlabel('Creek')
plt.bar(y_pos, fishCaught, color=('#9bbe4b'))
plt.xticks(y_pos, creekName)
plt.show()



            







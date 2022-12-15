import csv
import os

path = "E:\AIProjectFrontEnd\music"
listdir = os.listdir(path)
for i in range(len(listdir)):
    listdir[i] = listdir[i][:-4]
# print(listdir)
with open('spotify.csv', 'r', encoding="utf8") as input_file:
    inputreader = csv.reader(input_file)
    alreadyadded = []
    with open('testset.csv', 'w', encoding="utf8") as output_file:
        outputwriter = csv.writer(output_file)
        # alreadywritten = []
        # for i in range(len(listdir)):
        #     for row in inputreader:
        #         if row[12] == listdir[i] and listdir[i] not in alreadywritten:
        #             alreadywritten.append(listdir[i])
        #             outputwriter.writerow(row)
        #             i = 0
        #             # print(i[:-4])
        #             break
        for row in inputreader:
            if row[12] in listdir and row[12] not in alreadyadded:
                alreadyadded.append(row[12])
                outputwriter.writerow(row)

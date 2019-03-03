import csv
import pprint


class KingPlayer:

    def __init__(self, name, pos, value):
        self.name = name
        self.value = value
        self.pos = pos

    def __str__(self):
        return self.name + ": " + self.pos + ", " + str(self.value)

    def __repr__(self):
        return self.name + ": " + self.pos + ", " + str(self.value)


path = 'C:\\Users\\jacks\\Downloads\\DKSalaries.csv'

CPT = []
UTIL = []

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    players = []
    salary = []
    pos = []
    ppg = []
    group = []
    group2 = []

    for row in csv_reader:
        players.append(row[2])
        salary.append(row[5])
        ppg.append(row[8])
        pos.append(row[4])
    salary.remove("Salary")
    players.remove("Name")
    ppg.remove("AvgPointsPerGame")

    index = salary.__len__()

    for num in range(1, index):
        conv = float(ppg[num])
        if conv != 0:
            try:
                value = round(float(salary[num]) / float(ppg[num]), 1)
                player = KingPlayer(players[num], pos[num], value)
                if pos[num] == 'CPT':
                    group.append(player)
                else:
                    group2.append(player)

            except ZeroDivisionError as e:
                print(salary[num] + " " + ppg[num])
    group.sort(key=lambda x: x.value, reverse=False)
    CPT = sorted(group, key=lambda x: x.value, reverse=False)

    group2.sort(key=lambda x: x.value, reverse=False)
    UTIL = sorted(group, key=lambda x: x.value, reverse=False)

with open("results.txt", 'w') as f:
    f.write("Best CPT Players: \n")
    for p in CPT:
        f.write(" " + p.__str__() + "\n")
    f.write("Best UTIL Players\n")
    for u in UTIL:
        f.write(" " + u.__str__() + "\n")
    f.close()
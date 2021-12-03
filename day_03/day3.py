report = [x.strip() for x in open('input')]
#report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

# Part 1
gamma = ''
epsilon = ''
reportLen = len(report[0])

for digit in range(reportLen):
    counter_0 = 0
    counter_1 = 0
    for each in report:
        if int(each[digit]) == 1:
            counter_1 += 1
        else:
            counter_0 += 1
    if counter_1 > counter_0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

power_consumption = int(gamma, 2) * int(epsilon, 2)
print(power_consumption)

# Part 2
o2List = report[:]
co2List = report[:]

for digit in range(reportLen):
    if len(co2List) > 1:
        counter_0 = 0
        counter_1 = 0
        tempList = []
        for each in o2List:
            if int(each[digit]) == 1:
                counter_1 += 1
            else:
                counter_0 += 1
        if counter_0 > counter_1:
            for i in o2List:
                if i[digit] == '0':
                    tempList.append(i)
        else:
            for i in o2List:
                if i[digit] == '1':
                    tempList.append(i)
        o2List = tempList[:]
    else:
        break

for digit in range(reportLen):
    if len(co2List) > 1:
        counter_0 = 0
        counter_1 = 0
        tempList = []
        for each in co2List:
            if int(each[digit]) == 1:
                counter_1 += 1
            else:
                counter_0 += 1
        if counter_1 < counter_0:
            for i in co2List:
                if i[digit] == '1':
                    tempList.append(i)
        else:
            for i in co2List:
                if i[digit] == '0':
                    tempList.append(i)
        co2List = tempList[:]
    else:
        break

life_support = int(o2List[0], 2) * int(co2List[0], 2)
print(life_support)

report = [x.strip() for x in open('input')]
#report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

# Part 1
counter_0 = 0
counter_1 = 0
gamma_rate = ''
epsilon_rate = ''

for digit in range(len(report[0])):
    for each in report:
        if int(each[digit]) == 1:
            counter_1 += 1
        if int(each[digit]) == 0:
            counter_0 += 1
    if counter_1 > counter_0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'
    counter_0 = 0
    counter_1 = 0

power_consumption = int(gamma_rate,2) * int(epsilon_rate,2)
print(power_consumption)

# Part 2

#life_support = O2_generator * CO2_scrubber

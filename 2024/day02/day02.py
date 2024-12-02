file = [x.strip() for x in open('2024/day02/input')]

def check_report(report):
    first_diff = report[1] - report[0]

    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        if diff * first_diff <= 0 or abs(diff) < 1 or abs(diff) > 3:
            return False 
    return True

def check_report_dampener(report):
    if check_report(report):
        return True

    for i in range(len(report)):
        test_report = report[:i] + report[i+1:]
        if check_report(test_report):
            return True
    return False

reports = [list(map(int, line.split())) for line in file]
part1 = sum(check_report(report) for report in reports)
part2 = sum(check_report_dampener(report) for report in reports)

print(part1, part2)
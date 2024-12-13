from collections import Counter

valid = lambda r: len(set([j > 0 for j in r])) == 1 and all([abs(j) in (1, 2, 3) for j in r])

reports = []

with open("input.txt") as f:
    for line in f:
        line = line.strip().split()
        reports.append(list(map(int, line)))

report_diffs = [
    [reports[i][j] - reports[i][j - 1] for j in range(1, len(reports[i]))]
    for i in range(len(reports))
]

report_dirs = [[j > 0 for j in i] for i in report_diffs]
report_dirs = [[j == max((d := Counter(i)), key=d.get) for j in i] for i in report_dirs]
report_mags = [[abs(j) for j in i] for i in report_diffs]

print(*reports, sep="\n")

tot = 0

"""
a    b    c    d    e
     b-a  c-b  d-c  e-d

p = 0 c-b d-c e-d
p = 1 c-a d-c e-d
p = 2 b-a d-b e-d
p = 3 b-a c-b e-c
p = 4 b-a c-b d-c
"""

for report, r in zip(report_diffs, reports):
    if valid(report):
        tot += 1
    else:
        if valid(report[1:]) or valid(report[:-1]):
            tot += 1
            continue

        for p in range(1, len(report)):
            if valid(report[:p - 1] + [report[p] + report[p - 1]] + report[p + 1:]):
                tot += 1
                print(r)
                break

print(tot)

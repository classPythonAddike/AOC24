reports = []

with open("input.txt") as f:
    for line in f:
        line = line.strip().split()
        reports.append(list(map(int, line)))

report_diffs = [
    [reports[i][j] - reports[i][j - 1] for j in range(1, len(reports[i]))]
    for i in range(len(reports))
]

report_valid = [len(set([j > 0 for j in i])) == 1 and all([abs(j) in (1, 2, 3) for j in i]) for i in report_diffs]
print(sum(report_valid))

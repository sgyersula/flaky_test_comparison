from collections import defaultdict
f = open('../dataset/candidates.txt', 'r')
projects = f.readline().split(',')
f.close()
projects = [project.strip() for project in projects]
mark = defaultdict(bool)
target = []

f = open('some_results/Flakify_per_project_results_on_IDoFT_dataset.csv','r')
head = None
for line in f:
    if not head:
        head = line
    comp = line.split()
    for project in projects:
        if project in comp[0] and not mark[project]:
            target.append(line)
            mark[project] = True
            break
f.close()

f = open('some_results/Flakify_per_project_results_on_selected.csv','w')
f.write(head)
for l in target:
    f.write(l)
f.close()

from collections import defaultdict
f = open('./selected_input.csv', 'r')
projects = []
for line in f:
    if line.split(',')[0] == 'Project URL':
        continue
    projects.append(line.split(',')[0].split('/')[-1])
f.close()

mark = defaultdict(bool)
target = []

f = open('./Flakify/some_results/Flakify_per_project_results_on_IDoFT_dataset.csv','r')
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

f = open('./Flakify/some_results/Flakify_per_project_results_on_selected.csv','w')
f.write(head)
for l in target:
    f.write(l)
f.close()

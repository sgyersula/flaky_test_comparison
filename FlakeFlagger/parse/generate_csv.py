import csv
f = open('FlakeFlagger/parse/selected.txt','r')
projects = []
for line in f:
    items = line.split()
    for item in items:
        projects.append(item)
f.close()

towrite = []
f = open('dataset/pr-data.csv','r')
fff = open('./selected_input.csv','w')
# writer = csv.writer(fff)
for line in f:
    if not towrite:
        towrite.append(line)
    tmp = line.split(',')
    name = tmp[0].split('/')[-1]
    if name in projects and name not in towrite[-1].split(',')[0].split('/')[-1]:
        towrite.append(line)

for line in towrite:
    fff.write(line)
f.close()
fff.close()
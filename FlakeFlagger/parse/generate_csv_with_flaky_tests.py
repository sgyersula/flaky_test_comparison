import csv
fff = open('./selected_input.csv','r')
projects = {}
for line in fff:
    items = line.split(',')
    projects[items[0]] = items[1]
fff.close()

towrite = []
f = open('dataset/pr-data.csv','r')
ff = open('./selected_input_with_flaky_tests.csv','w')
# writer = csv.writer(fff)
for line in f:
    if not towrite:
        towrite.append(line)
    tmp = line.split(',')
    url = tmp[0]
    sha = tmp[1]
    if url in projects and projects[url] == sha:
        towrite.append(line)

for line in towrite:
    ff.write(line)
f.close()
ff.close()
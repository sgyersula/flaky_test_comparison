lines = []
with open('./dataset/pr-data.csv') as f:
    for line in f:
        lines.append(line)
    
keys = lines[0]
sample_line = lines[-1].split(',')
print(sample_line)
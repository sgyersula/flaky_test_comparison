import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--csv_path', type=str, default='sample_input.csv')
args = parser.parse_args()

csv_path = args.csv_path
lines = []
with open(csv_path, 'r') as f:
    for row in f:
        lines.append(row)
keys = lines[0]
lines = lines[1:]

if not os.path.exists('projects'):
    os.mkdir('projects')
os.chdir('projects')

# Columns
# Project URL,SHA Detected,Module Path,Fully-Qualified Test Name (packageName.ClassName.methodName),Category,Status,PR Link,Notes
# Sha should be dealt within parse_data.py

for line in lines:
    project = line.split(',')
    project_url = project[0]
    project_name = project_url.split('/')[-1]
    sha = project[1]
    module = project[2]
    test_name = project[3] 
    os.system('git clone ' + project_url)
    

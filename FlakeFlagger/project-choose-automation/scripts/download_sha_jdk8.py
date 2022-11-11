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
my_verified_dict = {}
for i,line in enumerate(lines):
    project = line.split(',')
    project_url = project[0]
    
    project_name = project_url.split('/')[-1]
    sha = project[1]
    module = project[2]
    test_name = project[3] 
    if i > 0 and lines[i-1].split(',')[0] == project_url and lines[i-1].split(',')[1] == sha:
        continue
    if project_url in my_verified_dict:
        continue
    os.system('git clone ' + project_url)
    os.chdir(project_name)
    os.system('git checkout ' + sha)
    f = open("pom.xml")
    print("debug info: starting" + str(i) + project_url + sha)
    line = f.readline()
    flagValid = False
    while line:
        flag1 = False
        flag2 = False    
        if "<properties>" in line:
            flag1 = True
            while line:
                if "1.5" in line or "1.6" in line or "1.7" in line or "1.8" in line:
                    flagValid = True
                    print("debug info: mvn verify because of properties"+ str(i))
                    my_verified_dict[project_url] = sha
                    os.system('mvn verify')
                    break
                if "</properties>" in line:
                    break     
                line = f.readline()
        if not flagValid:
            if "<configuration>" in line:
                flag2 = True
                while line:
                    if "1.5" in line or "1.6" in line or "1.7" in line or "1.8" in line:
                        flagValid = True
                        print("debug info: mvn verify because of configuration"+ str(i))
                        my_verified_dict[project_url] = sha
                        os.system('mvn verify')
                        break
                    if "</configuration>" in line:
                        break     
                    line = f.readline()
        if flag1 and flag2:
            break
        if flagValid:
            break
        line = f.readline()
    f.close()
    os.chdir(os.path.abspath(".."))
    if not flagValid:
        os.system('rm -rf ' + project_name)
    print("debug info: ending" + str(i))
    print(my_verified_dict)
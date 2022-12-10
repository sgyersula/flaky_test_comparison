import time
import os
import os.path as osp
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--csv_file', type=str, default='new_projects.csv')
args = parser.parse_args()
csv_file = args.csv_file

projects_dir = '/misc/scratch/sherrys/code/iDF/dataset'
print(csv_file)

f   = open('./'+csv_file,'r')
os.chdir('iDFlakies')
for line in f:
    items = line.split(',')
    if items[0] == 'Project URL':
        continue
    name = items[0].split('/')[-1]
    # start testing
    
    # set up the pom.xml
    # bash pom-modify/modify-project.sh path_to_maven_project
    os.system('bash pom-modify/modify-project.sh ' + osp.join(projects_dir,name))
    
    # run iDFlakies
    os.chdir(osp.join(projects_dir, name))
    # mvn idflakies:detect -Ddetector.detector_type=random-class-method -Ddt.randomize.rounds=10 -Ddt.detector.original_order.all_must_pass=false
    os.system('mvn idflakies:detect -Ddetector.detector_type=random-class-method -Ddt.randomize.rounds=50 -Ddt.detector.original_order.all_must_pass=false')
    os.chdir('/misc/scratch/sherrys/code/iDF/iDFlakies')
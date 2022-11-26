import time
import os
import os.path as osp
log = open('./logging.out','w')
projects_dir = '/misc/scratch/sherrys/code/iDF/dataset/selected'

f   = open('./selected.csv','r')
os.chdir('iDFlakies')
for line in f:
    items = line.split(',')
    if items[0] == 'Project URL':
        continue
    name = items[0].split('/')[-1]
    # start testing
    log.write(name + ' start test at ' + str(time.time()) + '\n')
    
    # set up the pom.xml
    log.write(name + ' set up pom at ' + str(time.time()) + '\n')
    # bash pom-modify/modify-project.sh path_to_maven_project
    os.system('bash pom-modify/modify-project.sh ' + osp.join(projects_dir,name))
    
    # run iDFlakies
    log.write(name + ' start run  at ' + str(time.time()) + '\n')
    os.chdir(osp.join(projects_dir, name))
    # mvn idflakies:detect -Ddetector.detector_type=random-class-method -Ddt.randomize.rounds=10 -Ddt.detector.original_order.all_must_pass=false
    os.system('mvn idflakies:detect -Ddetector.detector_type=random-class-method -Ddt.randomize.rounds=10 -Ddt.detector.original_order.all_must_pass=false')
    os.chdir('/misc/scratch/sherrys/code/iDF/iDFlakies')
    log.write(name + ' finished at   ' + str(time.time()) + '\n')

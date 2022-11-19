import csv
import os
import os.path as osp
import argparse


# input parameters
parser = argparse.ArgumentParser()
parser.add_argument('--csv_path', type=str, default='FlakeFlagger/parse/sample_input.csv')
args = parser.parse_args()
csv_path = args.csv_path

# get input data
projects = []
with open(csv_path) as f:
    for line in f:
        projects.append(line)
input_keys = projects[0]
projects = projects[1:]

def get_method_text(module, road, file): 
    """ 
    project_path: path to the github download of the test project
    module: '.' for current directory or specified for a subdirectory
    road: com.sjioa.sherry etc 
    file: java file name 
    """
    project_path = osp.join(module, 'src/test/java', road, file+'.java')
    res = ''
    # /Users/yueshangguan/Desktop/files/22fall/courses/test/project/spring-boot-cloud/registry/src/test/java/cn/zhangxd/registry/ApplicationTests.java
    f = open(project_path,'r')
    methods = []
    lines = []
    for line in f:
        lines.append(line)
    
    accum = []
    count = 0
    flag = False
    for line in lines:
        if 'public' in line and '{' in line and 'class' not in line.split():
            flag = True
        if flag:
            accum.append(line)
            if '{' in line:
                count += 1
            if '}' in line:
                count -= 1
            if count == 0:
                flag = False
                tmpstr = ''.join(accum)
                accum = []
                if 'assert' in tmpstr or 'Assert' in tmpstr:
                    methods.append(tmpstr)
            
    return methods

os.chdir('FlakeFlagger/parse/projects')
# start transforming each project
for project in projects:
    res = []
    project = project.split(',')
    # get parameter from data
    project_name = project[0].split('/')[-1]
    sha = project[1]
    module = project[2]
    test_name = project[3]
    
    # switch directory
    os.chdir(project_name)
    os.system('git checkout ' + sha)
    
    # decode
    road = ('/').join(test_name.split('.')[:-2])
    file_name = test_name.split('.')[-2]
    target_method = test_name.split('.')[-1]
    
    
    contexts = get_method_text(module, road, file_name) # todo
    
    positive, negative = [],[]
    for context in contexts:
        print(context)
        if target_method in context:
            positive.append(context)
        else:
            negative.append(context)
    os.chdir('..')
    os.chdir('../class_file')
    if not os.path.exists(project_name):
        os.mkdir('./'+project_name)
    
    os.chdir(project_name)
    if not os.path.exists('positive'):
        os.mkdir('./positive')
    os.chdir('positive')
    for pos in positive:
        name = pos.split()[2].split('(')[0]
        f = open(name+'.java','w')
        f.write(pos)
        f.close()
    os.chdir('..') 
    if not os.path.exists('negative'):
        os.mkdir('./negative')
    os.chdir('negative')
    for neg in negative:
        name = neg.split()[2].split('(')[0]
        f = open(name+'.java','w')
        f.write(pos)
        f.close()
    os.chdir('..') 
    os.chdir('..')
    
    os.chdir('../projects')
    
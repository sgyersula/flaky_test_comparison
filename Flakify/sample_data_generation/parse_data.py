import csv
import os
import os.path as osp
import argparse


# input parameters
parser = argparse.ArgumentParser()
parser.add_argument('--csv_path', type=str, default='sample_input.csv')
args = parser.parse_args()
csv_path = args.csv_path

# get input data
projects = []
with open('./dataset/pr-data.csv') as f:
    for line in f:
        projects.append(line)
input_keys = projects[0]
projects = projects[1:]

# set up output file
output_file = open('sample_output.csv','w')
writer = csv.writer(output_file)
output_keys = 'test_case_name,project,version,package_name,class_name,method_name,flaky,smells_found,full_code,preprocessed_code'.split(',')
writer.writerow(output_keys)

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
    f = open(osp.join(project_path, road, file),'r')
    methods = []
    lines = []
    for line in f:
        lines.append(line)
    accum = []
    for i, line in enumerate(lines):
        if line != '\n':
            accum.append(line)
        else:
            methods.append(''.join(accum))
            accum = []
    for method in methods:
        if target_method in method:
            res = method
            break
    return res



# start transforming each project
for project in projects:
    res = []
    
    # get parameter from data
    project_name = project[0].split('/')[-1]
    sha = project[1]
    module = project[2]
    test_name = project[3]
    
    # switch directory
    os.chdir('projects')
    os.chdir(project_name)
    os.system('git checkout ' + sha)
    
    # decode
    road = ('/').join(test_name.split('.')[:-2])
    file_name = test_name.split('.')[-2]
    target_method = test_name.split('.')[-1]
    test_dir = osp.join()
    
    context = get_method_text(module, road, file_name) # todo
    res.append(project_name)
    res.append(sha)
    res.append('') # todo
    res.append(target_method)
    res.append(str(1))
    res.append(context)
    res.append('')
    res.append(context)
    res.append(0)
    res.append(0)
    res.append(context)
    os.chdir('..')
    os.chdir('..')
    
    writer.writerow(res)



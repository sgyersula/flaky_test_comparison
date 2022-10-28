from errno import ENOTCONN
import os.path as osp

lines = []
with open('./dataset/pr-data.csv') as f:
    for line in f:
        lines.append(line)
    
keys = lines[0]
sample_line = lines[-1].split(',')
module = sample_line[2]
project_path = '/Users/yueshangguan/Desktop/files/22fall/courses/test/project/spring-boot-cloud/' + module + '/src/test/java'
road = ('/').join(sample_line[3].split('.')[:-2])
file = sample_line[3].split('.')[-2]+'.java'
target_method = sample_line[3].split('.')[-1]


def get_method_text(project_path, module, road, file): 
    """ 
    project_path: path to the github download of the test project
    module: '.' for current directory or specified for a subdirectory
    road: com.sjioa.sherry etc 
    file: java file name 
    """
    project_path = osp.join(project_path, module, 'src/test/java', road, file+'.java')
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
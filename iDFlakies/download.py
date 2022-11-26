import os
import os.path as osp
dataset_dir = '/misc/scratch/sherrys/code/iDF/dataset/selected'

# download
f   = open('./selected.csv','r')
os.chdir('dataset/selected')
for line in f:
    items = line.split(',')
    if items[0] == 'Project URL':
        continue
    url = items[0]
    sha = items[1]
    name = url.split('/')[-1]
    os.system('git clone ' + url)
    
    
# checkout
f   = open('./selected.csv','r')
for line in f:
    items = line.split(',')
    if items[0] == 'Project URL':
        continue
    url = items[0]
    sha = items[1]
    name = url.split('/')[-1]
    os.chdir(osp.join(dataset_dir, name))
    os.system('git checkout ' + sha)
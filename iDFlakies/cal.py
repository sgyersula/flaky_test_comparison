import os
import os.path as osp

dataset_path = './dataset'
projects = os.listdir(dataset_path)
for p in projects:
    path = osp.join(dataset_path, p,'.dtfixingtools')
    if os.path.exists(path) and 'error' not in os.listdir(path):
        print(p)

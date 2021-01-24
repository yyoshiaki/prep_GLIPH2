import pandas as pd
import os
import json
import sys

# dir_arcasHLA = './test'
dir_arcasHLA = sys.argv[1]

suffix = '.genotype.json'

list_files = [x for x in os.listdir(dir_arcasHLA) if x.endswith(suffix)]
list_samples = [x.split(suffix)[0] for x in list_files]

list_lines = []
for s,f_arc in zip(list_samples, list_files):
    with open(dir_arcasHLA + '/' + f_arc, 'r') as f:
        d = json.load(f)

    l = []
    for k,v in d.items():
        if k.startswith('D'):
            for a in v:
                a = a.split(':')[0] + ':' + a.split(':')[1]
                l.append(a)
                
    list_lines.append("\t".join([s] + l))

with open(dir_arcasHLA + '/GLIPH2.input.HLA.tsv', 'w') as f:
    for c in list_lines:
        # print(c)
        f.writelines(c + '\n')
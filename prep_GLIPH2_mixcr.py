import pandas as pd
import os
import sys

# dir_mixcr = '../test'
dir_mixcr = sys.argv[1]
suffix = '.clonotypes.TRB.txt'

list_files = [x for x in os.listdir(dir_mixcr) if x.endswith(suffix)]
list_samples = [x.split(suffix)[0] for x in list_files]

list_df = []
for s,f in zip(list_samples, list_files):
    df = pd.read_csv(dir_mixcr + '/' + f, sep='\t')
    df['TRBV'] = df['allVHitsWithScore'].str.split(',').str.get(0).str.split('*').str.get(0)
    df['TRBJ'] = df['allJHitsWithScore'].str.split(',').str.get(0).str.split('*').str.get(0)
    df['CDR3a'] = 'NA'
    df['sub:cond'] = s + ':NA'

    list_df.append(df[['aaSeqCDR3', 'TRBV', 'TRBJ', 'CDR3a', 'sub:cond', 'cloneCount']])

df_merged = pd.concat(list_df)
df_merged = df_merged.groupby(
    by=['aaSeqCDR3', 'TRBV', 'TRBJ', 'CDR3a', 'sub:cond'], 
    as_index=False).sum().sort_values(by='sub:cond')

df_merged.to_csv(dir_mixcr + '/GLIPH2.input.TRB.tsv', sep='\t', index=None, header=None)
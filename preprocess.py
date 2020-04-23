import pandas as pd
import math
log_fpkm=pd.read_csv('./data/TCGA-LIHC.htseq_fpkm.tsv',sep='\t', index_col=0)
fpkm=log_fpkm.applymap(lambda x:math.pow(2,x)-1)
fpkm_tumor=pd.DataFrame()
fpkm_normal=pd.DataFrame()
for column in fpkm.columns:
    if column[-3:-2]=='0': # tumor
        fpkm_tumor[column]=fpkm[column]
    else: # normal
        fpkm_normal[column]=fpkm[column]
print(fpkm_tumor.shape,fpkm_normal.shape)
fpkm_tumor.to_csv('./data/TCGA-LIHC.htseq_fpkm_tumor.tsv',sep='\t')
fpkm_normal.to_csv('./data/TCGA-LIHC.htseq_fpkm_normal.tsv',sep='\t')
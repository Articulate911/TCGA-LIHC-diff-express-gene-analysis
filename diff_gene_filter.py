import pandas as pd
from scipy import stats
import numpy as np
fpkm_tumor=pd.read_csv('./data/TCGA-LIHC.htseq_fpkm_tumor.tsv',sep='\t')
fpkm_normal=pd.read_csv('./data/TCGA-LIHC.htseq_fpkm_normal.tsv',sep='\t')
stat=pd.DataFrame()
stat['tumor_avg']=fpkm_tumor.mean(axis=1)
stat['normal_avg']=fpkm_normal.mean(axis=1)
delete_index=[]

print(stat.shape)

for i in range(len(stat.index)):
    if stat['tumor_avg'].iloc[i]==0 and stat['normal_avg'].iloc[i]==0:
        delete_index.append(i)
fpkm_tumor.drop(labels=delete_index,axis=0,inplace=True)
fpkm_tumor.reset_index(drop=True,inplace=True)
fpkm_normal.drop(labels=delete_index,axis=0,inplace=True)
fpkm_normal.reset_index(drop=True,inplace=True)
stat.drop(labels=delete_index,axis=0,inplace=True)
stat.reset_index(drop=True,inplace=True)
stat['fold_change']=stat['tumor_avg']/stat['normal_avg']

delete_index=[]
for i in range(len(stat.index)):
    fc=stat['fold_change'].iloc[i]
    a=np.delete(fpkm_tumor.iloc[i].values,0)
    b=np.delete(fpkm_normal.iloc[i].values,0)
    t,pvalue=stats.ttest_ind(a,b,equal_var=False)
    if pvalue>0.05 or (fc>0.5 and fc <2):
        delete_index.append(i)
fpkm_tumor.drop(labels=delete_index,axis=0,inplace=True)
fpkm_tumor.reset_index(drop=True,inplace=True)
fpkm_normal.drop(labels=delete_index,axis=0,inplace=True)
fpkm_normal.reset_index(drop=True,inplace=True)
stat.drop(labels=delete_index,axis=0,inplace=True)
stat.reset_index(drop=True,inplace=True)
print(stat.shape)
fpkm_tumor.to_csv('./data/TCGA-LIHC.htseq_fpkm_tumor_filter.tsv',sep='\t',index=False)
fpkm_normal.to_csv('./data/TCGA-LIHC.htseq_fpkm_normal_filter.tsv',sep='\t',index=False)
stat.index=fpkm_tumor.index
stat.to_csv('./data/stats.tsv',sep='\t',index=False)
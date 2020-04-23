from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import numpy as np
fpkm_tumor=pd.read_csv('./data/TCGA-LIHC.htseq_fpkm_tumor.tsv',sep='\t',index_col=0)
fpkm_normal=pd.read_csv('./data/TCGA-LIHC.htseq_fpkm_normal.tsv',sep='\t',index_col=0)
tumor_maxtrix=np.array(fpkm_tumor.values)
normal_matrix=np.array(fpkm_normal.values)
pca=PCA(n_components=2)
reduced_tumor=pca.fit_transform(tumor_maxtrix)
reduced_normal=pca.fit_transform(normal_matrix)
# plt.scatter(reduced_tumor[:,0],reduced_tumor[:,1],c='r',marker='X')
# plt.scatter(reduced_normal[:,0],reduced_normal[:,1],c='g',marker='.')
# plt.show()
# silhouettescore=[]
# for i in range(2,11):
#     print('i=',i)
#     clf=KMeans(n_clusters=i).fit(reduced_tumor)
#     score=silhouette_score(reduced_tumor,clf.labels_)
#     silhouettescore.append(score)
# plt.figure(figsize=(10,6))
# plt.plot(range(2,11),silhouettescore,linewidth=1.5,linestyle='-')
# plt.show()

# silhouettescore=[]
# for i in range(2,11):
#     print('i=',i)
#     clf=KMeans(n_clusters=i).fit(reduced_normal)
#     score=silhouette_score(reduced_normal,clf.labels_)
#     silhouettescore.append(score)
# plt.figure(figsize=(10,6))
# plt.plot(range(2,11),silhouettescore,linewidth=1.5,linestyle='-')
# plt.show()

clf=KMeans(n_clusters=2).fit(reduced_tumor)
centers = clf.cluster_centers_
plt.scatter(reduced_tumor[:,0],reduced_tumor[:,1],c='r',marker='X',label='tumor')
plt.scatter(centers[:,0],centers[:,1],c='b',marker='.',label='centers')
plt.show()

clf=KMeans(n_clusters=2).fit(reduced_normal)
centers = clf.cluster_centers_
plt.scatter(reduced_normal[:,0],reduced_normal[:,1],c='g',marker='X',label='normal')
plt.scatter(centers[:,0],centers[:,1],c='r',marker='.',label='centers')
plt.show()

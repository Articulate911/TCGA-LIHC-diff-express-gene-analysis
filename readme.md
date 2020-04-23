# TCGA-LIHC-diff-express-gene-analysis
## Author
Tian-yuan-hao-jie
## Introduction
Differentially expressed genes analysis based on TCGA-LIHC(liver cancer) data. Project on bioinformatics course.
## Usage of files/folders
preprocess.py: retrieve the original FPKM matrix and separate it to tumor matrix and normal matrix


diff_gene_filter.py: filter genes according to pvalue and fold change

cluster.py: do cluster analysis using k-means method

data: contain original data downloaded from TCGA-LIHC(GDC) and output images during intermediate process, all of them are in *.tsv form

images: output images during cluster anaylsis
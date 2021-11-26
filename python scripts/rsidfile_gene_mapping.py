import pandas as pd
import os
os.chdir(r'C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\hg_files')
df = pd.read_csv('rsid_gene_conversion_file.csv',sep=',')

snp_gene_name_dict ={}

for index,row in df.iterrows():
     snp_gene_name_dict[row['rsid']]= (row['gene_name'],row['gene_id'],row['url'])

data_files =[file for file in os.listdir() if file.startswith("A2") or file.startswith("B1") or file.startswith("C2")]

os.mkdir("rsid_gene_converted_folder")
def extracting_gene_name_id_url(file_name):
    name,ext = os.path.splitext(file_name)
    snp_df = pd.read_csv(file_name)
    snp_df["gene_name"]=snp_df['rsid'].apply(lambda x:snp_gene_name_dict.get(x)[0])
    snp_df["gene_id"]=snp_df['rsid'].apply(lambda x:snp_gene_name_dict.get(x)[1])
    snp_df["url"]=snp_df['rsid'].apply(lambda x:snp_gene_name_dict.get(x)[2])
    snp_df.to_csv(r"rsid_gene_converted_folder/{}.csv".format(name), index=False)

#extracting_gene_name_id_url(data_files[0])

for f_name in data_files:
    extracting_gene_name_id_url(f_name)
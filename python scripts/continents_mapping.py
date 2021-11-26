import pandas as pd
import os
import numpy as np
from tqdm import tqdm
os.chdir(r'C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\hg_files')
os.mkdir("rsid_gene_country_continent_codes")

B=pd.read_csv('rsid_gene_country_codes\studies_id_continent_mapping.csv')
study_continent_dict = {}
for index,row in B.iterrows():
    study_continent_dict[row["study_id"]] = row["continent_code"]
#print(study_continent_dict)

files = [file for file in os.listdir() if file.startswith("A")
         or file.startswith("B") or file.startswith("C")]

def mapping_continent_codes(filename=None):
    name,ext = os.path.splitext(filename)
    df = pd.read_csv("rsid_gene_country_codes/{}".format(filename))
    country_list=np.array(list(map(int,df['country_codes'][0].split(','))))
    df['continent_codes'] =  (np.array((set([study_continent_dict[country] for country in country_list]))))
    df['country_codes'] = np.array(set(country_list))
    df.to_csv("rsid_gene_country_continent_codes/{}.csv".format(name))

for file in files:
    mapping_continent_codes(filename=file)
    #break

# retreive gene name, gene id, URL from SNP database

import pandas as pd
import os
from tqdm import tqdm
pd.options.mode.chained_assignment = None  # default='warn'
import re
import requests

api_rootURL = 'https://api.ncbi.nlm.nih.gov/variation/v0/'

os.chdir(r'C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\hg_files')
data_files =[
    file for file in os.listdir() if file.startswith("A2") or file.startswith("B1") or file.startswith("C2")
]
snp_master_list = set()
for file in data_files:
    #print(file)
    df = pd.read_csv(file)
    for val in df['rsid']:
        snp_master_list.add(val)  #.values

snp_master_list=list(sorted(snp_master_list))
print(snp_master_list)
print(len(snp_master_list))

def get_gene_id(rs):
    if type(rs)== str:   #  only str goes , thus NA is not gone in
        rs = re.sub('rs', '', rs.rstrip())
        if rs.isdigit():
            url = api_rootURL + 'beta/refsnp/' + rs
            #print(url)
            req = requests.get(url).json()
            if "primary_snapshot_data" in req.keys():
                assembly_annotation = req['primary_snapshot_data']['allele_annotations'][0]['assembly_annotation'][0]['genes']
                if assembly_annotation == []:
                     gene_name = None
                     gene_id = None
                else:
                    gene_name= assembly_annotation[0]['locus']
                    gene_id = assembly_annotation[0]['id']
                return url,gene_name,gene_id
            else:   # if it was merged with some rsid
                return url,None,None


snp_gene_name_dict ={}
# for rs in (snp_master_list)[:5]:
#     print(rs,get_gene_id(rs))

rsid_log_file  = open("rsid_log_file.txt","w")
output_file = open("rsid_gene_conversion_file.csv","w")
output_file.write("{},{},{},{},{}\n".format("id","rsid","gene_name","gene_id","url"))
for index,id in tqdm(enumerate(snp_master_list)):
    #print(index,id)
    rsid_log_file.write("{}.The current rsid searching is {}.\n".format(index,id))
    url, gene_name,gene_id= get_gene_id(id)
    snp_gene_name_dict[id]=(gene_name,gene_id,url)
    #print(snp_gene_name_dict)
    output_file.write("{},{},{},{},{}\n".format(index,id,gene_name,gene_id,url))


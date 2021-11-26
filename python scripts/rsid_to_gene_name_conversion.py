import time
import sys
from tqdm import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None  # default='warn'
import requests
import json
import argparse
import re

api_rootURL = 'https://api.ncbi.nlm.nih.gov/variation/v0/'

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
                     gene_name = "NA"
                     gene_id = "NA"
                else:
                    gene_name= assembly_annotation[0]['locus']
                    gene_id = assembly_annotation[0]['id']
                return url,gene_name,gene_id
            else:   # if it was merged with some rsid
                return url, "NA","NA"

df = pd.read_csv(r'C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\COVID19_HGI_A2_ALL_20210107.10k.txt',
                sep='\t')
rsid = df['rsid'].dropna().values
print(len(rsid))
#print(rsid[7980])
rsid_log_file  = open("rsid_log_file_7251.txt","w")
output_file = open("rsid_gene_conversion_file_7251.csv","w")
output_file.write("{},{},{},{},{}\n".format("id","rsid","gene_name","gene_id","url"))
for index,id in tqdm(enumerate(rsid[7251:],7251)):
    #print(index,id)
    rsid_log_file.write("{}.The current rsid searching is {}.\n".format(index,id))
    url, gene_name,gene_id= get_gene_id(id)
    output_file.write("{},{},{},{},{}\n".format(index,id,gene_name,gene_id,url))
    time.sleep(0.1)


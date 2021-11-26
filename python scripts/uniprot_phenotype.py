import pandas as pd
import mygene
import requests, sys
from tqdm import tqdm
import os
os.chdir(r'C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\hg_files')


api_rootURL = "https://rest.ensembl.org"
mg = mygene.MyGeneInfo()

# reading the rsid_gene_conversion file
df = pd.read_csv("rsid_gene_conversion_file.csv")
gene_id_list = set(df['gene_id'].dropna().values)
gene_id_list = list(sorted(gene_id_list))
gene_id_list = [i for i in gene_id_list if i!="None"]

#getting different identifiers with gene id example "9731"

def getting_different_identifiers(gene_id):
    identifiers = mg.getgene(int(gene_id), fields='symbol,name,uniprot')
    if identifiers != None: # identifier is a dict
        #print( (identifiers)) #['Swiss-Prot']
        #print((identifiers.keys()))
        uniprot_id = identifiers.get('uniprot' ,None)
        if uniprot_id != None:
            uniprot_id = uniprot_id.get('Swiss-Prot',None)
        gene_symbol = identifiers['symbol']
        #print(uniprot_id,gene_symbol)
        return gene_id, gene_symbol,uniprot_id
    else: # identifier is not a dict
        return gene_id,"",""

## getting phenotype data from ensembl
def getting_phenotype(gene_symbol):
    ext = "/phenotype/gene/homo_sapiens/{}".format(gene_symbol)
    URL = api_rootURL + ext
    result = requests.get(URL, headers={"Content-Type": "application/json"}).json()
    if type(result) == dict and result['error']: #{'error': 'Gene LOC105378904 not found.'}
        return "",URL
    else:
        phenotypes_list = []
        for element in result:
            phenotypes_list.append(element.get('description',None).lower().replace(",",""))
        # ",".join(sorted(phenotypes_list))
        return ";".join(sorted(phenotypes_list)), URL

# gene_id, gene_symbol, uniprot_id = getting_different_identifiers(105374013) #105378904   105374013
# phenotypes_list, URL = getting_phenotype(gene_symbol)
# print(gene_id, gene_symbol, uniprot_id)
# print(phenotypes_list, URL)

output_file = open("gene_id_uniprot_phenotypes.csv","w")
output_file.write("{},{},{},{},{},{}\n".format("index","gene_id","gene_symbol","uniprot_id","phenotypes_list","URL"))
uniprot_phenotype_log_file  = open("uniprot_phenotype_log_file.txt","w")

for index,gene in tqdm(enumerate(gene_id_list)):
    uniprot_phenotype_log_file.write("{}.The current rsid searching is {}.\n".format(index,gene))
    gene_id, gene_symbol, uniprot_id = getting_different_identifiers(gene)
    phenotypes_list, URL = getting_phenotype(gene_symbol)
    # print(gene_id, gene_symbol, uniprot_id)
    # print(phenotypes_list, URL)
    output_file.write("{},{},{},{},{},{}\n".format(index,int(gene_id),gene_symbol,uniprot_id,phenotypes_list,URL))

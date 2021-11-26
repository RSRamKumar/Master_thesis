# extracting drug gene interaction from the https://dgidb.org/api
# takes a gene name and lists drug names,chembl id

import requests
import json
import pandas as pd
import numpy as np
import time


# extracting drugs for a particular gene
def extracting_gene_drug_interactions(gene_name):
     response = requests.get("https://dgidb.org/api/v2/interactions.json?genes={}".format(gene_name)).json()
     try:
         gene_name =  response['matchedTerms'][0]['geneName']
         interactions_list = response['matchedTerms'][0]['interactions']
         number_of_interactions =  len(interactions_list)

         drug_list = []
         chembl_list = []
         for i in range(number_of_interactions):
             drug_list.append(interactions_list[i]['drugName'])
             chembl_list.append(interactions_list[i]['drugConceptId'])
     except:
            drug_list = np.nan
            chembl_list = np.nan

     return drug_list, chembl_list

     # drug_df = pd.DataFrame({
     #    "drugs": drug_list,
     #    "chembl_id":chembl_list })
     # return drug_df.head()

## function call - and reading gene list from file
hgi_df = pd.read_csv(r"C:\Users\rsurulinathan\Downloads\selectfromhgi.csv")
hgi_gene_list = list(set(hgi_df['gene_name'].dropna()))
out = open('gene_drug_interaction.csv',"w")
error_log = open("gene_drug_error.txt", "w")

for gene in set(hgi_gene_list):
    error_log.write("{} is being processed\n".format(gene ))
    drug_list, chembl_list = extracting_gene_drug_interactions(gene)
    out.write("{};{};{}\n".format(gene, drug_list,chembl_list ))
    time.sleep(1)


# writing json response to a json file
# with open('sample.json', 'w') as outfile:
#     json.dump(r, outfile,indent=5)


# Reading the gene_drug_interaction.csv and cleaning it
"""
MIS18A;[];[]
PAN3;[];[]
MYO10;[];[]
LOC105378642;nan;nan
"""
gene_drug_df = pd.read_csv("gene_drug_interaction.csv", sep=";", header=None)
gene_drug_df.columns = ['gene_name', 'drug_list','chemblid_list']

gene_drug_df.replace("[]", np.nan, inplace=True)

gene_drug_df["chemblid_list"] = gene_drug_df["chemblid_list"].apply(lambda x: eval(x) if type(x)==str else x)
gene_drug_df["drug_list"] = gene_drug_df["drug_list"].apply(lambda x: eval(x) if type(x)==str else x)


# print(type(gene_drug_df['chemblid_list'][0]),  (gene_drug_df['chemblid_list'][0]),  ((gene_drug_df['chemblid_list'][0])))
# print(type(gene_drug_df['chemblid_list'][1]),  (gene_drug_df['chemblid_list'][1]), len((gene_drug_df['chemblid_list'][1])))
# print(type(gene_drug_df['chemblid_list'][2]),  (gene_drug_df['chemblid_list'][2]),  ((gene_drug_df['chemblid_list'][2])))

# indexes to be remoed which follows the above stated condition
index_to_remove = []
for index, row in gene_drug_df.iterrows():
    if type(row['drug_list']) == float :
        index_to_remove.append(index)
print(len(index_to_remove))
print(gene_drug_df.shape)
gene_drug_df.drop(gene_drug_df.index[index_to_remove], inplace=True)

gene_drug_df['drug_count'] = gene_drug_df['drug_list'].apply(lambda x: len(x))
gene_drug_df.sort_values(by=['drug_count'], inplace=True, ascending=False)
#print(gene_drug_df['gene_name'].tolist())
gene_drug_df.to_csv("gene_drug_interaction_cleaned.csv",sep=";", index=False)
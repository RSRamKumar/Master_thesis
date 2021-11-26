# conversion of chembl to drugbank identifiers
# ref: https://www.ebi.ac.uk/unichem/info/webservices

import pandas as pd
import requests
import numpy as np

drug_df = pd.read_csv("gene_drug_interaction_cleaned.csv",sep=";")
#conversion of "['a','n']" to ['a','n'] i.e. string to list
drug_df['chemblid_list'] = drug_df['chemblid_list'].apply(lambda x:eval(x))

 # drugbank name obtaining using API
def converting_chembl_to_drugbank(chembl_list):
    drugbank_list = []
    for chembl in chembl_list:
            id = chembl[chembl.index(":")+1:]
            response = requests.get("https://www.ebi.ac.uk/unichem/rest/src_compound_id/{}/1/2".format(id)).json()
            try:
                #print(",".join(response[0].values()))
                drugbank_list.append(",".join(response[0].values()))
            except:
                drugbank_list.append(np.nan)
                #print(response)
    return drugbank_list

# a=converting_chembl_to_drugbank(['chembl:CHEMBL1762621', 'chembl:CHEMBL1093059', 'chembl:CHEMBL2107333'])
# b=converting_chembl_to_drugbank(['chembl:CHEMBL25', 'chembl:CHEMBL266158', 'chembl:CHEMBL11662'])
# c=converting_chembl_to_drugbank(['chembl:CHEMBL57'])


drug_df['drugbank_list']=drug_df['chemblid_list'].apply(lambda x:converting_chembl_to_drugbank(x))

drug_df.to_csv("gene_drug_interaction_cleaned_drugbank_added.csv",sep=";",index=False)

import requests
import pandas as pd


URL="https://www.covid19dataportal.org/api/backend/biochemistry/drug-targets?page=3&size=1000&fields=disease_name,gene,target_id,disease_id,association_score_overall"

response = requests.get(URL, headers={"Content-Type": "application/json"}).json()
print( (response['entries'][0]))

association_dict = {}

for i in range(len(response['entries'])):
    field_dict = response['entries'][i]['fields']
    #print(field_dict ) "".join(field_dict['target_id']),
    gene_name = "".join(field_dict['gene'])
    association_dict[gene_name] = float("".join(field_dict['association_score_overall']))

print(association_dict)
columns=['gene_name','target_id','association_score_overall']
X=pd.DataFrame( association_dict.items(), columns=['gene_name','association_score_overall'] )
print(X.head())

X.to_csv("score_page_3.csv", index=False)
# df = pd.read_csv(r'C:\Users\rsurulinathan\Downloads\continent_added_cts.tsv',sep='\t')
# print(df.loc[24:26])
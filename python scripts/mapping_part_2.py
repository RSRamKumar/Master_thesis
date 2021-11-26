import pandas as pd
import os
os.chdir(r'C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\hg_files')

study_mapping = pd.read_csv("studies_id_mapping.csv")
study_mapping_dict = {}
for index,row in study_mapping.iterrows():
    study_mapping_dict[row['study_name']]= (row['study_id'],row['country'])
#print(study_mapping_dict)
os.mkdir("rsid_gene_country_codes")
def mapping_country_codes_to_rsid_files(file):
    df = pd.read_csv("rsid_gene_converted_folder/{}".format(file))
    x = df['studies'][0].replace("'", '').replace(']', "").replace("[", "").split(",")
    studies_list_country_striped = [i.strip().rsplit("_", 1)[0] for i in x]
    #print(studies_list_country_striped)
    df['country_codes'] = ",".join(set(str(study_mapping_dict[i][0]) for i in studies_list_country_striped))
    # B['country_names']=",".join([enumerated_studies_countries_dict[i][1] for i in studies_list_country_striped])
    df.drop('studies', axis=1, inplace=True)
    #print(df.head())
    df.to_csv(r"rsid_gene_country_codes/{}".format(file), index=False)

for file in os.listdir("rsid_gene_converted_folder"):
    mapping_country_codes_to_rsid_files(file)
    print(file)
#mapping_country_codes_to_rsid_files("B1_ALL_eur_leave_ukbb.csv")
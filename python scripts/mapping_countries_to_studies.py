import pandas as pd
import os
os.chdir(r'C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\hg_files')
studies_countries_dict = {
    "Amsterdam_UMC_COVID_study_group": "Netherlands",
    "Ancestry":"United States",
    "BRACOVID":"Brazil",
    "BelCovid":"Belgium",
    "BQC19":"Canada",
    "DECODE":"Iceland",
    "Corea":"South Korea",
    "EstBB":"Estonia",
    "FinnGen":"Finland",
    "GENCOVID":"Italy",
    "genomicc":"Canada",
    "GNH":"United Kingdom",
    "GS":"United Kingdom",
    "HOSTAGE":"Germany",
    "Helix":"United States",
    "INTERVAL":"United Kingdom",
    "MGI": "United States",
    "MVP":"United States",
    "NTR":"Netherlands",
    "PHBB": "United States",
    "PMBB": "United States",
    "QGP":"Qatar",
    "SPGRX":"Spain",
    "Stanford":"United States",
    "SweCovid":"Sweden",
    "UKBB":"United Kingdom",
    "BoSCO":"Germany",
    "23ANDME":"United States",
    "Italy_HOSTAGE":"Italy",
    "Spain_HOSTAGE":"Spain",
    "genomicsengland100kgp":"United Kingdom",
    "Lifelines":"Netherlands",
    "GeneRISK":"Finland",
    "RS":"Netherlands",
    "CU":"Columbia",
    "GHS_Freeze_145":"United States",
    "JapanTaskForce":"Japan",
    "idipaz24genetics":"Spain",
    "FHoGID":"Switzerland",
    "UCLA":"United States",
    "Genetics_COVID19_Korea":"South Korea",
    "LGDB":"Latvia",
    "ACCOuNT":"United States",
    "BioVU":"United States",
    "CCPM":"United States",
    "GCAT":"Spain",
    "GFG":"United States",
    "Genotek":"Russia",
    "MSHS_CGI":"United States",
    "TOPMed_CHRIS10K":"Italy"
}
sorted_studies_countries_dict=dict(sorted(studies_countries_dict.items(),key=lambda x: x[1]))
enumerated_studies_countries_dict = {j[0]:(str(i),j[1]) for i,j in enumerate(sorted_studies_countries_dict.items(),1)}
print(enumerated_studies_countries_dict)

# df = pd.DataFrame.from_dict(enumerated_studies_countries_dict,orient='index')
# df = df.reset_index()
# df.columns = ['study_name', "study_id","country"]
# df.to_csv("studies_id_mapping.csv",index=False)


# A = pd.read_csv(r"C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\hg_files\rsid_gene_converted_folder\A2_ALL_eur.csv")
# #print(A.head())
# studies_ = A["studies"][0]
# studies_list = studies_.split(",")#.strip()
# print(studies_list)
# studies_list_country_striped = [i.strip().rsplit("_",1)[0] for i in studies_list]
# print(studies_list_country_striped)
#
# country_codes=",".join([enumerated_studies_countries_dict[i][0] for i in studies_list_country_striped])
# print(country_codes)
# country_names=",".join([enumerated_studies_countries_dict[i][1] for i in studies_list_country_striped])
# print(country_names)

B = pd.read_csv(r"C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\hg_files\rsid_gene_converted_folder\A2_ALL_eur.csv")
print(B['studies'].head())
x = B['studies'][0].replace("'",'').replace(']',"").replace("[","").split(",")
studies_list_country_striped = [i.strip().rsplit("_",1)[0] for i in x]
print(studies_list_country_striped)
B['country_codes']=",".join([enumerated_studies_countries_dict[i][0] for i in studies_list_country_striped])
#B['country_names']=",".join([enumerated_studies_countries_dict[i][1] for i in studies_list_country_striped])
B.drop('studies', axis=1, inplace=True)

B.to_csv("y.csv",index=False)

#!/usr/bin/env python3

# Import relevant libraries for HTTP request and JSON formatting
import requests
import json
import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time

def scraping_drug_names_from_DrugBank_website(drugbank_list):
    names_scrapped = []
    chembl_scrapped = []

    if type(drugbank_list) == list:
        for drug in drugbank_list:
            response = requests.get("https://go.drugbank.com/drugs/{}".format(drug)).content
            soup = BeautifulSoup(response, "html.parser")
            #drug_name = soup.title.text.split(":")[0]
            drug_name = soup.find("dd", class_="col-xl-4 col-md-9 col-sm-8 pr-xl-2").text
            names_scrapped.append(drug_name)
            chembl_finds = []
            chembl_soup = soup.find_all("dd", class_="col-md-8 col-sm-7")

            for i in chembl_soup:

                id = re.findall(r"CHEMBL\w+", i.text)
                if len(id) >= 1:
                    chembl_finds.append(id)

            flat_list = flat_list = [item for sublist in chembl_finds for item in sublist]

            if len(flat_list) ==0:
                chembl_scrapped.append(np.nan)
            elif len(flat_list) !=0:
                chembl_scrapped.append((",".join(flat_list)))
    else:
        names_scrapped.append(np.nan)
        chembl_scrapped.append(np.nan)
    time.sleep(1)
    return names_scrapped,chembl_scrapped


# print(scraping_drug_names_from_DrugBank_website(['DB00207', 'DB14972', 'DB00199']))
# print(scraping_drug_names_from_DrugBank_website(['DB12182', 'DB01370', 'DB14865']))
# # print(scraping_drug_names_from_DrugBank_website([]))

##function call
ct_df = pd.read_csv(r"C:\Users\rsurulinathan\Downloads\selecttrial_idd.csv",error_bad_lines=False)
ct_df['drugs'] = ct_df['drugs'].str[1:-1].str.split(',').tolist()
ct_df['drugs'] = ct_df['drugs'].apply(lambda x: [i.strip() for i in x] if type(x)== list else x)

ct_df['regions']=ct_df['regions'].str[1:-1].str.split(',').tolist()
ct_df['regions'] = ct_df['regions'].apply(lambda x: [i.strip().lower() for i in x] if type(x)== list else x)

ct_df['english_names'] = ct_df['drugs'].apply(lambda x:scraping_drug_names_from_DrugBank_website(x)[0])
ct_df['chembl_names'] = ct_df['drugs'].apply(lambda x:scraping_drug_names_from_DrugBank_website(x)[1])

print(ct_df.head())
ct_df.to_csv("clinical_trials_bruce.csv",index=False)

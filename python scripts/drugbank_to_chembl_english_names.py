
#!/usr/bin/env python3

# Import relevant libraries for HTTP request and JSON formatting
import requests
import json
import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import time

def scraping_drug_names_from_DrugBank_website(drugbank_id):
    names_scrapped = []
    chembl_scrapped = []
    response = requests.get("https://go.drugbank.com/drugs/{}".format(drugbank_id)).content
    soup = BeautifulSoup(response, "html.parser")
    # drug_name = soup.title.text.split(":")[0]
    drug_name = soup.find("dd", class_="col-xl-4 col-md-9 col-sm-8 pr-xl-2").text
    names_scrapped.append(drug_name)
    chembl_finds = []
    chembl_soup = soup.find_all("dd", class_="col-md-8 col-sm-7")

    for i in chembl_soup:
        id = re.findall(r"CHEMBL\w+", i.text)
        if len(id) >= 1:
            chembl_finds.append(id)

    flat_list = flat_list = [item for sublist in chembl_finds for item in sublist]

    if len(flat_list) == 0:
        chembl_scrapped.append(np.nan)
    elif len(flat_list) != 0:
        chembl_scrapped.append((",".join(flat_list)))

    return names_scrapped,chembl_scrapped

# print(scraping_drug_names_from_DrugBank_website("DB00207"))
# print(scraping_drug_names_from_DrugBank_website("DB14972"))
# print(scraping_drug_names_from_DrugBank_website("DB01370"))
# print(scraping_drug_names_from_DrugBank_website("DB12182"))

##function call
ct_df = pd.read_csv(r"C:\Users\rsurulinathan\Downloads\selecttrial_idd.csv",error_bad_lines=False)
ct_df['drugs'] = ct_df['drugs'].str[1:-1].str.split(',').tolist()
ct_df['drugs'] = ct_df['drugs'].apply(lambda x: [i.strip() for i in x] if type(x)== list else x)

drug_list = set()
for index, entries in enumerate(ct_df['drugs'].values):
    if type(entries) == list:
        for drug in entries:
            drug_list.add(drug)


print(len( (list(sorted(drug_list)))))


f=open("drugbank_chembl_english.csv",'w',encoding="utf-8")
f1=open("drug_error.txt","w")
for drug in list(sorted(drug_list)):
    f1.write("The drug for the scrappig process is {}\n".format(drug))
    english, chembl = scraping_drug_names_from_DrugBank_website(drug)
    f.write("{},{},{}\n".format(drug,english,chembl))


#https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
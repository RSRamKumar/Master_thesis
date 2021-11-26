import requests
from tqdm import tqdm
import csv
import pandas as pd

api_rootURL = "https://api.ncbi.nlm.nih.gov/variation/v0/"


# dict of biosampleid and ethnicities

dict_biosample_id_ethnicities = {
    'SAMN10492705':'Total',
    'SAMN10492695':'European',
    'SAMN10492703':'African',
    'SAMN10492696':'African Others',
    'SAMN10492698':'African American',
    'SAMN10492704':'Asian',
    'SAMN10492697':' East Asian',
    'SAMN10492701':'Other Asian',
    'SAMN10492699':'Latin American 1',
    'SAMN10492700':'Latin American 2',
    'SAMN10492702':'South Asian',
    'SAMN11605645':'Other'
}



def calculating_allele_frequency(allele_counts_dict):
    allele_freq_dict = {}
    sample_size_list = []
    for key,value in allele_counts_dict.items():
        sample_size  = sum(value.values() )
        sample_size_list.append(sample_size)
        allele_freq_dict[dict_biosample_id_ethnicities[key]]={i:(round(j/sample_size,4))
                for i,j in value.items()}
    return allele_freq_dict,sample_size_list

def parsing_allele_files(rsid=None):
    id = rsid.strip("rs")
    ext = "/refsnp/{}/frequency".format(int(id))
    URL = api_rootURL + ext
    response = requests.get(URL, headers={"Content-Type": "application/json"}).json()
    if 'results' in response.keys() :
        id_with_at = ",".join(response['results'].keys())
        reference_allele = response['results'][id_with_at]['ref']
        allele_counts_dict = response['results'][id_with_at]['counts']['PRJNA507278']['allele_counts']
        #print(calculating_allele_frequency(allele_counts_dict))
        return  calculating_allele_frequency(allele_counts_dict)
        #print("yes1")
    else:
        print("NA")

D,P=parsing_allele_files(rsid="674")
print(type(D))
print(P)

X=(pd.DataFrame.from_dict(D,orient='index'))
X['sample_size'] = P
X=X.reset_index()
#X.columns[0] = "Ethnicity"
print(X.columns)
print(X)
X.to_json("rs674.json",orient="records",indent=5)

# parsing_allele_files(rsid="rs1234")
# parsing_allele_files(rsid="rs14")


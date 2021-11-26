import pandas as pd
import os
from tqdm import tqdm
os.chdir(r'C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\hg_files')
os.mkdir("allele_frequencies_folder")

df = pd.read_csv("rsid_gene_conversion_file.csv")

rsid_list = df['rsid'].values
allele_log_file = open("allele_frequencies_folder/allele_log_file.txt","w")
error_log_file = open("allele_frequencies_folder/error_log_file.txt","w")

for index,rsid in tqdm(enumerate(rsid_list)):
    allele_log_file.write("{}.The current rsid is {}\n".format(index,rsid))
    try:
        allele_df = pd.read_table("https://www.ncbi.nlm.nih.gov/snp/{}/download/frequency".format(rsid),
                                  skiprows = 12)
        allele_df.to_json("allele_frequencies_folder/{}.json".format(rsid),
                      orient='records',indent=5)
    except:
        allele_log_file.write("{}.It got failed unfortunately {}\n".format(index,rsid))
        error_log_file.write("{}.It got failed unfortunately {}\n".format(index, rsid))


import pandas as pd
import os
from upsetplot import from_memberships
os.chdir(r'C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\hg_files\rsid_gene_country_codes')
files=[file  for file in os.listdir() if  file[0].isupper()]
print(files)

file_rsid_dict = {}
def extracting_rsid_from_file(filename):
    df = pd.read_csv(filename)
    file_rsid_dict[filename] = set(df['rsid'].values)
    #return file_rsid_dict

for file in files:
    extracting_rsid_from_file(file)


print(len(file_rsid_dict))

# k=from_memberships([
# file_rsid_dict['A2_ALL_eur.csv'],
# file_rsid_dict['A2_ALL_eur_leave_ukbb.csv']
# ])
# print(k)

from upsetplot import generate_counts, plot,from_contents
from matplotlib import pyplot
contents = {
    'A2_ALL_eur.csv': file_rsid_dict['A2_ALL_eur.csv'],
    "A2_ALL_eur_leave_ukbb.csv":file_rsid_dict['A2_ALL_eur_leave_ukbb.csv'],
    "A2_ALL_leave_23andme.csv":file_rsid_dict['A2_ALL_leave_23andme.csv'],
    "A2_ALL_leave_UKBB.csv":file_rsid_dict['A2_ALL_leave_UKBB.csv']

}
k=from_contents(contents)
#plot(k, orientation='vertical', show_counts='%d')
plot(k, show_counts='%d')
pyplot.show()
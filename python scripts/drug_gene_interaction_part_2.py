import pandas as pd
hgi_df = pd.read_csv(r"C:\Users\rsurulinathan\Downloads\selectfromhgi.csv")

#print(hgi_df.columns)

# grouping gene name and rsid
"""
MAPT-AS1,['rs7221167', 'rs7221167'],2
LINC00298,['rs34452414', 'rs35400177', 'rs62104919'],3
"""
# gene_rsid_dict = {}
# for gene in set(hgi_df['gene_name'].dropna()):
#     rsid_list = (hgi_df[hgi_df['gene_name'] == gene ]['rsid'].tolist())
#     gene_rsid_dict[gene] = rsid_list
#
#
# # print(gene_rsid_dict)
#
# df = pd.DataFrame({
#     "gene_name": gene_rsid_dict.keys(),
#     "rsid": gene_rsid_dict.values()
# })
# df['rsid'] = df['rsid'].apply(lambda x: eval(x)  if type(x) == str else x)
# df['rsid_count'] = df['rsid'].apply(lambda x:len(x))
# print(df.head())
#
# df.to_csv("hgi_gene_rsid.csv",sep=";", index=False)


# Reading the hgi_gene_rsid file

hgi_gene_rsid_df = pd.read_csv("hgi_gene_rsid.csv", sep= ";")
print(hgi_gene_rsid_df.head())

hgi_gene_rsid_df.sort_values(by=['rsid_count'],inplace=True,ascending=False)

hgi_gene_rsid_df.to_csv("hgi_gene_rsid.csv",sep=";", index=False)


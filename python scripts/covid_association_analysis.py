import pandas as pd
import matplotlib.pyplot as plt

score_df = pd.read_csv("score_all.csv")

score_gene_list = score_df['gene_name'].values.tolist()
#print(len(score_gene_list))

hgi_df = pd.read_csv(r"C:\Users\rsurulinathan\Downloads\selectfromhgi.csv")
hgi_gene_list = hgi_df['gene_name'].dropna()
#print(len(set(hgi_gene_list)))
hgi_gene_list.to_csv("hgi_gene_alone.csv", index=False)

# common elements between 2 sets
common_gene_name_list= set(hgi_gene_list).intersection(set(score_gene_list))
print(*sorted(common_gene_name_list))
# print(len (common_gene_name_list))

#
common_gene_score_list = [score_df[score_df["gene_name"]== gene]["association_score_overall"].values.astype(float)[0] for gene in common_gene_name_list]
#print(common_gene_score_list)
#
gene_score = dict(zip(common_gene_name_list,common_gene_score_list))

sorted_gene_score = {k: v for k, v in sorted(gene_score.items(), key=lambda item: item[1], reverse=True)}


bar = plt.barh( list(sorted_gene_score.keys() ),list(sorted_gene_score.values()))
plt.title("Plot of HGI Genes and Association Score")
plt.xlabel("COVID-19 Association Score")
plt.ylabel("Genes found")
plt.xticks(rotation=90)
plt.savefig(r"C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\covid19score.pdf" )
plt.show()


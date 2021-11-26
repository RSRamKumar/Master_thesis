import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
pd.options.mode.chained_assignment = None  # default='warn'
os.chdir(r'C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files\hg_files\rsid_gene_country_continent_codes')

os.mkdir("summary_pie_plots")
def making_pie_chart(ref_alt_rsid_comparison,chromosome_rsid_comparison,gene_rsid_comparison,rsid_AF_comparison,filename=None):
    name,ext = os.path.splitext(filename)
    fig, axs = plt.subplots(3, 2, figsize=(15, 8))
    fig.suptitle('Summary of the file "{}"'.format(filename), fontsize=16) # explode=(0.1, 0, 0, 0, 0) autopct='%1.1f%%'
    axs[0,0].pie(ref_alt_rsid_comparison, labels=ref_alt_rsid_comparison.index, normalize=True,autopct='%1.1f%%');
    axs[0,0].title.set_text('Allele and rsid comparison')

    axs[0, 1].pie(chromosome_rsid_comparison, labels=chromosome_rsid_comparison.index, normalize=True, autopct='%1.1f%%');
    axs[0, 1].title.set_text('Chromosome and rsid comparison')

    axs[1,0].pie(gene_rsid_comparison.head(), labels=gene_rsid_comparison.index[:5], normalize=True, autopct='%1.1f%%');
    axs[1,0].title.set_text('Gene and rsid comparison')

    axs[1, 1].pie(rsid_AF_comparison, labels=rsid_AF_comparison.index, normalize=True, autopct='%1.1f%%');
    axs[1, 1].title.set_text('rsid and minimum allele frequency comparison')

    plt.xticks(rotation=30)
    axs[2,0].bar(gene_rsid_comparison.index[:10], gene_rsid_comparison.values[:10],width = 0.4)

    axs[2, 1].bar(gene_rsid_comparison.index[:10], gene_rsid_comparison.values[:10],width = 1.0)

    fig.savefig("summary_pie_plots/{}_summary_pie.jpg".format(name))
    fig.tight_layout()

def summarizing_snps(filename):
    df = pd.read_csv(filename)
    df['ref:alt'] = df['REF'] + ":" + df['ALT']
    df = df[['#CHR', "POS", "REF", "ALT", "all_meta_AF", "rsid", "gene_name", "gene_id", "url", "continent_codes", "ref:alt"]]

    df = df.replace(to_replace='None', value=np.nan).dropna()

     #df.dropna(inplace=True)

    ref_alt_rsid_comparison = df.groupby(['ref:alt'])['rsid'].nunique().sort_values(ascending=False).head()
    chromosome_rsid_comparison = df.groupby(['#CHR'])['rsid'].nunique().sort_values(ascending=False).head()
    gene_rsid_comparison = df.groupby(['gene_name'])['rsid'].nunique().sort_values(ascending=False)
    #study_rsid_comparison = df.groupby(['study'])['rsid'].count().sort_values(ascending=False)
    rsid_AF_comparison = df.groupby(['rsid'])['all_meta_AF'].mean().sort_values(ascending=False).head()


    making_pie_chart(ref_alt_rsid_comparison,chromosome_rsid_comparison,gene_rsid_comparison,rsid_AF_comparison, filename=filename)



files=[file  for file in os.listdir() if  file[0].isupper()]
for file in files:
    summarizing_snps(file)

#print( (summarizing_snps(files[2])))













#https://www.gormanalysis.com/blog/python-pandas-for-your-grandpa-3-9-dataframe-groupby/
#https://stackoverflow.com/questions/42513049/get-all-keys-from-groupby-object-in-pandas
# https://stackoverflow.com/questions/45512763/python-pandas-dataframe-remove-all-rows-where-none-is-the-value-in-any-column
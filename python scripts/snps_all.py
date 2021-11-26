import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

url = "https://storage.googleapis.com/covid19-hg-public/20201215/results/20210107/COVID19_HGI_C2_ALL_leave_UKBB_23andme_20210107.txt.gz_1.0E-5.txt"
df=pd.read_csv(url,sep='\t')
print(df.head())

columns = ['#CHR', 'POS','REF' ,'ALT','all_meta_AF','rsid' ]

snp_table = df[columns]
snp_null_count = snp_table.isna().sum()['rsid']
print("There are {} null SNPs in the file".format(snp_null_count))
snp_table.dropna(inplace=True)

studies = str(['ACCOuNT_AFR', 'BQC19_EUR', 'BelCovid_EUR', 'BioVU_EUR', 'CCPM_EUR', 'CU_AFR', 'CU_EUR', 'DECODE_EUR', 'EstBB_EUR', 'FinnGen_FIN', 'GCAT_EUR', 'GENCOVID_EUR', 'GFG_EUR', 'GHS_Freeze_145_EUR', 'GNH_SAS', 'Genotek_EUR', 'INTERVAL_EUR', 'JapanTaskForce_EAS', 'LGDB_EUR', 'Lifelines_EUR', 'MSHS_CGI_EUR', 'Stanford_EUR', 'TOPMed_CHRIS10K_EUR', 'TOPMed_Gardena_EUR', 'UCLA_AMR', 'UCLA_EUR', 'SPGRX_EUR', 'PMBB_AFR', 'QGP_ARAB', 'MVP_AFR', 'MVP_EUR', 'MVP_HIS', 'Corea_EAS', 'genomicsengland100kgp_EUR', 'Helix_EUR', 'MGI_EUR', 'NTR_EUR', 'PHBB_AFR', 'PHBB_EUR', 'PHBB_HIS', 'Ancestry_EUR', 'BRACOVID_AMR', 'Genetics_COVID19_Korea_EAS', 'idipaz24genetics_EUR', 'Amsterdam_UMC_COVID_study_group_EUR', 'HOSTAGE_EUR', 'SweCovid_EUR', 'genomicc_EAS', 'genomicc_EUR'])

snp_table['studies']=studies
#(snp_table.head())

snp_table.to_csv("C2_ALL_leave_UKBB.csv",index=False)
import os
import pandas as pd
os.chdir(r"C:\Users\rsurulinathan\Desktop\Ram Kumar Master thesis files")

clinicaltrial_df = pd.read_excel("clinicaltrialsgov.xlsx")
ct_id = clinicaltrial_df['NCT Number'].values
print(len(ct_id),len(set(ct_id)))


covid_trials_df = pd.read_csv("covid-trials.csv")
covid_trials_df_id = covid_trials_df['ID'].values
print(len(covid_trials_df_id),len(set(covid_trials_df_id)))

comb = list(set(ct_id)) + list(set(covid_trials_df_id))
print(len(comb))

pd.DataFrame(comb).to_csv("trial_ids.csv",index=False,header=None)
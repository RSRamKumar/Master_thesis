import pandas as pd
from ast import literal_eval

df = pd.read_csv(r'C:\Users\rsurulinathan\Downloads\cts.tsv',sep='\t')
                # converters={'location_countries': eval})
df= df.fillna(value="NA")
 #print(df.head(31))
df['location_countries'] = df.location_countries.apply(lambda x: x[1:-1].strip().split(',')if x[0]=="[" else x )
print(df['location_countries'].head(50))


# for index,val in enumerate(df['location_countries']) :
#     if pd.isna(val):
#         print(index)


from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2
continents = {
    'NA': 'North America',
    'SA': 'South America',
    'AS': 'Asia',
    'OC': 'Australia',
    'AF': 'Africa',
    'EU':'Europe'
}
# countries_list = ['India', 'Australia','Belgium','Russia',['Ukraine','Burkina Faso'],['China']]
# continent_list =[]
# for cou in countries_list:
#     if type(cou) != list:
#           continent_list.append(continents[country_alpha2_to_continent_code(country_name_to_country_alpha2(cou))])
#     if type(cou)==list:
#         temp=[]
#         for c in cou:
#             temp.append(continents[country_alpha2_to_continent_code(country_name_to_country_alpha2(c))])
#         continent_list.append(temp)
# print(continent_list)

def converting_countries_to_continents(countries_list):
    continent_list = []
    for  index,cou in  enumerate(countries_list):
        #print(index)
        if cou != "NA":
            if type(cou) != list and cou == "Republic of Korea":
                #print("korea found")
                continent_list.append("Asia")
            elif type(cou) != list and cou == "Côte D'Ivoire":
                continent_list.append("Africa")
            elif type(cou) != list:
                continent_list.append(continents[country_alpha2_to_continent_code(country_name_to_country_alpha2(cou))])
            elif type(cou) == list:
                #print(cou)
                temp = []
                for c in cou:
                    if c.strip() =="Republic of Korea":
                        #print("gere")
                        temp.append("Asia")
                    else:
                        temp.append(continents[country_alpha2_to_continent_code(country_name_to_country_alpha2(c.strip()))])
                continent_list.append(temp)
        else:
            continent_list.append("NA")

    return continent_list


# df['continents']=converting_countries_to_continents(df['location_countries'])
# print(df.head())
# print(df.tail())
# #print(df.loc[5893])
#
# df.to_csv(r'C:\Users\rsurulinathan\Downloads\continent_added_cts.tsv',sep='\t',index=False)


#https://stackoverflow.com/questions/23111990/pandas-dataframe-stored-list-as-string-how-to-convert-back-to-list
#https://stackoverflow.com/questions/45758646/pandas-convert-string-into-list-of-strings
#https://stackoverflow.com/questions/14714181/conditional-logic-on-pandas-dataframe
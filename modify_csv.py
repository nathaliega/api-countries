import pandas as pd
import requests
import json

df = pd.read_csv('data/data.csv')


countries = df['Country Name'].unique()

df['Continent'] = '' 


for country in countries:
    cts = df[df['Country Name']== country].index
    try:
        continent = requests.get(f"https://restcountries.com/v3.1/name/{country}").json()[0]['continents'][0]
    except KeyError:
        continent = 'UNIDENTIFIED'
    df.loc[cts, "Continent"] = continent



df.to_csv('data/output.csv', index=False)
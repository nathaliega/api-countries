import pandas as pd 
from sql import crud, schemas 

df = pd.read_csv('data/output2.csv')

# continents = df['Continent'].unique()

# for continent in continents:
#     crud.add_continent(schemas.ContinentBase(continent_name=continent))
    

countries = df['Country Name'].unique()

years = list(df.columns)[2:12]

for country in countries:
    rows = df[df['Country Name'] == country].values
    
    for i,year in enumerate(years):
        crud.add_country(schemas.CountryBase(
            continent_id= crud.get_continent_by_name(rows[0][12]).continent_id,
            country_name= country,
            year= int(year),
            GDP= float(rows[0][i+2]),
            GDP_growth= float(rows[1][i + 2]),
            GDP_pc = float(rows[2][i+2]), 
            inflation= float(rows[3][i+2]) if not pd.isnull(rows[3][i+2]) else None,
            population=float(rows[4][i+2]),
            surface= float(rows[5][i+2]),
            imports= float(rows[6][i+2]),
            exports= float(rows[7][i+2])
        ))




# regions = df['Region'].unique()

# for region in regions: 

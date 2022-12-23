import pandas as pd
import requests

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
print('done')


df['Region'] = '' 

for country in countries:
    cts = df[df['Country Name']== country].index
    try: 
        region = requests.get(f"https://restcountries.com/v3.1/name/{country}").json()[0]['region']
    except KeyError:
        region = 'UNIDENTIFIED'
    df.loc[cts, "Region"] = region
print('done')




df.to_csv('data/output.csv', index=False)



# class User:
    
#     def __init__(self,name, password) -> None:
#         self.name = name
#         self.password = password

#     def say_hi():
#         print(hi im {self.name})


# class UserModel(Pydantic_model):
#     name: str
#     password: str


# u_model = UserModel(name=json[0], password=json[1])


# u_model.dict():

# {
#     name: json[0],
#     password: json[1]
# }



# u1 = User(**u_model.dict())

# u1 = User(name=json[0], password=json[1])

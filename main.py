from fastapi import FastAPI
from sql import  *
import uvicorn

app = FastAPI()

@app.get("/country/{country_name}", response_model=schemas.CountryBase)
def get_country_by_name(country_name: str):
    return crud.get_country_by_name(country_name)


# crud.test_cont()
# crud.test()
# crud.get_country_by_name()

# crud.add_country(schemas.CountryBase(
#     country_name="Ecuador",
#     year=2002,
#     GDP=2,
#     GDP_growth=0,
#     GDP_pc=2,
#     inflation=100,
#     population=1,
#     surface=200,
#     imports=10000,
#     exports=0,
#     continent_id=crud.get_continent_by_name("America").continent_id
# ))


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False, log_level="debug",
                workers=1, limit_concurrency=1, limit_max_requests=1)

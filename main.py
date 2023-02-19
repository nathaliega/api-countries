from fastapi import FastAPI, Depends
from sql import database, crud, schemas
import uvicorn
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

app = FastAPI(
    title="Countries API",
    description="""This API was built with FastAPI and exists to find some
                of the main economics indicators of countries around
                the world.""",
    root_path="/nathalie/api"
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# region country


@app.get("/country/{country_name}", response_model=schemas.ReturnCountry,
         summary="Get information of a country by its name",
         tags=["Countries"])
def get_country_by_name(country_name: str, db: Session = Depends(get_db)):
    try:
        rows = crud.get_country_by_name(country_name.capitalize(), db)
        my_dict = {}
        for row in rows:
            my_dict[str(row.year)] = row
            final_dict = {
                "country_name": country_name,
                "continent": rows[0].continent,
                "region": rows[0].region,
                "years": my_dict
            }
        return final_dict
    except crud.NotFoundException:
        return JSONResponse(status_code=404,
                            content={"message": "Country not found :("})


@app.get("/country/{country}/{year}", response_model=schemas.LongCountry,
         summary="Get information of a country by year", tags=["Countries"])
def get_country_by_year(country: str, year: int, db: Session = Depends(get_db)):
    try:
        return crud.country_by_year(country, year, db)
    except crud.NotFoundException:
        return JSONResponse(status_code=404,
                            content={"message": "Year not found :("})


@app.post("/country/", response_model=schemas.LongCountry,
          summary="Adds country to the database", tags=["Countries"])
def create_country(country: schemas.CountryCreate,
                   db: Session = Depends(get_db)):
    return crud.add_country(country, db)


# endregion country


# region continent

@app.get("/continent/{continent_name}", 
         response_model=schemas.ReturnContinent,
         summary="Get countries that belong to a continent",
         tags=["Continent"])
def get_countries_by_continent(continent_name: str,
                               db: Session = Depends(get_db)):
    try:
        countries = crud.get_countries_from_continent(
                    continent_name.capitalize(), db)
        my_dict = {}
        for country in countries:
            my_dict[country.country_name] = country
        final_dict = {
            "continent_name": continent_name,
            "countries": my_dict
             }
        return final_dict
    except crud.NotFoundException:
        return JSONResponse(status_code=404,
                            content={"message": "Continent not found :("})


@app.post("/continent/", response_model=schemas.ContinentBase,
          summary="Add a continent to the database", tags=["Continent"])
def add_continent(continent: schemas.ContinentBase,
                  db: Session = Depends(get_db)):
    return crud.add_continent(continent, db)


# endregion continent


# region region

@app.get("/region/{region_name}", response_model=schemas.ReturnRegion,
         summary="Get countries that belong to a region", tags=["Region"])
def get_countries_by_region(region_name: str, db: Session = Depends(get_db)):
    try: 
        countries = crud.get_countries_from_region(region_name.capitalize(),
                                                   db)
        my_dict = {}
        for country in countries:
            my_dict[country.country_name] = country
        final_dict = {
            "region_name": region_name,
            "countries": my_dict
             }
        return final_dict
    except crud.NotFoundException:
        return JSONResponse(status_code=404,
                            content={"message": "Region not found :("})


@app.post("/region/", response_model=schemas.RegionBase,
          summary="Add a region to the database", tags=["Region"])
def add_region(region: schemas.RegionBase, db: Session = Depends(get_db)):
    return crud.add_region(region, db)

# endregion region


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True,
                workers=3)

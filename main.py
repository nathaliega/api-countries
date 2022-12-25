from fastapi import FastAPI, Depends
from sql import  *
import uvicorn
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally: 
        db.close()

# region country

@app.get("/country/{country_name}", response_model=schemas.ReturnCountry)
def get_country_by_name(country_name: str, db: Session = Depends(get_db)):
    try: 
        return crud.get_country_by_name(country_name.capitalize(), db)
    except crud.NotFoundException:
        return JSONResponse(status_code=404, content={"message": "Country not found :("})

# endregion

# @app.get("/country")



@app.get("/continent/{continent_name}", response_model=schemas.ReturnContinent)
def get_countries_by_continent(continent_name: str, db: Session = Depends(get_db)):
    try: 
        return crud.get_continent(continent_name.capitalize(), db)
    except crud.NotFoundException:
        return JSONResponse(status_code=404, content={"message": "Continent not found :("})



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=4557, reload=True,
                workers=3)

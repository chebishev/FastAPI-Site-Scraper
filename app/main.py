from fastapi import FastAPI, Query
import uvicorn
from .scrapper import valid_links

app = FastAPI()

@app.get(
    "/valid-links", 
    summary="Scrapes links from a website",
    description="This endpoint scrapes all the links from a given website (in format \"https://example.com/\") and returns them in a dictionary format where the key is the link address and the value is the link text."
    )
def get_valid_links(site: str  = Query(..., description="The URL of the site to scrape in format \"https://example.com/\"")):
    data = valid_links(site)
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

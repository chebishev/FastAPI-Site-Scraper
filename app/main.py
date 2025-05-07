from fastapi import FastAPI, Query
import uvicorn
from scrapper import valid_links


description = """
    Get all hrefs and corresponding text from website in format https://example.com
    """

app = FastAPI(
    title="Fast API SITE Scraper",
    description=description,
    summary="API that allows you to get all valid links from website in format https://example.com",
    version="0.0.3",
    contact={
        "name": "Atanas Chebishev",
        "url": "https://chebishev.github.io/",
        "email": "atanas.chebishev@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
)

tags_metadata = [
    {
        "name": "Scrapes links from a website",
        "description": "This endpoint scrapes all the links from a given website (in format \"https://example.com/\") and returns them in a dictionary format where the key is the link address and the value is the link text.",
    },
]

#Todo: add the tag to the endpoint
@app.get(
    "/valid-links", tags=["Scrapes links from a website"],
    )
def get_valid_links(web_address: str  = Query(..., description="The URL of the site to scrape in format \"https://example.com/\"")):
    data = valid_links(web_address)
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

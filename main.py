from fastapi import FastAPI

from api.scrape import router


# Initialize FastAPI app
app = FastAPI(
    title="Web Scraper API",
    description="A FastAPI application to scrape data from a website and store it in a database.",
    version="1.0.0",
)

app.include_router(router, tags=["Website Scraper"])


@app.get("/")
async def root():
    return {"message": "Service is up and running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

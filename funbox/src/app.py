import uvicorn
from fastapi import FastAPI, Response

from cache import cache_link_by_timestamp, get_links_by_timestamp


app = FastAPI()


@app.get("/")
async def home():
    return {"status": "App is runnung"}


@app.post("/visited_links/")
async def visited_links(links: list[str]) -> Response:
    cache_link_by_timestamp(links=links)

    return {"status": "ok"}


@app.get("/visited_domains/")
async def get_visited_links(ts_from: int | None = None, ts_to: int | None = None) -> Response:
    visited_links = set([])

    for links in get_links_by_timestamp(start=ts_from, end=ts_to):
        visited_links |= set(links)

    return {"domains": visited_links, "status": "ok"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)

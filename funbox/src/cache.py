import json
import os
import time

from redis import Redis


redis = Redis(
    host=os.environ.get("REDIS_HOST"),
    port=os.environ.get("REDIS_PORT"),
    decode_responses=True,
)


def cache_link_by_timestamp(links: list[str]) -> None:
    if links:
        unixtime = int(time.time())
        redis.set(unixtime, json.dumps(links))


def get_links_by_timestamp(start: int | None = None, end: int | None = None) -> list[str]:
    if start and end and start > end:
        start, end = end, start

    for key in redis.keys():
        ts = int(key)

        if start and ts < start:
            continue

        if end and ts > end:
            continue

        yield json.loads(redis.get(key))

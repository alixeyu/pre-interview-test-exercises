Links cacher is a service for storing links in Redis.

## REST API
### Store links in Redis

URL structure: ```POST /visited_links/```

#### Example
``` bash
curl -X POST http://127.0.0.1/visited_links/ --data "{\"links\": [\"www.google.com\"]}"
```

#### Parameters
```json
{
    "links": ["www.google.com"]
}
```

- **links** List of String. List of links that will be stored in Redis.


#### Returns

Returns the record which was stored in Redis.

``` json
{
    "1711185138": ["www.google.com"]
}
```

### Retrieve links

URL structure: ```GET /visited_domains/```

#### Example
``` bash
curl http://127.0.0.1/visited_domains/ -d ts_from=1711185100 -d ts_tp=1711185150
```

#### Parameters
- **ts_from** Integer. The Unix timestamp that's used for defining the start of period which links should be retrieved for.
- **ts_to** Integer. The Unix timestamp that's used for defining the end of period which links should be retrieved for.

#### Returns
``` json
{
    "domains": ["www.google.com"],
    "status": "ok"
}
```
This endpoint returns a JSON-encoded dictionary with the following fields:
- **domains** List of String. The list of links stored in Redis
- **status** String. The status of request.

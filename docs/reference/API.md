<!-- Generator: Widdershins v4.0.1 -->

<h1 id="albion-online-community-api-reference">Albion Online community API reference v1.0.0</h1>

Unofficial reference for an observed subset of Albion Online web APIs.
Routes and sample shapes were observed in specific requests; parameter requiredness,
accepted ranges, response stability, and complete server behavior are unverified.

Base hosts: `https://gameinfo.albiononline.com` serves the gameinfo routes shown
below, and `https://albiononline.com` serves the Character Builder and comment
routes. The events list also has two observed regional hosts, shown on that
operation. Do not infer that every host serves every route.

Illustrative request patterns (replace every angle-bracket placeholder with a
value you choose; these are not ready-to-run requests):

```http
GET https://gameinfo.albiononline.com/api/gameinfo/events?limit=<limit>&offset=<offset>
GET https://gameinfo.albiononline.com/api/gameinfo/events/<eventId>
GET https://gameinfo.albiononline.com/api/gameinfo/events/<subjectId>/history/<otherSubjectId>
GET https://albiononline.com/characterbuilder/api/builds/<buildId>
```

Query inputs and accepted combinations remain unverified. Reading this reference
sends no request, and the hosted Swagger UI disables request execution.

<h1 id="albion-online-community-api-reference-character-builder">Character Builder</h1>

## List builds

`GET /characterbuilder/api/builds/`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="list-builds-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|excludes|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `_trending`. This is not a complete accepted set.|
|limit|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `1`, `26`. This is not a complete accepted set.|
|offset|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `0`. This is not a complete accepted set.|
|type|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `single`, `group`. This is not a complete accepted set.|

> Example responses

> 200 Response

```json
[
  {
    "author": {},
    "builds": [],
    "createdAt": "string",
    "featured": {},
    "groupSize": {},
    "id": 0,
    "items": {},
    "likes": {},
    "published": {},
    "tags": {},
    "tiers": {},
    "title": "string",
    "type": "string",
    "updatedAt": "string",
    "visible": {}
  }
]
```

<h3 id="list-builds-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="list-builds-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» author|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» builds|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» createdAt|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» featured|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» groupSize|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» items|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» likes|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» published|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tags|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tiers|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» title|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» updatedAt|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» visible|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» author|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» builds|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» createdAt|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» featured|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» groupSize|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» items|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» likes|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» published|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tags|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tiers|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» title|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» updatedAt|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» visible|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

## Get a build

`GET /characterbuilder/api/builds/{buildId}`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="get-a-build-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|buildId|path|string|true|Identifier in the route. Format and accepted values are unverified.|

> Example responses

> 200 Response

```json
{
  "author": "string",
  "builds": [],
  "createdAt": "string",
  "description": "string",
  "featured": true,
  "groupSize": 0,
  "id": 0,
  "items": {},
  "likes": 0,
  "published": true,
  "tags": [],
  "tiers": [],
  "title": "string",
  "type": "string",
  "updatedAt": "string",
  "visible": true
}
```

<h3 id="get-a-build-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="get-a-build-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» author|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» builds|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» createdAt|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» description|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» featured|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» groupSize|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» likes|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» published|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» tags|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» tiers|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» title|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» updatedAt|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» visible|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» author|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» builds|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» createdAt|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» description|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» featured|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» groupSize|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» likes|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» published|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» tags|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» tiers|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» title|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» updatedAt|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» visible|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

## Featured builds

`GET /characterbuilder/api/featured`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="featured-builds-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `5`. This is not a complete accepted set.|
|offset|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `0`. This is not a complete accepted set.|
|type|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `single`, `group`. This is not a complete accepted set.|

> Example responses

> 200 Response

```json
[
  {
    "author": "string",
    "builds": [],
    "createdAt": "string",
    "featured": true,
    "groupSize": 0,
    "id": 0,
    "items": {},
    "likes": 0,
    "published": true,
    "tags": [],
    "tiers": [],
    "title": "string",
    "type": "string",
    "updatedAt": "string",
    "visible": true
  }
]
```

<h3 id="featured-builds-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="featured-builds-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» author|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» builds|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» createdAt|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» featured|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» groupSize|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» id|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» items|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» likes|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» published|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» tags|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» tiers|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» title|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» updatedAt|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» visible|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» author|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» builds|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» createdAt|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» featured|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» groupSize|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» id|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» items|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» likes|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» published|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» tags|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» tiers|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» title|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» updatedAt|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» visible|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

## Popular builds

`GET /characterbuilder/api/popularbuilds`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="popular-builds-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `26`, `51`. This is not a complete accepted set.|
|offset|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `0`, `50`. This is not a complete accepted set.|
|type|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `single`, `group`. This is not a complete accepted set.|

> Example responses

> 200 Response

```json
[
  {
    "author": "string",
    "builds": [],
    "createdAt": "string",
    "featured": true,
    "groupSize": 0,
    "id": 0,
    "items": {},
    "likes": 0,
    "published": true,
    "tags": [],
    "tiers": [],
    "title": "string",
    "type": "string",
    "updatedAt": "string",
    "visible": true
  }
]
```

<h3 id="popular-builds-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="popular-builds-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» author|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» builds|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» createdAt|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» featured|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» groupSize|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» likes|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» published|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tags|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» tiers|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» title|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» type|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» updatedAt|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» visible|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» author|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» builds|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» createdAt|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» featured|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» groupSize|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» likes|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» published|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tags|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» tiers|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» title|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» type|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» updatedAt|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» visible|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

<aside class="success">
This operation does not require authentication
</aside>

## Search builds

`GET /characterbuilder/api/search`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="search-builds-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|activeFilter[filterType]|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `tags`. This is not a complete accepted set.|
|activeFilter[filter]|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `pve`. This is not a complete accepted set.|
|activeFilter[title]|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `pve`. This is not a complete accepted set.|
|activeFilter[value]|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `2`. This is not a complete accepted set.|
|limit|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `6`, `51`. This is not a complete accepted set.|
|offset|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `0`. This is not a complete accepted set.|
|q|query|string|false|Observed query input; requiredness and accepted values are unverified.|
|showBadges|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `true`. This is not a complete accepted set.|
|type|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `single`, `group`, `guide`. This is not a complete accepted set.|

> Example responses

> 200 Response

```json
[
  {
    "author": {},
    "createdAt": {},
    "featured": {},
    "groupSize": {},
    "id": {},
    "items": {},
    "likes": {},
    "published": {},
    "tags": {},
    "tiers": {},
    "title": {},
    "type": {},
    "updatedAt": {},
    "visible": {}
  }
]
```

<h3 id="search-builds-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="search-builds-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» author|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» createdAt|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» featured|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» groupSize|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» likes|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» published|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tags|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tiers|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» title|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» type|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» updatedAt|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» visible|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» author|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» createdAt|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» featured|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» groupSize|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» likes|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» published|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tags|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» tiers|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» title|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» type|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» updatedAt|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» visible|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

## Trending builds

`GET /characterbuilder/api/trending`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="trending-builds-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `5`. This is not a complete accepted set.|
|offset|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `0`. This is not a complete accepted set.|
|type|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `single`, `group`. This is not a complete accepted set.|

> Example responses

> 200 Response

```json
[
  null
]
```

<h3 id="trending-builds-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="trending-builds-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Build list (sampled redirect)

`GET /characterbuilder/api/builds`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="build-list-(sampled-redirect)-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|excludes|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `_trending`. This is not a complete accepted set.|
|limit|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `26`. This is not a complete accepted set.|
|offset|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `0`. This is not a complete accepted set.|
|type|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `single`, `group`. This is not a complete accepted set.|

<h3 id="build-list-(sampled-redirect)-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|301|[Moved Permanently](https://tools.ietf.org/html/rfc7231#section-6.4.2)|HTTP 301 sampled for this path without the trailing slash. The redirect destination is unverified.|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="albion-online-community-api-reference-community">Community</h1>

## List comments

`GET /killboard/api/comment/list`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="list-comments-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `20`. This is not a complete accepted set.|
|offset|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `0`. This is not a complete accepted set.|
|reference|query|string|false|Observed query input; requiredness and accepted values are unverified.|

> Example responses

> 200 Response

```json
{
  "commentCount": 0,
  "comments": []
}
```

<h3 id="list-comments-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="list-comments-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» commentCount|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» comments|array|false|none|Optional field seen in an observed sample; server contract unverified.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» commentCount|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» comments|array|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="albion-online-community-api-reference-events">Events</h1>

## List events

`GET /api/gameinfo/events`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="list-events-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|allianceId|query|string|false|Observed query input; requiredness and accepted values are unverified.|
|guildId|query|string|false|Observed query input; requiredness and accepted values are unverified.|
|limit|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `51`, `1`, `11`. This is not a complete accepted set.|
|offset|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `0`, `50`. This is not a complete accepted set.|

> Example responses

> 200 Response

```json
[
  {
    "BattleId": {},
    "Category": {},
    "EventId": {},
    "GroupMembers": {},
    "GvGMatch": {},
    "KillArea": {},
    "Killer": {},
    "Location": {},
    "Participants": {},
    "TimeStamp": {},
    "TotalVictimKillFame": {},
    "Type": {},
    "Version": {},
    "Victim": {},
    "groupMemberCount": {},
    "numberOfParticipants": {}
  }
]
```

<h3 id="list-events-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="list-events-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» BattleId|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Category|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» EventId|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» GroupMembers|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» GvGMatch|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» KillArea|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Killer|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Location|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Participants|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» TimeStamp|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» TotalVictimKillFame|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Type|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Version|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Victim|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» groupMemberCount|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» numberOfParticipants|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» BattleId|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Category|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» EventId|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» GroupMembers|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» GvGMatch|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» KillArea|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Killer|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Location|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Participants|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|array|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» TimeStamp|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» TotalVictimKillFame|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Type|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|string|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Version|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» Victim|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» groupMemberCount|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» numberOfParticipants|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. Type was not captured.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

## Get an event

`GET /api/gameinfo/events/{eventId}`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="get-an-event-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|eventId|path|string|true|Identifier in the route. Format and accepted values are unverified.|

> Example responses

> 200 Response

```json
{
  "BattleId": 0,
  "Category": null,
  "EventId": 0,
  "GroupMembers": [],
  "GvGMatch": null,
  "KillArea": "string",
  "Killer": {},
  "Location": null,
  "Participants": [],
  "TimeStamp": "string",
  "TotalVictimKillFame": 0,
  "Type": "string",
  "Version": 0,
  "Victim": {},
  "groupMemberCount": 0,
  "numberOfParticipants": 0
}
```

<h3 id="get-an-event-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="get-an-event-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» BattleId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Category|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» EventId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GroupMembers|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GvGMatch|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» KillArea|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Killer|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Location|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» Participants|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TimeStamp|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TotalVictimKillFame|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Version|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Victim|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» groupMemberCount|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» numberOfParticipants|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» BattleId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Category|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» EventId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GroupMembers|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GvGMatch|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» KillArea|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Killer|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Location|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» Participants|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TimeStamp|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TotalVictimKillFame|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Version|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Victim|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» groupMemberCount|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» numberOfParticipants|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

## Event history between two identifiers

`GET /api/gameinfo/events/{subjectId}/history/{otherSubjectId}`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="event-history-between-two-identifiers-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|subjectId|path|string|true|Identifier in the route. Format and accepted values are unverified.|
|otherSubjectId|path|string|true|Identifier in the route. Format and accepted values are unverified.|

> Example responses

> 200 Response

```json
[
  {
    "BattleId": 0,
    "Category": null,
    "EventId": 0,
    "GroupMembers": [],
    "GvGMatch": null,
    "KillArea": "string",
    "Killer": {},
    "Location": null,
    "Participants": [],
    "TimeStamp": "string",
    "TotalVictimKillFame": 0,
    "Type": "string",
    "Version": 0,
    "Victim": {},
    "groupMemberCount": 0,
    "numberOfParticipants": 0
  }
]
```

<h3 id="event-history-between-two-identifiers-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="event-history-between-two-identifiers-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» BattleId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Category|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» EventId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GroupMembers|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GvGMatch|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» KillArea|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Killer|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Location|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» Participants|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TimeStamp|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TotalVictimKillFame|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Version|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Victim|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» groupMemberCount|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» numberOfParticipants|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» BattleId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Category|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» EventId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GroupMembers|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GvGMatch|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» KillArea|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Killer|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Location|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» Participants|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TimeStamp|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TotalVictimKillFame|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Version|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Victim|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» groupMemberCount|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» numberOfParticipants|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

## Kill fame rankings

`GET /api/gameinfo/events/killfame`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="kill-fame-rankings-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `6`. This is not a complete accepted set.|
|offset|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `0`. This is not a complete accepted set.|
|range|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `week`, `lastWeek`. This is not a complete accepted set.|

> Example responses

> 200 Response

```json
[
  {
    "BattleId": 0,
    "Category": null,
    "EventId": 0,
    "GroupMembers": [],
    "GvGMatch": null,
    "KillArea": "string",
    "Killer": {},
    "Location": null,
    "Participants": [],
    "TimeStamp": "string",
    "TotalVictimKillFame": 0,
    "Type": "string",
    "Version": 0,
    "Victim": {},
    "groupMemberCount": 0,
    "numberOfParticipants": 0
  }
]
```

<h3 id="kill-fame-rankings-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="kill-fame-rankings-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» BattleId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Category|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» EventId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GroupMembers|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GvGMatch|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» KillArea|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Killer|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Location|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» Participants|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TimeStamp|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TotalVictimKillFame|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Version|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Victim|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» groupMemberCount|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» numberOfParticipants|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» BattleId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Category|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» EventId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GroupMembers|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GvGMatch|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» KillArea|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Killer|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Location|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» Participants|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TimeStamp|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TotalVictimKillFame|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Version|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Victim|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» groupMemberCount|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» numberOfParticipants|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="albion-online-community-api-reference-alliances">Alliances</h1>

## Get an alliance

`GET /api/gameinfo/alliances/{allianceId}`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="get-an-alliance-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|allianceId|path|string|true|Identifier in the route. Format and accepted values are unverified.|

> Example responses

> default Response

```json
{
  "AllianceId": "string",
  "AllianceName": "string",
  "AllianceTag": "string",
  "Founded": "string",
  "FounderId": "string",
  "FounderName": "string",
  "Guilds": [],
  "NumPlayers": 0
}
```

<h3 id="get-an-alliance-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="get-an-alliance-responseschema">Response Schema</h3>

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» AllianceId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» AllianceName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» AllianceTag|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Founded|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» FounderId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» FounderName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Guilds|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» NumPlayers|number|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="albion-online-community-api-reference-battles">Battles</h1>

## List battles

`GET /api/gameinfo/battles`

An Americas request on 2026-10-21 UTC returned a JSON array. Requests
using `sort=recent`, `limit=1` or `2`, and `offset=0` or `1` returned
populated arrays in the sampled calls. These observations do not establish
parameter bounds, defaults, requiredness, stable ordering, or pagination
behavior. The response shape is a limited observation; generated examples
are illustrative shape diagrams, not captured payloads.

<h3 id="list-battles-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|sort|query|string|false|Observed query input: `recent`. Other accepted values and behavior are unverified.|
|limit|query|string|false|Observed query input: `1`, `2`. Bounds, defaults, and count behavior are unverified.|
|offset|query|string|false|Observed query input: `0`, `1`. Bounds, defaults, and pagination behavior are unverified.|

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "startTime": "string",
    "endTime": "string",
    "totalFame": 0,
    "totalKills": 0,
    "players": {
      "property1": {},
      "property2": {}
    },
    "guilds": {
      "property1": {},
      "property2": {}
    },
    "alliances": {
      "property1": {},
      "property2": {}
    }
  }
]
```

<h3 id="list-battles-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|JSON array observed from the Americas host on 2026-10-21 UTC. The sample does not establish a complete or stable server contract.|Inline|

<h3 id="list-battles-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|integer|false|none|Optional field seen in the sampled battle objects.|
|» startTime|string|false|none|Optional field seen in the sampled battle objects.|
|» endTime|string|false|none|Optional field seen in the sampled battle objects.|
|» totalFame|integer|false|none|Optional field seen in the sampled battle objects.|
|» totalKills|integer|false|none|Optional field seen in the sampled battle objects.|
|» players|object|false|none|Optional map seen in sampled battle objects; keys and complete entry shape are unverified.|
|»» **additionalProperties**|object|false|none|none|
|» guilds|object|false|none|Optional map seen in sampled battle objects; keys and complete entry shape are unverified.|
|»» **additionalProperties**|object|false|none|none|
|» alliances|object|false|none|Optional map seen in sampled battle objects; keys and complete entry shape are unverified.|
|»» **additionalProperties**|object|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Get a battle

`GET /api/gameinfo/battles/{battleId}`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="get-a-battle-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|battleId|path|string|true|Identifier in the route. Format and accepted values are unverified.|

> Example responses

> default Response

```json
{
  "alliances": {
    "property1": {
      "deaths": 0,
      "id": "string",
      "killFame": 0,
      "kills": 0,
      "name": "string"
    },
    "property2": {
      "deaths": 0,
      "id": "string",
      "killFame": 0,
      "kills": 0,
      "name": "string"
    }
  },
  "battle_TIMEOUT": 0,
  "clusterName": null,
  "endTime": "string",
  "guilds": {
    "property1": {
      "alliance": "string",
      "allianceId": "string",
      "deaths": 0,
      "id": "string",
      "killFame": 0,
      "kills": 0,
      "name": "string"
    },
    "property2": {
      "alliance": "string",
      "allianceId": "string",
      "deaths": 0,
      "id": "string",
      "killFame": 0,
      "kills": 0,
      "name": "string"
    }
  },
  "id": 0,
  "players": {
    "property1": {
      "allianceId": "string",
      "allianceName": "string",
      "deaths": 0,
      "guildId": "string",
      "guildName": "string",
      "id": "string",
      "killFame": 0,
      "kills": 0,
      "name": "string"
    },
    "property2": {
      "allianceId": "string",
      "allianceName": "string",
      "deaths": 0,
      "guildId": "string",
      "guildName": "string",
      "id": "string",
      "killFame": 0,
      "kills": 0,
      "name": "string"
    }
  },
  "startTime": "string",
  "timeout": "string",
  "totalFame": 0,
  "totalKills": 0
}
```

<h3 id="get-a-battle-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="get-a-battle-responseschema">Response Schema</h3>

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» alliances|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|»» **additionalProperties**|object|false|none|none|
|»»» deaths|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» id|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» killFame|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» kills|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» name|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» battle_TIMEOUT|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» clusterName|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» endTime|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» guilds|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|»» **additionalProperties**|object|false|none|none|
|»»» alliance|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» allianceId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» deaths|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» id|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» killFame|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» kills|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» name|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» id|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» players|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|»» **additionalProperties**|object|false|none|none|
|»»» allianceId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» allianceName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» deaths|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» guildId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» guildName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» id|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» killFame|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» kills|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» name|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» startTime|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» timeout|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» totalFame|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» totalKills|number|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="albion-online-community-api-reference-guilds">Guilds</h1>

## Get a guild

`GET /api/gameinfo/guilds/{guildId}`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="get-a-guild-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|guildId|path|string|true|Identifier in the route. Format and accepted values are unverified.|

> Example responses

> default Response

```json
{
  "AllianceId": "string",
  "AllianceName": null,
  "AllianceTag": "string",
  "AttacksWon": null,
  "DeathFame": 0,
  "DefensesWon": null,
  "Founded": "string",
  "FounderId": "string",
  "FounderName": "string",
  "Id": "string",
  "Logo": null,
  "MemberCount": 0,
  "Name": "string",
  "killFame": 0
}
```

<h3 id="get-a-guild-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="get-a-guild-responseschema">Response Schema</h3>

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» AllianceId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» AllianceName|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» AllianceTag|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» AttacksWon|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» DeathFame|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» DefensesWon|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» Founded|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» FounderId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» FounderName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Id|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Logo|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» MemberCount|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Name|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» killFame|number|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

## Guild feud

`GET /api/gameinfo/guilds/{guildId}/feud/{otherGuildId}`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="guild-feud-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|guildId|path|string|true|Identifier in the route. Format and accepted values are unverified.|
|otherGuildId|path|string|true|Identifier in the route. Format and accepted values are unverified.|

> Example responses

> 200 Response

```json
[
  {
    "BattleId": 0,
    "Category": null,
    "EventId": 0,
    "GroupMembers": [],
    "GvGMatch": null,
    "KillArea": "string",
    "Killer": {},
    "Location": null,
    "Participants": [],
    "TimeStamp": "string",
    "TotalVictimKillFame": 0,
    "Type": "string",
    "Version": 0,
    "Victim": {},
    "groupMemberCount": 0,
    "numberOfParticipants": 0
  }
]
```

<h3 id="guild-feud-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="guild-feud-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» BattleId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Category|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» EventId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GroupMembers|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GvGMatch|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» KillArea|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Killer|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Location|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» Participants|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TimeStamp|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TotalVictimKillFame|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Version|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Victim|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» groupMemberCount|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» numberOfParticipants|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» BattleId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Category|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» EventId|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GroupMembers|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GvGMatch|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» KillArea|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Killer|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Location|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» Participants|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TimeStamp|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» TotalVictimKillFame|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Type|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Version|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Victim|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» groupMemberCount|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» numberOfParticipants|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="albion-online-community-api-reference-items">Items</h1>

## Get item data

`GET /api/gameinfo/items/{itemId}/data`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="get-item-data-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|itemId|path|string|true|Identifier in the route. Format and accepted values are unverified.|

> Example responses

> 200 Response

```json
{
  "abilityPower": 0,
  "activeSlots": {},
  "activeSpellSlots": 0,
  "attackDamage": 0,
  "attackRange": 0,
  "attackSpeed": 0,
  "attackType": "string",
  "categoryId": "string",
  "categoryName": "string",
  "craftingRequirements": {},
  "durability": 0,
  "durabilityLossAttack": 0,
  "durabilityLossReceivedattack": 0,
  "durabilityLossReceivedspell": 0,
  "durabilityLossSpelluse": 0,
  "enchantmentLevel": 0,
  "enchantments": {},
  "equipable": true,
  "fxboneName": null,
  "hitpointsMax": 0,
  "hitpointsRegenerationBonus": 0,
  "itemPower": 0,
  "itemPowerProgressionType": "string",
  "itemType": "string",
  "level": 0,
  "localizedDescriptions": {},
  "localizedNames": {},
  "magicAttackDamageBonus": null,
  "magicResistance": 0,
  "magicspellDamageBonus": 0,
  "mainhandAnimationType": "string",
  "maxQualityLevel": 0,
  "maxStackSize": 0,
  "passiveSlots": {},
  "passiveSpellSlots": 0,
  "physicalArmor": 0,
  "physicalAttackDamageBonus": 0,
  "physicalSpellDamageBonus": 0,
  "revision": 0,
  "showinmarketplace": true,
  "skinCount": {},
  "slotType": "string",
  "spriteName": "string",
  "stackable": true,
  "tier": 0,
  "transformation": null,
  "twoHanded": true,
  "uiAtlas": null,
  "uiSprite": "string",
  "uiSpriteOverlay1": null,
  "uiSpriteOverlay2": null,
  "uiSpriteOverlay3": null,
  "unequipInCombat": null,
  "uniqueName": "string",
  "unlockedToEquip": true,
  "weight": 0
}
```

<h3 id="get-item-data-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="get-item-data-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» abilityPower|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» activeSlots|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» activeSpellSlots|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» attackDamage|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» attackRange|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» attackSpeed|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» attackType|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» categoryId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» categoryName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» craftingRequirements|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» durability|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» durabilityLossAttack|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» durabilityLossReceivedattack|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» durabilityLossReceivedspell|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» durabilityLossSpelluse|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» enchantmentLevel|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» enchantments|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» equipable|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» fxboneName|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» hitpointsMax|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» hitpointsRegenerationBonus|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» itemPower|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» itemPowerProgressionType|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» itemType|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» level|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» localizedDescriptions|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» localizedNames|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» magicAttackDamageBonus|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» magicResistance|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» magicspellDamageBonus|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» mainhandAnimationType|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» maxQualityLevel|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» maxStackSize|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» passiveSlots|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» passiveSpellSlots|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» physicalArmor|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» physicalAttackDamageBonus|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» physicalSpellDamageBonus|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» revision|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» showinmarketplace|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» skinCount|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» slotType|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» spriteName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» stackable|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» tier|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» transformation|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» twoHanded|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» uiAtlas|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» uiSprite|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» uiSpriteOverlay1|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» uiSpriteOverlay2|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» uiSpriteOverlay3|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» unequipInCombat|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» uniqueName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» unlockedToEquip|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» weight|number|false|none|Optional field seen in an observed sample; server contract unverified.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» abilityPower|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» activeSlots|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» activeSpellSlots|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» attackDamage|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» attackRange|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» attackSpeed|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» attackType|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» categoryId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» categoryName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» craftingRequirements|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» durability|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» durabilityLossAttack|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» durabilityLossReceivedattack|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» durabilityLossReceivedspell|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» durabilityLossSpelluse|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» enchantmentLevel|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» enchantments|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» equipable|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» fxboneName|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» hitpointsMax|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» hitpointsRegenerationBonus|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» itemPower|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» itemPowerProgressionType|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» itemType|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» level|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» localizedDescriptions|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|object|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» localizedNames|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» magicAttackDamageBonus|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» magicResistance|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» magicspellDamageBonus|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» mainhandAnimationType|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» maxQualityLevel|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» maxStackSize|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» passiveSlots|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|» passiveSpellSlots|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» physicalArmor|integer|false|none|Optional field seen in an observed sample; server contract unverified.|
|» physicalAttackDamageBonus|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» physicalSpellDamageBonus|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» revision|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» showinmarketplace|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» skinCount|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» slotType|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» spriteName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» stackable|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» tier|any|false|none|Alternative optional field observations across samples; not exhaustive server types.|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|integer|false|none|Optional field seen in an observed sample; server contract unverified.|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» *anonymous*|number|false|none|Optional field seen in an observed sample; server contract unverified.|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» transformation|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» twoHanded|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» uiAtlas|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» uiSprite|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» uiSpriteOverlay1|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» uiSpriteOverlay2|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» uiSpriteOverlay3|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» unequipInCombat|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» uniqueName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» unlockedToEquip|boolean|false|none|Optional field seen in an observed sample; server contract unverified.|
|» weight|number|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

## Weapon categories

`GET /api/gameinfo/items/_weaponCategories`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

> Example responses

> 200 Response

```json
[
  {
    "id": "string",
    "name": "string"
  }
]
```

<h3 id="weapon-categories-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|HTTP 200 JSON sampled for specific requests. Properties shown in the schema are optional sample observations; their continued presence and types are unverified.|Inline|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="weapon-categories-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» name|string|false|none|Optional field seen in an observed sample; server contract unverified.|

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» id|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» name|string|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="albion-online-community-api-reference-crystal-league">Crystal League</h1>

## List Crystal League matches

`GET /api/gameinfo/matches/crystalleague`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="list-crystal-league-matches-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|category|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `crystal_league_nonlethal`, `crystal_league_city`, `ranked`. This is not a complete accepted set.|
|limit|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `51`. This is not a complete accepted set.|
|offset|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `0`. This is not a complete accepted set.|

> Example responses

> default Response

```json
[
  {
    "MatchId": "string",
    "category": "string",
    "crystalLeagueLevel": 0,
    "matchType": "string",
    "startTime": "string",
    "team1Guild": null,
    "team1LeaderId": "string",
    "team1Results": {
      "property1": {
        "Deaths": 0,
        "Fame": 0,
        "Healing": null,
        "IsMercenary": null,
        "Kills": 0,
        "Name": "string",
        "PlayerId": "string",
        "Team": "string"
      },
      "property2": {
        "Deaths": 0,
        "Fame": 0,
        "Healing": null,
        "IsMercenary": null,
        "Kills": 0,
        "Name": "string",
        "PlayerId": "string",
        "Team": "string"
      }
    },
    "team1Territory": null,
    "team1Tickets": 0,
    "team1Timeline": [],
    "team2Guild": null,
    "team2LeaderId": "string",
    "team2Results": {
      "property1": {},
      "property2": {}
    },
    "team2Territory": null,
    "team2Tickets": 0,
    "team2Timeline": [],
    "ttl": "string",
    "winner": 0
  }
]
```

<h3 id="list-crystal-league-matches-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="list-crystal-league-matches-responseschema">Response Schema</h3>

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» MatchId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» category|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» crystalLeagueLevel|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» matchType|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» startTime|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team1Guild|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» team1LeaderId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team1Results|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|»» **additionalProperties**|object|false|none|none|
|»»» Deaths|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» Fame|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» Healing|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|»»» IsMercenary|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|»»» Kills|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» Name|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» PlayerId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» Team|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team1Territory|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» team1Tickets|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team1Timeline|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team2Guild|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» team2LeaderId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team2Results|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|»» **additionalProperties**|object|false|none|none|
|» team2Territory|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» team2Tickets|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team2Timeline|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» ttl|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» winner|number|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

## Get a Crystal League match

`GET /api/gameinfo/matches/crystalleague/{matchId}`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="get-a-crystal-league-match-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|matchId|path|string|true|Identifier in the route. Format and accepted values are unverified.|

> Example responses

> default Response

```json
{
  "MatchId": "string",
  "category": "string",
  "crystalLeagueLevel": 0,
  "matchType": "string",
  "startTime": "string",
  "team1Guild": null,
  "team1LeaderId": "string",
  "team1Results": {
    "property1": {
      "Deaths": 0,
      "Fame": 0,
      "Healing": null,
      "IsMercenary": null,
      "Kills": 0,
      "Name": "string",
      "PlayerId": "string",
      "Team": "string"
    },
    "property2": {
      "Deaths": 0,
      "Fame": 0,
      "Healing": null,
      "IsMercenary": null,
      "Kills": 0,
      "Name": "string",
      "PlayerId": "string",
      "Team": "string"
    }
  },
  "team1Territory": null,
  "team1Tickets": 0,
  "team1Timeline": [],
  "team2Guild": null,
  "team2LeaderId": "string",
  "team2Results": {
    "property1": {},
    "property2": {}
  },
  "team2Territory": null,
  "team2Tickets": 0,
  "team2Timeline": [],
  "ttl": "string",
  "winner": 0
}
```

<h3 id="get-a-crystal-league-match-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="get-a-crystal-league-match-responseschema">Response Schema</h3>

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» MatchId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» category|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» crystalLeagueLevel|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» matchType|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» startTime|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team1Guild|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» team1LeaderId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team1Results|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|»» **additionalProperties**|object|false|none|none|
|»»» Deaths|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» Fame|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» Healing|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|»»» IsMercenary|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|»»» Kills|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» Name|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» PlayerId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|»»» Team|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team1Territory|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» team1Tickets|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team1Timeline|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team2Guild|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» team2LeaderId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team2Results|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|»» **additionalProperties**|object|false|none|none|
|» team2Territory|any|false|none|Optional field seen in an observed sample; server contract unverified. This sample's value was null; future values are unconstrained.|
|» team2Tickets|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» team2Timeline|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» ttl|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» winner|number|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="albion-online-community-api-reference-players">Players</h1>

## Get a player

`GET /api/gameinfo/players/{playerId}`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="get-a-player-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|playerId|path|string|true|Identifier in the route. Format and accepted values are unverified.|

> Example responses

> default Response

```json
{
  "AllianceId": "string",
  "AllianceName": "string",
  "AllianceTag": "string",
  "Avatar": "string",
  "AvatarRing": "string",
  "AverageItemPower": 0,
  "DeathFame": 0,
  "Equipment": {
    "MainHand": null,
    "OffHand": null,
    "Head": null,
    "Armor": null,
    "Shoes": null,
    "Bag": null,
    "Cape": null,
    "Mount": null,
    "Potion": null,
    "Food": null
  },
  "FameRatio": 0,
  "GuildId": "string",
  "GuildName": "string",
  "Id": "string",
  "Inventory": [],
  "KillFame": 0,
  "LifetimeStatistics": {
    "PvE": null,
    "Gathering": null,
    "Crafting": null,
    "CrystalLeague": null,
    "FishingFame": null,
    "FarmingFame": null,
    "Timestamp": null
  },
  "Name": "string"
}
```

<h3 id="get-a-player-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="get-a-player-responseschema">Response Schema</h3>

Status Code **default**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» AllianceId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» AllianceName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» AllianceTag|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Avatar|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» AvatarRing|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» AverageItemPower|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» DeathFame|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Equipment|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|»» MainHand|any|false|none|Key seen in one sample; type unverified.|
|»» OffHand|any|false|none|Key seen in one sample; type unverified.|
|»» Head|any|false|none|Key seen in one sample; type unverified.|
|»» Armor|any|false|none|Key seen in one sample; type unverified.|
|»» Shoes|any|false|none|Key seen in one sample; type unverified.|
|»» Bag|any|false|none|Key seen in one sample; type unverified.|
|»» Cape|any|false|none|Key seen in one sample; type unverified.|
|»» Mount|any|false|none|Key seen in one sample; type unverified.|
|»» Potion|any|false|none|Key seen in one sample; type unverified.|
|»» Food|any|false|none|Key seen in one sample; type unverified.|
|» FameRatio|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GuildId|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» GuildName|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Id|string|false|none|Optional field seen in an observed sample; server contract unverified.|
|» Inventory|array|false|none|Optional field seen in an observed sample; server contract unverified.|
|» KillFame|number|false|none|Optional field seen in an observed sample; server contract unverified.|
|» LifetimeStatistics|object|false|none|Optional field seen in an observed sample; server contract unverified.|
|»» PvE|any|false|none|Key seen in one sample; type unverified.|
|»» Gathering|any|false|none|Key seen in one sample; type unverified.|
|»» Crafting|any|false|none|Key seen in one sample; type unverified.|
|»» CrystalLeague|any|false|none|Key seen in one sample; type unverified.|
|»» FishingFame|any|false|none|Key seen in one sample; type unverified.|
|»» FarmingFame|any|false|none|Key seen in one sample; type unverified.|
|»» Timestamp|any|false|none|Key seen in one sample; type unverified.|
|» Name|string|false|none|Optional field seen in an observed sample; server contract unverified.|

<aside class="success">
This operation does not require authentication
</aside>

## Player statistics

`GET /api/gameinfo/players/statistics`

Observed route. Parameters and response shapes describe limited observations, not a complete server contract. Generated response examples are illustrative shape diagrams, not captured payloads.

<h3 id="player-statistics-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|allianceId|query|string|false|Observed query input; requiredness and accepted values are unverified.|
|guildId|query|string|false|Observed query input; requiredness and accepted values are unverified.|
|limit|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `11`. This is not a complete accepted set.|
|offset|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `0`. This is not a complete accepted set.|
|range|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `week`. This is not a complete accepted set.|
|region|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `Total`. This is not a complete accepted set.|
|subtype|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `All`. This is not a complete accepted set.|
|type|query|string|false|Observed query input; requiredness and accepted values are unverified. Values seen in requests or samples: `PvE`, `Gathering`, `Crafting`. This is not a complete accepted set.|

> Example responses

> default Response

```json
[
  null
]
```

<h3 id="player-statistics-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|default|Default|JSON shape observed in samples where the HTTP status was not recorded. This does not assert a particular status.|Inline|

<h3 id="player-statistics-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="albion-online-community-api-reference-search">Search</h1>

## Search players and guilds

`GET /api/gameinfo/search`

An Americas request with `q=Albion` on 2026-10-21 UTC returned ten
players and ten guilds. Each sampled `Name` contained the query text
when compared without regard to case. This does not establish result
completeness, a result limit, or case-sensitivity rules. Generated
response examples are illustrative shape diagrams, not captured payloads.

<h3 id="search-players-and-guilds-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|q|query|string|false|Observed query input; requiredness and accepted values are unverified.|

> Example responses

> 200 Response

```json
{
  "guilds": [
    {
      "Id": "string",
      "Name": "string",
      "AllianceId": "string",
      "AllianceName": "string",
      "KillFame": null,
      "DeathFame": 0
    }
  ],
  "players": [
    {
      "Id": "string",
      "Name": "string",
      "GuildId": "string",
      "GuildName": "string",
      "AllianceId": "string",
      "AllianceName": "string",
      "Avatar": "string",
      "AvatarRing": "string",
      "KillFame": 0,
      "DeathFame": 0,
      "FameRatio": 0,
      "totalKills": null,
      "gvgKills": null,
      "gvgWon": null
    }
  ]
}
```

<h3 id="search-players-and-guilds-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|JSON object observed from the Americas host on 2026-10-21 UTC. The sample does not establish a complete or stable server contract.|Inline|

<h3 id="search-players-and-guilds-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» guilds|[object]|false|none|Optional field seen in an observed sample; server contract unverified.|
|»» Id|string|false|none|Optional field observed in sampled guilds.|
|»» Name|string|false|none|Optional field observed in sampled guilds.|
|»» AllianceId|string|false|none|Optional field observed in sampled guilds.|
|»» AllianceName|string|false|none|Optional field observed in sampled guilds.|
|»» KillFame|any|false|none|Optional field observed as null in every sampled guild; other values and their types are unverified.|
|»» DeathFame|integer|false|none|Optional field observed in sampled guilds.|
|» players|[object]|false|none|Optional field seen in an observed sample; server contract unverified.|
|»» Id|string|false|none|Optional field observed in sampled players.|
|»» Name|string|false|none|Optional field observed in sampled players.|
|»» GuildId|string|false|none|Optional field observed in sampled players.|
|»» GuildName|string,null|false|none|Optional field observed as a string or null in sampled players.|
|»» AllianceId|string|false|none|Optional field observed in sampled players.|
|»» AllianceName|string,null|false|none|Optional field observed as a string or null in sampled players.|
|»» Avatar|string|false|none|Optional field observed in sampled players.|
|»» AvatarRing|string|false|none|Optional field observed in sampled players.|
|»» KillFame|integer|false|none|Optional field observed in sampled players.|
|»» DeathFame|integer|false|none|Optional field observed in sampled players.|
|»» FameRatio|number|false|none|Optional field observed in sampled players.|
|»» totalKills|any|false|none|Optional field observed as null in every sampled player; other values and their types are unverified.|
|»» gvgKills|any|false|none|Optional field observed as null in every sampled player; other values and their types are unverified.|
|»» gvgWon|any|false|none|Optional field observed as null in every sampled player; other values and their types are unverified.|

<aside class="success">
This operation does not require authentication
</aside>


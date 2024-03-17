# todolist

Base URLs:

# Authentication

# 增

## POST 添加待办事项

POST /task

> Body Parameters

```json
{
  "title": "等连也到",
  "content": "ut",
  "status": "undone",
  "add_time": "2024/2/17 23:42:24",
  "end_time": "2024/2/17 23:42:24"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» title|body|string| yes |none|
|» content|body|string| yes |none|
|» status|body|string| yes |none|
|» add_time|body|integer| yes |none|
|» end_time|body|integer| yes |none|

> Response Examples

> 成功

```json
{
  "code": 200,
  "msg": "添加成功"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

# 删

## DELETE 根据id删除

DELETE /task/{id}

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer| yes |事项id|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## DELETE 根据状态删除

DELETE /task/status

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|status|query|string| yes |none|

> Response Examples

> 成功

```json
{
  "code": 200,
  "msg": "删除成功"
}
```

> 请求有误

```json
{
  "code": 400,
  "msg": "参数错误"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|请求有误|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|

HTTP Status Code **400**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|

## DELETE 删除全部

DELETE /task/all

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

# 查

## GET 根据id查询

GET /task/{id}

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer| yes |事项id|

> Response Examples

> 成功

```json
{
  "code": 200,
  "data": {
    "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
    "content": "ut",
    "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
    "id": 1,
    "status": "undone",
    "title": "等连也到"
  },
  "msg": "success"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## GET 根据关键字查询

GET /task

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|keyword|query|string| yes |标题或内容包含的关键字|
|per_page|query|integer| no |每页数量|

> Response Examples

> 成功

```json
{
  "code": 200,
  "data": [
    [
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 1,
        "status": "undone",
        "title": "等连也到"
      },
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 2,
        "status": "undone",
        "title": "等连也到"
      }
    ],
    [
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 3,
        "status": "undone",
        "title": "等连也到"
      },
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 4,
        "status": "undone",
        "title": "等连也到"
      }
    ],
    [
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 5,
        "status": "undone",
        "title": "等连也到"
      }
    ]
  ],
  "msg": "success"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## GET 根据状态查询

GET /task/status

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|status|query|string| yes |done已完成，undone未完成|
|per_page|query|integer| yes |每页数量|

> Response Examples

> 成功

```json
{
  "code": 200,
  "data": [
    [
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 1,
        "status": "undone",
        "title": "等连也到"
      },
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 2,
        "status": "undone",
        "title": "等连也到"
      },
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 3,
        "status": "undone",
        "title": "等连也到"
      }
    ],
    [
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 4,
        "status": "undone",
        "title": "等连也到"
      },
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 5,
        "status": "undone",
        "title": "等连也到"
      }
    ]
  ],
  "msg": "success"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## GET 查询所有事项

GET /task/all

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|per_page|query|integer| no |每页数量|

> Response Examples

> 成功

```json
{
  "code": 200,
  "data": [
    [
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 1,
        "status": "undone",
        "title": "等连也到"
      },
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 2,
        "status": "undone",
        "title": "等连也到"
      }
    ],
    [
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 3,
        "status": "undone",
        "title": "等连也到"
      },
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 4,
        "status": "undone",
        "title": "等连也到"
      }
    ],
    [
      {
        "add_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "content": "ut",
        "end_time": "Sat, 17 Feb 2024 23:42:24 GMT",
        "id": 5,
        "status": "undone",
        "title": "等连也到"
      }
    ]
  ],
  "msg": "success"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

# 改

## PUT 根据id更改状态

PUT /task/{id}

根据提供的原完成状态，改变事项的状态
（已完成->未完成，未完成->已完成）

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|id|path|integer| yes |事项id|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## PUT 根据状态更新状态

PUT /task/status

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|old_status|query|string| yes |原来的状态，done已完成，undone未完成|

> Response Examples

> 成功

```json
{
  "code": 200,
  "msg": "修改成功"
}
```

> 请求有误

```json
{
  "code": 400,
  "msg": "参数错误"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|请求有误|Inline|

### Responses Data Schema

# Data Schema


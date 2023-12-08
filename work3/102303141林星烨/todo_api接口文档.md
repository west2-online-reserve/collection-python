---
title: 个人项目 v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.17"

---

# 个人项目

> v1.0.0

Base URLs:

# Authentication

# todolist

## POST 代办全变已完成

POST /update/all

> Body 请求参数

```yaml
{}

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|

> 返回示例

> 成功

```json
{
  "code": 200,
  "msg": "update all success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 一条改为已完成

POST /update/{id}

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|id|path|integer| 是 |none|

> 返回示例

> 成功

```json
{
  "code": 200,
  "msg": "update single success"
}
```

> 失败

```json
{
  "code": 404,
  "msg": "NOT FOUND"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|失败|Inline|

### 返回数据结构

## POST 已完成全变代办

POST /update2/all

> 返回示例

> 成功

```json
{
  "code": 200,
  "msg": "update all success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 一条改为代办

POST /update2/{id}

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|id|path|integer| 是 |none|

> 返回示例

> 成功

```json
{
  "code": 200,
  "msg": "update single success"
}
```

> 记录不存在

```json
{
  "code": 404,
  "msg": "NOT FOUND"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|记录不存在|Inline|

### 返回数据结构

## GET 查看所有已完成

GET /search/all/completed

> 返回示例

> 成功

```json
{
  "code": 200,
  "data": [],
  "msg": "success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## GET 查看所有代办

GET /search/all/not_completed

> 返回示例

> 成功

```json
{
  "code": 200,
  "data": [
    {
      "completed": "false",
      "created_at": "Tue, 05 Dec 2023 23:15:39 GMT",
      "deadline": "Tue, 05 Dec 2023 23:15:39 GMT",
      "id": 80,
      "title": "吃饭"
    },
    {
      "completed": "false",
      "created_at": "Tue, 05 Dec 2023 23:15:48 GMT",
      "deadline": "Tue, 05 Dec 2023 23:15:48 GMT",
      "id": 81,
      "title": "睡觉"
    }
  ],
  "msg": "success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## GET 查看所有事项

GET /search/all

> 返回示例

> 成功

```json
{
  "code": 200,
  "data": [
    {
      "completed": "false",
      "created_at": "Fri, 08 Dec 2023 16:34:15 GMT",
      "deadline": "Fri, 08 Dec 2023 16:34:15 GMT",
      "id": 84,
      "title": "吃饭"
    },
    {
      "completed": "false",
      "created_at": "Fri, 08 Dec 2023 16:34:20 GMT",
      "deadline": "Fri, 08 Dec 2023 16:34:20 GMT",
      "id": 85,
      "title": "睡觉"
    },
    {
      "completed": "false",
      "created_at": "Fri, 08 Dec 2023 16:34:31 GMT",
      "deadline": "Fri, 08 Dec 2023 16:34:31 GMT",
      "id": 86,
      "title": "不睡觉"
    },
    {
      "completed": "true",
      "created_at": "Fri, 08 Dec 2023 16:34:38 GMT",
      "deadline": "Fri, 08 Dec 2023 16:34:38 GMT",
      "id": 87,
      "title": "冲锋"
    }
  ],
  "msg": "success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## GET 用关键词查询

GET /search/by_kw/{kw}

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|kw|path|string| 是 |none|

> 返回示例

> 成功

```json
{
  "code": 200,
  "data": [
    {
      "completed": "false",
      "created_at": "Tue, 05 Dec 2023 23:15:48 GMT",
      "deadline": "Tue, 05 Dec 2023 23:15:48 GMT",
      "id": 81,
      "title": "睡觉"
    }
  ],
  "msg": "search success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## GET 用id查询事项

GET /search/by_id/{id}

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|id|path|string| 是 |none|

> 返回示例

> 成功

```json
{
  "code": 200,
  "data": [
    {
      "completed": "false",
      "created_at": "Tue, 05 Dec 2023 23:15:48 GMT",
      "deadline": "Tue, 05 Dec 2023 23:15:48 GMT",
      "id": 81,
      "title": "睡觉"
    }
  ],
  "msg": "search success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## DELETE 删除一条事项

DELETE /delete/single_completed/{id}

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|id|path|integer| 是 |none|

> 返回示例

> 成功

```json
{
  "code": 200,
  "msg": "delete single success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## DELETE 删除所有已完成事项

DELETE /delete/all_completed

> 返回示例

> 成功

```json
{
  "code": 200,
  "msg": "delete all success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## DELETE 删除所有事项

DELETE /delete/all

> 返回示例

> 成功

```json
{
  "code": 200,
  "msg": "delete all success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## DELETE 删除所有未完成事项

DELETE /delete/all_not_completed

> 返回示例

> 成功

```json
{
  "code": 200,
  "msg": "delete all not completed success"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

# 数据模型


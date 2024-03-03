---
title: ToDoList v1.0.0
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

# ToDoList

> v1.0.0

Base URLs:

* <a href="http://test-cn.your-api-server.com">测试环境: http://test-cn.your-api-server.com</a>

# Authentication

# Default

## GET 初始页

GET /index

> Body 请求参数

```
string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|string| 否 |none|

> 返回示例

> 成功

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 创建待办

POST /create

> Body 请求参数

```json
{
  "title": "寒假作业",
  "content": "写100张数学试卷",
  "deadline": "2023-12-9 10:10:10"
}
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
  "msg": "添加待办成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|

## POST 查看待办

POST /look

> Body 请求参数

```json
{
  "page": 1
}
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
  "data": [
    {
      "content": "酷酷酷",
      "create_time": "2023-12-07 13:20:41",
      "deadline": "Sat, 09 Dec 2023 10:10:10 GMT",
      "id": 6,
      "state": "待办",
      "title": "寒假作业"
    }
  ],
  "msg": "查询成功"
}
```

```json
{
  "code": 200,
  "data": [
    {
      "content": "酷酷酷",
      "create_time": "2023-12-07 13:20:41",
      "deadline": "Sat, 09 Dec 2023 10:10:10 GMT",
      "id": 6,
      "state": "待办",
      "title": "寒假作业"
    },
    {
      "content": "888",
      "create_time": "2023-12-07 13:37:29",
      "deadline": "Sat, 09 Dec 2023 10:10:10 GMT",
      "id": 7,
      "state": "待办",
      "title": "寒假作业"
    }
  ],
  "msg": "查询成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» data|[object]|true|none||none|
|»» content|string|true|none||none|
|»» create_time|string|true|none||none|
|»» id|integer|true|none||none|
|»» title|string|true|none||none|
|» msg|string|true|none||none|

## DELETE 删除代办

DELETE /drop

> Body 请求参数

```json
{
  "id": 1
}
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
  "msg": "删除成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|

## PUT 修改状态

PUT /update

> Body 请求参数

```json
{
  "id": 2,
  "state": "待办"
}
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
  "msg": "更改成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|

## PUT 更新多个状态

PUT /updateall

> Body 请求参数

```json
{
  "state": "已完成"
}
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
  "msg": "更改全部成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|

## DELETE 删除所有待办/已完成

DELETE /dropsome

> Body 请求参数

```json
{
  "state": "已完成"
}
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
  "msg": "删除成功"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» code|integer|true|none||none|
|» msg|string|true|none||none|

# 数据模型


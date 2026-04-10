# API接口参考模板

## API目录结构

### 常见目录结构
```
api/ 或 services/
├── user.ts           # 用户相关API
├── order.ts          # 订单相关API
├── product.ts        # 商品相关API
├── common.ts         # 通用API
└── index.ts          # API导出
```

### API服务封装模式

```typescript
// 基础封装
import request from './request'

// GET请求
export const getUserList = (params: UserQuery) => {
  return request.get('/api/users', { params })
}

// POST请求
export const createUser = (data: UserForm) => {
  return request.post('/api/users', data)
}

// PUT请求
export const updateUser = (id: string, data: UserForm) => {
  return request.put(`/api/users/${id}`, data)
}

// DELETE请求
export const deleteUser = (id: string) => {
  return request.delete(`/api/users/${id}`)
}
```

## API接口文档模板

### 接口信息表

| 接口名称 | 请求方式 | 请求路径 | 功能描述 |
|----------|----------|----------|----------|
| 获取用户列表 | GET | /api/users | 分页查询用户列表 |
| 获取用户详情 | GET | /api/users/:id | 获取单个用户信息 |
| 创建用户 | POST | /api/users | 新增用户 |
| 更新用户 | PUT | /api/users/:id | 修改用户信息 |
| 删除用户 | DELETE | /api/users/:id | 删除用户 |

### 详细接口文档

#### 获取用户列表

**请求信息**
- 方法: GET
- 路径: /api/users
- 参数: Query

**请求参数**
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| page | number | 否 | 页码，默认1 |
| pageSize | number | 否 | 每页条数，默认10 |
| keyword | string | 否 | 搜索关键词 |
| status | string | 否 | 用户状态 |

**响应参数**
```json
{
  "code": 200,
  "data": {
    "total": 100,
    "list": [
      {
        "id": "1",
        "name": "张三",
        "email": "zhangsan@example.com",
        "status": "active",
        "createTime": "2024-01-01"
      }
    ]
  },
  "message": "success"
}
```

## 常用HTTP状态码

| 状态码 | 含义 | 说明 |
|--------|------|------|
| 200 | 成功 | 请求成功 |
| 201 | 创建成功 | 资源创建成功 |
| 400 | 请求错误 | 参数错误 |
| 401 | 未授权 | 需要登录 |
| 403 | 禁止访问 | 权限不足 |
| 404 | 未找到 | 资源不存在 |
| 500 | 服务器错误 | 后端异常 |

## 错误处理模式

### 前端错误处理

```typescript
// 统一错误处理
try {
  const res = await getUserList(params)
  if (res.code === 200) {
    // 处理成功
    setUserList(res.data.list)
  } else {
    // 处理业务错误
    message.error(res.message)
  }
} catch (error) {
  // 处理网络错误
  message.error('网络请求失败')
}
```

## API与业务功能对应

| 功能点 | API端点 | 请求方式 | 说明 |
|--------|---------|----------|------|
| 查询用户 | /api/users | GET | 分页、筛选 |
| 新增用户 | /api/users | POST | 表单提交 |
| 编辑用户 | /api/users/:id | PUT | 表单提交 |
| 删除用户 | /api/users/:id | DELETE | 单条删除 |
| 批量删除 | /api/users/batch | DELETE | 批量删除 |
| 导出用户 | /api/users/export | GET | Excel导出 |

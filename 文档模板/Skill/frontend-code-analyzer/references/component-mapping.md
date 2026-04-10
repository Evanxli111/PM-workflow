# 组件与功能映射参考

## 前端框架目录结构

### React项目结构
```
src/
├── components/          # 通用组件
│   ├── Basic/          # 基础组件
│   ├── Form/           # 表单组件
│   ├── Display/        # 展示组件
│   └── Navigation/     # 导航组件
├── pages/              # 页面组件
│   ├── Home/
│   ├── User/
│   └── Order/
├── layouts/            # 布局组件
├── hooks/              # 自定义Hooks
├── services/           # API服务
├── stores/             # 状态管理
├── utils/              # 工具函数
├── types/              # 类型定义
└── constants/          # 常量定义
```

### Vue项目结构
```
src/
├── components/         # 组件
├── views/              # 页面视图
├── router/             # 路由配置
├── store/              # 状态管理
├── api/                # API接口
├── utils/              # 工具函数
├── types/              # 类型定义
└── constants/          # 常量定义
```

## 页面与路由映射

### React Router示例
```javascript
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/user" element={<UserList />} />
  <Route path="/user/:id" element={<UserDetail />} />
  <Route path="/order" element={<OrderList />} />
  <Route path="/order/:id" element={<OrderDetail />} />
</Routes>
```

### Vue Router示例
```javascript
routes: [
  { path: '/', name: 'Home', component: Home },
  { path: '/user', name: 'UserList', component: UserList },
  { path: '/user/:id', name: 'UserDetail', component: UserDetail },
]
```

## 组件映射表模板

| 页面名称 | 路由路径 | 主组件 | 子组件 | 功能描述 |
|----------|----------|--------|--------|----------|
| 用户列表 | /user | UserList | UserTable, UserSearch, UserModal | 用户CRUD |
| 用户详情 | /user/:id | UserDetail | UserInfo, UserForm | 用户信息管理 |
| 订单列表 | /order | OrderList | OrderTable, OrderFilter | 订单查询 |

## 业务模块识别

### 模块命名规范
- 使用功能命名，避免技术命名
- 模块名称应简洁明了
- 相关功能归类到同一模块

### 模块划分原则
1. **按业务域划分**：用户模块、订单模块、商品模块
2. **按操作划分**：列表页、详情页、表单页
3. **按权限划分**：管理端、用户端

### 模块依赖关系
```
基础模块（公共组件、工具函数）
    ↓
数据模块（API服务、数据模型）
    ↓
业务模块（具体业务功能）
    ↓
页面模块（页面组件）
```

## 组件业务含义标注

在分析组件时，应标注以下信息：

| 标注项 | 说明 | 示例 |
|--------|------|------|
| 组件名称 | 组件的语义化名称 | UserTable |
| 组件类型 | 基础组件/业务组件 | 业务组件 |
| 所属页面 | 组件所在的页面 | 用户列表页 |
| 业务含义 | 组件在业务中的作用 | 展示用户数据列表 |
| 交互行为 | 组件的用户交互 | 点击行进入详情 |
| 数据来源 | 组件使用的数据 | API: /api/users |

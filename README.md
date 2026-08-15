# LangChain & LangGraph 学习笔记

> 持续更新中 — 基于 LangChain v1.2 和 LangGraph 的 AI Agent 开发学习项目

## 📖 项目简介

本项目是 LangChain 和 LangGraph 的系统性学习记录，涵盖从基础模型调用到 RAG 知识库、从单 Agent 到多节点图编排的完整链路。所有示例使用阿里云 DashScope（通义千问）系列模型。

## 🗂️ 目录结构

```
.
├── common.py                  # 通用工具函数（模型初始化、Embedding、PostgreSQL）
├── knowledge.txt              # RAG 案例客服知识库
├── langchain_v1.2/            # LangChain v1.2 学习笔记
│   ├── chapter02_model/       # 模型初始化与调用（在线/Ollama、同步/异步）
│   ├── chapter03-langsmith/   # LangSmith 追踪与调试
│   ├── chapter04_messages_template/  # 消息模板与 Prompt 构建
│   ├── chapter05-tools/       # 工具调用
│   ├── chapter06_structured_output/  # 结构化输出（四种模式）
│   ├── chapter07-Agents/      # Agent 构建
│   ├── chapter08-Middleware/   # 中间件（HumanInTheLoop、PII、TodoList、自定义 Hook）
│   ├── chapter09-memory/      # 记忆管理（短期/长期记忆、记忆治理）
│   ├── chapter10-RAG/         # RAG 全流程（加载→切分→嵌入→Milvus→客服案例）
│   └── docs/                  # 问题汇总与 TODO
├── langgraph/                 # LangGraph 学习笔记
│   ├── src/                   # 核心知识点 Notebook
│   └── hitl_demo/             # Human-in-the-Loop 实战 Demo
└── postgresql/                # PostgreSQL 相关
```

## 🚀 LangChain 章节

| 章节 | 主题 | 关键内容 |
|------|------|----------|
| Chapter 02 | 模型初始化与调用 | 在线模型、Ollama 本地模型、同步/异步调用 |
| Chapter 03 | LangSmith | 链路追踪、调试与监控 |
| Chapter 04 | 消息与模板 | Content Blocks、ChatPromptTemplate、MessagesPlaceholder |
| Chapter 05 | 工具调用 | Tool 定义与绑定 |
| Chapter 06 | 结构化输出 | 四种模式的验证与使用 |
| Chapter 07 | Agent | ReAct Agent 构建 |
| Chapter 08 | 中间件 | HumanInTheLoop、PII 脱敏、TodoList、自定义 Node/Wrap Hook |
| Chapter 09 | 记忆管理 | 短期记忆、长期记忆、记忆治理策略 |
| Chapter 10 | RAG | 文档加载→切分→Embedding→Milvus 向量库→客服知识库案例 |

## 🔷 LangGraph 章节

| 编号 | 主题 | 关键内容 |
|------|------|----------|
| 01 | 图的构建与运行 | StateGraph 基础 |
| 02 | State Reducer | 状态归并与更新策略 |
| 03 | 节点并行 | 并行执行节点 |
| 04 | Multi State | 多状态管理 |
| 05 | 内置预定义状态 | 预定义 State 类型 |
| 06 | 控制流 | 条件分支与循环 |
| 07 | ReAct 实现 | 基于 LangGraph 的 ReAct 模式 |
| 08 | 缓存与容错 | 节点级缓存与错误处理 |
| 09 | 检查点存储 | Checkpoint 机制 |
| 10 | 记忆检查点用途 | 持久化记忆场景 |
| 11 | 检查点回溯 | 状态回溯与恢复 |
| 12 | Store 存储 | 长期 KV 存储 |
| 13 | 运行时上下文 | Runtime 配置注入 |
| 14 | Checkpoint vs Store vs Runtime | 三者区别对比 |
| 15 | Node 总结 | 节点类型与最佳实践 |
| 16 | 检查点相关表 | 存储结构解析 |
| 17 | 动态中断与恢复 | HITL 动态断点 |
| 18 | 中断的检查点分析 | 中断状态深入分析 |
| 19 | 静态断点 | 静态中断点设置 |
| 20 | 工具调用与 ToolRuntime | 工具集成与运行时 |
| 21 | 流式输出 | Streaming 实现 |
| 22 | astream_events | 事件流 API |
| 23 | 子图 | Subgraph 构建 |
| 24 | 子图持久化策略 | 子图状态持久化 |
| 25 | 子图流式运行 | 子图 Streaming |
| 26 | 子图动态路由 | 子图路由分发 |
| 27 | 运行图设计模式 | Graph 运行最佳实践 |

## ⚙️ 环境配置

### 1. 安装依赖

```bash
pip install langchain langchain-core langchain-community langgraph
pip install dashscope          # 如直接使用 DashScope SDK
pip install rich               # 美化输出
```

### 2. 配置环境变量

在项目根目录创建 `.env` 文件：

```env
DASHSCOPE_API_KEY=your_api_key
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
POSTGRES_DB_URL=postgresql://user:password@localhost:5432/dbname
```

### 3. 快速使用

```python
from common import init_simple_dashscope_model

model = init_simple_dashscope_model(model='qwen-max')
resp = model.invoke("你好，请介绍一下你自己")
print(resp.content)
```

## 📝 问题记录

学习过程中遇到的问题与思考，详见 [issues_and_todo.ipynb](langchain_v1.2/docs/issues_and_todo.ipynb)，包括：

- LangSmith 原理与本地部署方案（LangFuse 替代）
- LangChain 管道命令（`|` 运算符）原理
- DashScope 专属域名的优势
- 模型选型与性能评测方法
- Qwen Embedding 模型兼容性问题与解决方案

## 📌 TODO

- [ ] astream 并发示例完善
- [ ] content_blocks 源码分析
- [ ] Pydantic 基础回顾
- [ ] 文档分片策略分析方法

---

**模型**: 通义千问（qwen-max / qwen3.7-plus）via DashScope
**框架**: LangChain v1.2 + LangGraph

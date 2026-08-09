# LangGraph

## 环境初始化
- `conda create -n langgraph python=3.13`
- `conda activate langgraph`

## LangChain和LangGraph的定位与关系
- LangChain是一个高层Agent应用框架，LangGraph更底层，LangChain底层依赖LangGraph
- LangChain提供更易用的Agent高层抽象，而LangGraph则提供可靠、持久化、更精细控制的底层执行能力

## 图三要素
- State: 运行时的共享数据结构，某一时刻的状态快照。 
- Node: 具体执行单元，通常实现为一个函数，输入为State，局部修改State。
- Edge: 定义节点之间的流转关系。决定下一个节点执行完成后决定下一步进入哪个节点。可以是固定流转，也可以根据当前State进行条件判断，循环控制，分支等复杂流程控制。

## 图运行过程
LangGraph运行过程基于Superstep组织和推进。
每次Superstep包含以下三个阶段：
- Planning/Routing阶段：根据State和Edge,确定应当进入哪个Node
- Execution阶段：运行Node。如果有多个Node，并行。在这个阶段每个Node对State的局部更新互相隔离
- Update/Commit阶段：本轮所有Node节点执行完毕，LangGraph将Node的输出统一合并到State中，生成新的状态快照。
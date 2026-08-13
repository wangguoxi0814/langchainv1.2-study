# PostgreSQL


### JSONB操作
#### 取值
    - metadata -> 'step'        -- 按 key 取，返回 jsonb
    - metadata ->> 'step'       -- 按 key 取，返回 text
    - metadata #> '{a,b}'       -- 按路径取，返回 jsonb
    - metadata #>> '{a,b}'      -- 按路径取，返回 text

#### 判断
    - metadata ? 'step'                    -- key 是否存在
    - metadata ?| array['step', 'source']  -- 任一 key 是否存在
    - metadata ?& array['step', 'source']  -- 所有 key 是否存在
#### 包含
  - metadata @> '{"step": 2}'  -- 是否包含指定 jsonb

#### 函数
- jsonb_array_length()

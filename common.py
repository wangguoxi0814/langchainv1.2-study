from typing import Any


def init_simple_qwen_max():
    """
    获取qwen-max模型
    :return:
    """
    from langchain.chat_models import init_chat_model
    from dotenv import load_dotenv
    import os
    from pathlib import Path

    # 从.env文件中加载环境变量
    load_dotenv(Path('../.env'), override=True)
    DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
    DASHSCOPE_BASE_URL = os.getenv("DASHSCOPE_BASE_URL")

    model = init_chat_model(
        model='qwen-max',
        model_provider='openai',
        api_key=DASHSCOPE_API_KEY,
        base_url=DASHSCOPE_BASE_URL,
    )

    return model


def init_simple_dashscope_model(model, profile: dict[str, Any] = None, extra_body: dict[str, Any] = None):
    """
    获取DASHSCOPE模型

    Args:
        model: qwen-max or qwen3.7-plus
        profile:
        extra_body:

    Returns:

    """
    from langchain.chat_models import init_chat_model
    from dotenv import load_dotenv
    import os
    from pathlib import Path

    # 从.env文件中加载环境变量
    load_dotenv(Path(__file__).parent / '.env', override=True)
    DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
    DASHSCOPE_BASE_URL = os.getenv("DASHSCOPE_BASE_URL")

    model = init_chat_model(
        model=model,
        model_provider='openai',
        api_key=DASHSCOPE_API_KEY,
        base_url=DASHSCOPE_BASE_URL,
        profile=profile,
        extra_body=extra_body
    )

    return model

def init_dashscope_embedding_model(model_name: str = 'qwen3.7-text-embedding', model_provider:str = 'openai'):

    from langchain.embeddings import init_embeddings
    import os
    from pathlib import Path
    from dotenv import load_dotenv

    # 从.env文件中加载环境变量
    load_dotenv(Path('../.env'), override=True)
    DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
    DASHSCOPE_BASE_URL = os.getenv("DASHSCOPE_BASE_URL")

    embedding_model = init_embeddings(
        model=model_name,
        provider=model_provider,
        api_key=DASHSCOPE_API_KEY,
        base_url=DASHSCOPE_BASE_URL,
        check_embedding_ctx_length=False,  # 关键：直接传原文 str
    )
    return embedding_model

def load_postgresql_url():
    import os
    from pathlib import Path
    from dotenv import load_dotenv

    load_dotenv(Path('../.env'), override=True)

    postgres_db_url = os.getenv("POSTGRES_DB_URL")
    return postgres_db_url
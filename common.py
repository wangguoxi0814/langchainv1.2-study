
def init_simple_qwen_max(**kwargs):
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

import openai
import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']

'''
chat = ChatOpenAI(
        cache=None,
        verbose=False,
        callbacks=None,
        callback_manager=None,
        tags=None,
        metadata=None,
        client=<class 'openai.api_resources.chat_completion.ChatCompletion'>,
        model_name='gpt-3.5-turbo',
        temperature=0.0,
        model_kwargs={},
        openai_api_key='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',
        openai_api_base='',
        openai_organization='',
        openai_proxy='',
        request_timeout=None,
        max_retries=6,
        streaming=False,
        n=1,
        max_tokens=None,
        tiktoken_model_name=None
        )
'''

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""
prompt_template = ChatPromptTemplate.from_template(template_string)

test1 = prompt_template.messages[0].prompt
test2 = prompt_template.messages[0].prompt.input_variables
print(test1+'\n')
print(test2)

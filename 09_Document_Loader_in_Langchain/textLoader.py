from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
  template= "Write a summary in 2 lines for the following {paragraph}",
  input_variables=['paragraph']
)

loader = TextLoader('./files/cricket.txt', encoding='utf-8')


text_docs = loader.load()

chain = prompt | model | parser

res = chain.invoke({'paragraph': text_docs[0].page_content})

print(res)
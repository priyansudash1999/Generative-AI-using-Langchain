from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()
# 1st Prompt
temp1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd Prompt
temp2 = PromptTemplate(
    template="Write a 5 line summary of the following text using bullet points:\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = temp1 | model | parser | temp2 | model | parser

result = chain.invoke({'topic': 'blackhole'})

print(result)


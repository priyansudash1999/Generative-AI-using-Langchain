from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt = PromptTemplate(
  template= "Write a joke about this {topic}",
  input_variables= ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser)

chain2 = prompt | model | parser

res = chain.invoke({'topic': "AI"})

result = chain2.invoke({'topic': "AI"})

print(res)

print(result)
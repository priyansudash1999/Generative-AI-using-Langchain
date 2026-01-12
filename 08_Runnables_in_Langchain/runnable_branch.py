from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
  template= "Write a detailed report on the {topic}",
  input_variables=["topic"]
)

prompt2 = PromptTemplate(
  template = "Summarize the following text \n {text}",
  input_variables=["text"]
)

report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
  (lambda x: len(x.split()) > 500, prompt2 | model | parser),
  RunnablePassthrough()
)

final_chain = report_gen_chain | branch_chain

res = final_chain.invoke({'topic': "India vs China"})

print(res)
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

passthrough = RunnablePassthrough()

prompt1 = PromptTemplate(
  template= "Write a joke about {topic}",
  input_variables= ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
  template= "Explain the following joke - {text}",
  input_variables= ['text']
)

joke_generator_chain = prompt1 | model | parser

parallel_chain = RunnableParallel(
  {
    "joke": RunnablePassthrough(),
    "explanation": prompt2 | model | parser
   }
)

final_chain = joke_generator_chain | parallel_chain

res = final_chain.invoke({
  "topic": "cricket"
})

print(res)
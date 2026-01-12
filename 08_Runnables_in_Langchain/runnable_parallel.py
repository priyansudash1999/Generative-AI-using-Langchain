from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

prompt_for_x = PromptTemplate(
  template= "Generate a tweet about {topic}",
  input_variables= ['topic']
)


prompt_for_linkedin = PromptTemplate(
  template= "Generate a post about {topic}",
  input_variables= ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

# parallel_chain = RunnableParallel({
#   "tweet": RunnableSequence(prompt_for_x, model, parser),
#   "linkedin": RunnableSequence(prompt_for_linkedin, model, parser)
# })

parallel_chain = RunnableParallel({
  "tweet": prompt_for_x | model | parser,
  "linkedin": prompt_for_linkedin | model | parser
})

res = parallel_chain.invoke({'topic': "AI"})

print(res)
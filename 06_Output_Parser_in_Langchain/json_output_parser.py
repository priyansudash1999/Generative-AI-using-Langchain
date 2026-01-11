from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
  repo_id= "google/gemma-2-2b-it",
  task= "text-generation"
)

model = ChatHuggingFace(llm = llm)

parser = JsonOutputParser()

# Prompt templates

template = PromptTemplate(
  template= "Give me the age, city, natioanal, job of Sundar Pichai \n {format_instruction}",
  input_variables= [],
  partial_variables= {"format_instruction": parser.get_format_instructions()}
)

# prompt = template.format()

# res = model.invoke(prompt)

# final_res = parser.parse(res.content)


# print(final_res)
# print(type(final_res))

chain = template | model | parser

result = chain.invoke(input={})
print(result)

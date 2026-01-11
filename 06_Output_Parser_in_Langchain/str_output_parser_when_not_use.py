from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()
# 1st Prompt
temp1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt1 = temp1.invoke({"topic": "black hole"})
res1 = model.invoke(prompt1)

# 2nd Prompt
temp2 = PromptTemplate(
    template="Write a 5 line summary of the following text using bullet points:\n{text}",
    input_variables=["text"]
)

prompt2 = temp2.invoke({"text": res1})
res2 = model.invoke(prompt2)

print(res2.content)

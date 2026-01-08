from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4.1-nano", temperature=0)


class Review(TypedDict):
  summary: str
  sentiment: str

str_model = model.with_structured_output(Review)
result = str_model.invoke(""" The hardware is great of the phone but the software lacks sometimes and all remaining are worse.""")

print(result)
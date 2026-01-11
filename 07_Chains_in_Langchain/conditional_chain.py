from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
  sentiment: Literal["positive", "negative", "neutral"] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
  template= "Classify the sentiment of the following text into positive, negative or neutral. \n {feedback} \n {format_instruction}",
  input_variables=["feedback"],
  partial_variables= {'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# res = classifier_chain.invoke({"feedback": "This is not good"})
# print(res)

# 2nd part --> Branching

prompt2 = PromptTemplate(
  template = "Write an approprite response to this positive feedback \n {feedback}",
  input_variables=['feedback']
)
prompt3 = PromptTemplate(
  template = "Write an approprite response to this Negative feedback \n {feedback}",
  input_variables=['feedback']
)
prompt4 = PromptTemplate(
  template = "Write an approprite response to this Neutral feedback \n {feedback}",
  input_variables=['feedback']
)

branch_chain = RunnableBranch(
  (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
  (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
  (lambda x:x.sentiment == 'neutral', prompt4 | model | parser),
  RunnableLambda(lambda x: "Could not find any sentiment...")
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback": """he Samsung Galaxy S24 Ultra is an impressive flagship device with a stunning display and powerful performance. Its Dynamic AMOLED screen offers vibrant colors and sharp detail, making videos and gaming visually immersive. The camera system, especially the 200MP main sensor and advanced zoom capabilities, captures high-quality photos even in low light. Battery life comfortably lasts a full day with moderate to heavy use, and the build quality feels premium with a solid and ergonomic design.On the downside, the S24 Ultra comes with a high price tag that may deter budget-conscious buyers, and some users may find the phone a bit large and heavy for one-handed use. While the software experience is generally smooth, occasional bloatware and persistent pre-installed apps can feel unnecessary. Additionally, fast charging speeds are good but not class-leading compared to some competitors. Overall, the S24 Ultra delivers cutting-edge features, but the cost and size may not be ideal for everyone. """})

print(result)
from typing import TypedDict, Annotated, Optional
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4.1-nano", temperature=0)


# class Review(TypedDict):
#   summary: str
#   sentiment: str

class Review(TypedDict):
  key_themes: Annotated[str, "Write down all the key themes discussed in the review of the list"]
  summary: Annotated[str, "A brief summary of the review"]
  sentiment: Annotated[str, "The sentiment of the review either positive or negative or neutral"]
  pros: Annotated[Optional[list[str]], "Write down all the pros inside the list"]
  cons: Annotated[Optional[list[str]], "Write down all the cons inside the list"]

str_model = model.with_structured_output(Review)
result = str_model.invoke(""" I recently used the Realme 12 Pro+, and unfortunately, my experience was disappointing. While the phone boasts attractive specs on paper, it fell short in several key areas. The software felt unstable, with frequent lags and inconsistent performance during everyday tasks. Battery life was mediocre at best, barely lasting a full day with moderate use. The camera, despite its high megapixel count, struggled in low-light conditions and produced washed-out colors. Additionally, the build quality didn’t feel as premium as expected for a device in this price range. All things considered, I expected much better, but the Realme 12 Pro+ ultimately left me underwhelmed.""")

print(result)
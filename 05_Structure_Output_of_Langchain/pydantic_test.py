from typing import TypedDict, Annotated, Optional, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()
model = ChatOpenAI(model="gpt-4.1-nano", temperature=0)


# class Review(TypedDict):
#   summary: str
#   sentiment: str

class Review(BaseModel):

  key_themes: list[str] = Field(description="Write down all the key themes discussed in the review of the list")
  summary: str = Field(description="A brief summary of the review")
  sentiment: Literal["pos", "neg"] = Field(description="The sentiment of the review either positive or negative or neutral")
  pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside the list")
  cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside the list")
  name: Optional[str] = Field(default=None, description="Write name of reviewer")
  

str_model = model.with_structured_output(Review)
result = str_model.invoke(""" I recently used the Realme 12 Pro+, and unfortunately, my experience was disappointing. While the phone boasts attractive specs on paper, it fell short in several key areas. The software felt unstable, with frequent lags and inconsistent performance during everyday tasks. Battery life was mediocre at best, barely lasting a full day with moderate use. The camera, despite its high megapixel count, struggled in low-light conditions and produced washed-out colors. Additionally, the build quality didn’t feel as premium as expected for a device in this price range. All things considered, I expected much better, but the Realme 12 Pro+ ultimately left me underwhelmed.""")

print(result)
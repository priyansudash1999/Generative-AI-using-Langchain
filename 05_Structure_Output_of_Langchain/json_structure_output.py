from typing import TypedDict, Annotated, Optional, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(model="gpt-4.1-nano", temperature=0)

# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes":{
      "type":"array",
      "items": {
        "type": "string"
      },
      "desc": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "desc": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "desc": "Return sentiment of the review either positive, negative or neutral"
    },
    "pros":{
      "type": ["array", "null"],
      "items":{
        "type": "string"
      },
      "desc": "Write down all the pros inside a list"
    },
    "cons":{
      "type":["array", "null"],
      "items":{
        "type": "string"
      },
      "desc": "Write down all the cons inside a list"
    },
    "name":{
      "type": ["string", "null"],
      "desc": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}



str_model = model.with_structured_output(json_schema)
result = str_model.invoke(""" I recently used the Realme 12 Pro+, and unfortunately, my experience was disappointing. While the phone boasts attractive specs on paper, it fell short in several key areas. The software felt unstable, with frequent lags and inconsistent performance during everyday tasks. Battery life was mediocre at best, barely lasting a full day with moderate use. The camera, despite its high megapixel count, struggled in low-light conditions and produced washed-out colors. Additionally, the build quality didn’t feel as premium as expected for a device in this price range. All things considered, I expected much better, but the Realme 12 Pro+ ultimately left me underwhelmed.  Review by Priyansu Dash""")

print(result)
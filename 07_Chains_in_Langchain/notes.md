# Chains in Langchain

- ### What ?
  - A chain lets us run multiple LLM-related operations in sequence as one workflow.
  - Auomatically 1st step output is 2nd step input and 2nd output is 3rd step input and so on...
- ### Why ?

  - Without chains:

    - We manually call the model again and again

    - We handle outputs and inputs yourself

    - Code becomes repetitive and error-prone

  - With chains:

    - Steps are connected automatically

    - Code is cleaner and reusable

    - Complex workflows become easy to manage

    `Step 1 → Step 2 → Step 3 → Final Output`

## Types of Chain

- Simple Chain
- Sequential Chain
- Parallel Chain
- Conditional Chain

### Simple Chain:-

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
  template = 'Generate 5 instructing fact about {topic}',
  input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

res = chain.invoke({'topic': "GenAI"})

print(res)
```

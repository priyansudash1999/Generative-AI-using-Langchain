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

- A Simple Chain in LangChain is the most basic pipeline where: `One prompt → One model → One output`
- There is no multiple steps, no branching—just a single flow.

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

### Sequential chain:-

- A Sequential Chain is a multi-step pipeline where:
  ```
      Output of Step-1 becomes input of Step-2,
      Output of Step-2 becomes input of Step-3, and so on.
  ```
- Use case:-
  ![seq](./assets/seq.png)

  ```python
  from langchain_openai import ChatOpenAI
  from dotenv import load_dotenv
  from langchain_core.prompts import PromptTemplate
  from langchain_core.output_parsers import StrOutputParser

  load_dotenv()

  prompt1 = PromptTemplate(
    template= 'Generate a detailed report on {topic}',
    input_variables= ['topic']
  )

  prompt2 = PromptTemplate(
    template = 'Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
  )

  model = ChatOpenAI()

  parser = StrOutputParser()

  chain = prompt1 | model | parser | prompt2 | model | parser

  res = chain.invoke({'topic': "GenAI affect on software engineering"})

  print(res)
  ```

### Parallel Chain :-

- A Parallel Chain runs multiple prompts at the same time on the same input and returns all outputs together.
  ```
            ┌── Prompt A → LLM → Output A
  Input ────┼── Prompt B → LLM → Output B
            └── Prompt C → LLM → Output C
  ```
- Use case :-
  ![parallel](./assets/par.png)

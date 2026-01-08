# Structure Output of Langchain

### Unstructured Output:-

- When we communicate with LLMs, we get unstructured output.
- Unstructured output is a list of tuples.

![unstructure_op](./assets/uns_op.png)

## Structured Output:-

- In Langchain, structure output refers to the practise of having language models return responses in a well defined data format (e.g:- JSON).
- This makes the model output easier to parse and work with programatically.

##### Example:- Prompts - Can you create a one day itinerary for Paris ?

- Here is an suggested itinerary.

  - Morning: Visit Eiffel Tower
  - Afternoon: Walk through the Louvre Museum
  - Evening: Enjoy Dinner at a Seine riverside cafe.

- JSON Enforced Output:
  - [
    {"time" : "Morning", "Activity": "Visit Eiffel Tower"},
    {"time" : "Afternoon", "Activity": "Walk through the Louvre Museum"},
    {"time" : "Evening", "Activity": "Enjoy Dinner at a Seine riverside cafe."}
    ]

> #### Why we need structure format output.

- Data Extraction
  - Example: If we are dealing with a job portal app, at there we need data in structure for extracting data.
  - From a resume we have to extract name, qualification, experience and skills
- API Building
  - If we are dealing with an e-commerce platform at there we need many API to do work.
    - If there is a review section, we need api for fetch review and get the topics, pros, cons and sentiment of the customer.
- Agents
  - If we have a calcultor tasks in any agent when the user will write find the sqrt of 16. calcultor can not understand those text. so we need an agent to communicate between user and calculator.

#### Ways to get structure outputs:-

![ways_](./assets/ways_.png)

### 1. withStructureOutput :-

![types_of_schema](./assets/types.png)

- `with_structured_output()` is a LangChain method that wraps an LLM so that its responses are forced into a predefined structured schema (TypedDict, Pydantic, or JSON), instead of free-text.
- Analody :-

  - LLMs normally return unstructured text:
    - E.g :- Sure! Here is your answer...
  - But real applications need deterministic data: - E.g :-{
    "skills": [],
    "score": 0.82
    }

    > ##### What exactly does it do? (Step-by-Step) ?
    >
    > Internally, it:

        Step 1 : Takes a schema
          - TypedDict
          - Pydantic model
          - JSON schema

        Step 2 : Converts the schema into an OpenAI tool/function

        Step 3 : Forces the LLM to call that tool

        Step 4 : Parses the tool output

        Step 5 : (If Pydantic) validates the output

        Step 6 :Returns structured Python data

  ##### Basic Example :-

  - Without with_structured_output() ❌

    ```python
    llm.invoke("Explain LangChain")
    ```

    Output :- `LangChain is a framework...`

  - With with_structured_output() ✅

    ```python
    from pydantic import BaseModel

    class Explanation(BaseModel):
        topic: str
        summary: str

    structured_llm = llm.with_structured_output(Explanation)

    result = structured_llm.invoke("Explain LangChain")

    ```

    Output :-

    ```
      Explanation(
      topic="LangChain",
      summary="A framework for building LLM applications"
      )
    ```

  ##### Types of Schema in with_structure_output function.

  - There are 3 types of schema or input in with_structure_output function.
    - typedDict
    - pydantic
    - JSON

  #### 1. typedDict :-

  - TypedDict is a clean and Python-native way to get structured output in LangChain, especially if us don’t want full Pydantic models.
  - TypedDict (from typing) lets us define the expected structure of a dictionary with type hints.

    - ✅ Lightweight
    - ✅ No validation overhead
    - ⚠️ Less strict than Pydantic

    ```python
    from typing import TypedDict, List
    from langchain_openai import ChatOpenAI

    class CoursePlan(TypedDict):
        title: str
        duration_weeks: int
        topics: List[str]
        level: str

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    structured_llm = llm.with_structured_output(CoursePlan)

    res = structured_llm.invoke("Create a GenAI course plan")
    print(res)
    ```

    Output:-

    ```
    {
    'title': 'GenAI Engineer Roadmap',
    'duration_weeks': 12,
    'topics': ['LLMs', 'Prompting', 'RAG', 'Agents'],
    'level': 'Intermediate'
    }
    ```

    - Output is guaranteed dictionary
    - Keys are fixed
    - Works perfectly with FastAPI / Streamlit

  > HR tip:
  > Say this in interview:
  > “I use TypedDict for lightweight deterministic outputs and Pydantic when validation and API safety are required.”

  ##### When Should You Use TypedDict?

  - You want simple structured output
  - You care about speed
  - You don’t need validation
  - Internal tools, PoCs

  ##### ❌ Avoid when:

  - Public APIs
  - User-generated inputs
  - Financial / healthcare apps

  ##### Types of TypedDict :-

  - There are four types of typedDict.

    - simple
    - annotated
    - literal
    -

    ###### (i) simple typedDict :-

    - Using basic Python types directly.

    ```python
    from typing import TypedDict
    from langchain_openai import ChatOpenAI
    from dotenv import load_dotenv

    load_dotenv()
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0)


    class Review(TypedDict):
      summary: str
      sentiment: str

    str_model = model.with_structure_output(Review)
    result = str_model.invoke(""" The hardware is great of the phone but the software lacks sometimes and all remaining are worse.""")

    print(result)
    ```

    - Characteristics
      - No constraints
      - No metadata
      - Most common
      - Fast
    - When to use
      - Internal tools
      - Quick PoCs
      - When precision is not critical

    ###### (ii) Annotated typedDict :-

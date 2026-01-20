# Tools in Langchain

## What is Tools ?

- A tool is just a python function or API that is wrapped in a way the LLM can understand and call when needed.
- Example:-
  - LLM like GPT are great at :-
    - Reasoning
    - Language generation
  - LLM can not do things like :-
    - Access live data (weather, data)
    - Do reliable math (complex math problems)
    - Call APIs
    - Run code
    - Interact with database

    > LLM can do all these using tools

  - Example:- We can make a function which can get IRCTC website to book tickets.

## Types of Tools:-

- Basically there are two types of tools in langchain.
  ![types](./assets/tpes.png)

### How tools fits into the Agent Ecosystem

- An AI agent is an LLM powered system that can autonomously think, decide and take actions using external tools or API to achieve a goal.
  ![agent](./assets/agent.png)
- For building agent both LLM and Tools are very important.

### Built-in tools :-

- Langchain identified some tools are common used like googling
- A built in tool is a tool that langchain already provides for us - it's pre-built, production ready and requires minimal or no setup.
- We don't have to write the function logic by ourself - we just import and use it.
- Popular built in tools
  | **Tools** | **Work** |
  | -------------------- | ------------------------- |
  | DuckDuckGoSearchRun | Web search via DuckDuckGo |
  | WikipediaQueryRun | Wikipedia summary |
  | PythonEPLTool | Run raw Python Code |
  | ShellTool | Run Shell commands |
  | RequestGetTool | Make HTTP GET requests |
  | GmailSendMessageTool | Send emails via gmail |
  | SlackSendMessageTool | Post message to slack |
  | SQLDatabaseQueryTool | Run SQL queries |
  > visit https://colab.research.google.com/drive/1bNBUKQRlIm8OLanAXnfHWm3SBuLCC8Nd#scrollTo=h5D0K7jcLwkx
- There are so many paid and free tools in langchain.

### Custom Tools :-

- When there are no built-in tools for our usecase.
- Example:-
  - We want to call our own APIs.
  - We want to encapsulate buisness logic.
  - We want the LLM to interact with our database, product and app.

### Ways to create custom tools

> visit https://colab.research.google.com/drive/1bNBUKQRlIm8OLanAXnfHWm3SBuLCC8Nd#scrollTo=PZ5XPKhJRp6o

![ways](./assets/ways.png)

#### Using StructuredTool and Pydantic :-

- A StructuredTool in langchain is a special type of tool where the input to the tool follows a structured schema, typically defined using a Pydantic model.

#### Using BaseTool Class :-

- BaseTool is a abstract base class for all tools in Langchain.
- It defines the core structure and interface that any tool must follow, wheather it's a simple one-liner or a fully customized function.
- All other tool like `@tool`, `StructuredTool` are built on top of BaseTool

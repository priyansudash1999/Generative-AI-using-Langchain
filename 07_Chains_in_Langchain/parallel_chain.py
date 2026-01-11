from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()


model1 = ChatOpenAI()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",   # HF internally handles chat
    max_new_tokens=300,
    temperature=0.7
)


model2 = ChatHuggingFace(llm=llm)
prompt1 = PromptTemplate(
  template="Generate short and simple notes from the following text \n {text}",
  input_variables=["text"]
)

prompt2 = PromptTemplate(
  template="Generate 5 short question answers from the following text \n {text}",
  input_variables=["text"]
)

prompt3 = PromptTemplate(
  template="Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quizs}",
  input_variables= ["notes", "quizs"]
)

parser = StrOutputParser()

# Parallel chain

parallel_chain = RunnableParallel({
  "notes": prompt1 | model1 | parser,
  "quizs": prompt2 | model2 | parser
})

# merge both
merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
  Artificial Intelligence (AI) is a field of computer science that focuses on building systems capable of performing tasks that normally require human intelligence. These tasks include learning from data, understanding natural language, recognizing patterns, and making decisions. AI systems are commonly classified into narrow AI, which is designed to perform a specific task, and general AI, which aims to perform any intellectual task a human can do. Modern AI heavily relies on machine learning techniques, especially deep learning, which uses neural networks with multiple layers to process large amounts of data. AI is widely used in real-world applications such as healthcare, finance, education, transportation, and virtual assistants, helping improve efficiency, accuracy, and automation.
"""

result = chain.invoke({"text": text})

print(result)
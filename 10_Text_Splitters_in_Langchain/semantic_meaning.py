from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
  OpenAIEmbeddings(),
  breakpoint_threshold_type="standard_deviation",
  breakpoint_threshold_amount=1
)

sample = """
  Farmers in India are working hard in the fields, preparing the soil and planting seeds for the next season. IPL is a cricket tournament of India where 10 teams play with each other
"""

docs = text_splitter.create_documents([sample])

print(docs)

print(len(docs))
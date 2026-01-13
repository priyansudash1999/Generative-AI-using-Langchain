from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader('./files/genai_roadmap_google.pdf')

docs_pypdf = loader.load()

print(docs_pypdf)
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('./files/genai_roadmap_google.pdf')

docs_pypdf = loader.load()


splitter = CharacterTextSplitter(
  chunk_size = 100,
  chunk_overlap = 0,
  separator = ''
)

res = splitter.split_documents(docs_pypdf)

print(res[0])
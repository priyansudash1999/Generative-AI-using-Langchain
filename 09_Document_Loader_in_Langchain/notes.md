# Document Loaders in Langchain

- Document loaders are component in Langchain used to load data from various sources into a standardized format(usually as document objects), which can then be used for chunking.
- Document loaders is one of the component of RAG.
  ![document_loaders](./assets/rag_comp.png)
- In langchain there are more than 100 document loaders.
- Main document(the most use) loaders are:-

  - TextLoader
  - PyPDFLoader
  - WebBaseLoader
  - CSVLoader

- Syntax :-
  ```python
  Document(
    page_content = "The actual text content",
    metadata = {"source": "filename.pdf", ...}
  )
  ```

## TextLoader :-

- TextLoader is a simple and commonly used document loader in langchain that reads plain text(`.txt`) files and converts them into Langchain Document objects.
- **Use Cases**:-

  - Ideal for loading chat logs, scraped text, transcripts, code snippets or any plain text data into a langchain pipeline.

- **Limitation** :-

  - Works for only `.txt` files

  ```python
  from langchain_community.document_loaders import TextLoader

  loader = TextLoader('./files/cricket.txt', encoding='utf-8')


  text_docs = loader.load()

  print(text_docs) # Output as in a list.

  print(type(text_docs))  # list

  print(text_docs[0]) # get the document text

  print(type(text_docs[0])) # langchain_core.documents.base.Document
  ```

## PyPDFLoader :-

- The most use loader in langchain.
- PyPDFLoader is a document loader in langchain used to load content from PDF files and convert each page into a Document Object.

  ```
  [
    Document(page_content = "Text from page 1", metadata = {"page": 0, "source": "file.pdf"}),
    Document(page_content = "Text from page 2", metadata = {"page": 1, "source": "file.pdf"}),
  ]
  ```

- **Limitation** :-

  - It used the PyPDF library under the hood - notgreat with scanned pdfs or complex layouts.

  ```python
  from langchain_community.document_loaders import PyPDFLoader
  from langchain_openai import ChatOpenAI
  from langchain_core.output_parsers import StrOutputParser
  from langchain_core.prompts import PromptTemplate
  from dotenv import load_dotenv

  load_dotenv()

  loader = PyPDFLoader('./files/genai_roadmap_google.pdf')

  docs_pypdf = loader.load()

  print(docs_pypdf)
  ```

- There are some other pdf loaders which works differently.
  | Use Case | Recommended Loader |
  |----------------------------|--------------------|
  | Simple, clean PDFS | PyPDF loader |
  | PDFS with tables/columns | PDFPlumberLoader |
  | Scanned/image PDFs | UnstructuredPDFLoader or AmazonTextractPDFLoader |
  | Need Layout and image data | PyMuPDFLoader |
  | Want best structure extraction | UnstructuredPDFLoader |

## DirectoryLoader :-

- DirectoryLoader is a document loader that lets us load multiple documents from a directory and convert them into a list of Document objects.

  | Glob Pattern    | What is loads                        |
  | --------------- | ------------------------------------ |
  | "\*\*_/\*_.txt" | All `.txt` files in all subfolders   |
  | "\*.pdf"        | All .pdf files in the root directory |
  | "data/\*.csv"   | All .csv files in the data/ folder   |
  | "\*\*_/\*_"     | All files (any type, all folders)    |

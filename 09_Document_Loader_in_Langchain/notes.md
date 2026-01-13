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

  ```python
  from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


  loader = DirectoryLoader(
    path="./files/roadmap",
    glob='*.pdf',
    loader_cls= PyPDFLoader
  )

  docs = loader.load()

  print(len(docs))

  print(docs[0].page_content)

  print(docs[0].metadata)
  ```

- The process is slow, I provided 2 pdf files, it can be slow but iof there are a lot of pdf files then it will be very slow.
- So, there is a solution called lazy loading in langchain.

### load vs lazy_load

#### load() :-

- Eager loading (loading everything at once)
- Returns: A list of document objects.
- Loads all documents immediately into memory.
- Best when :-

  - The number of documents is small.
  - You want everything loaded upfront.

  ```python
  from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


  loader = DirectoryLoader(
    path="./files/roadmap",
    glob='*.pdf',
    loader_cls= PyPDFLoader
  )

  docs = loader.load()


  print(docs[0].page_content)

  print(docs[0].metadata)
  ```

#### lazy_load() :-

- Lazy loading (loads on demand)
- Returns : A generator of Document object.
- Documents are not loaded at once. They are fetched one at a time as needed.
- Best when :-

  - We are dealing with large documents or lots of files.
  - You want to stream processing (E.g :- Chunking, embedding) without using lots of memory.

  ```python
  from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

  loader = DirectoryLoader(
    path="./files/roadmap",
    glob='*.pdf',
    loader_cls= PyPDFLoader
  )

  docs = loader.lazy_load()

  for doc in docs:
    print(doc.metadata)
  ```

## WebBaseLoader :-

- WebBaseLoader is a document loader in langchain used to load and extract text content form web pages(URLs).
- It uses `BeautifulSoup` under the hood to parse HTML and extract visible text.

- **When to use** :-

  - For blogs, news articles or public websites where the content is primarily text bases and static.

- **Limitation** :-

  - Does not handle javascript heavy pages well (use SeleniumURLLoader for that).
  - Loads only static content. (what's in the HTML, not what loads after the page renders).

  ```python
  from langchain_community.document_loaders import WebBaseLoader

  url = "https://www.flipkart.com/samsung-m7-series-107-9-cm-43-inch-4k-ultra-hd-led-backlit-va-panel-in-built-speaker-smart-tv-apps-airplay-wi-fi-bluetooth-usb-type-c-wireless-display-vision-ai-monitor-ls43fm700uwxxl/p/itm3d915c6583e0d?pid=MONHDA8MQBMRZVCH&lid=LSTMONHDA8MQBMRZVCHVVK4M4&marketplace=FLIPKART&store=6bo%2Fg0i%2F9no&srno=b_1_1&otracker=browse&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&fm=organic&iid=en_QqzEeHZbPFkemVbsrBGmLIRYcpt5c6t8RkuwUxPELB8k09JkjaQQRIY_VnQeKbxPbl2CBfejXb6WZd2drrugkg%3D%3D&ppt=hp&ppn=homepage&ssid=pbynw79g1c0000001768285370507"

  loader = WebBaseLoader(url)

  docs = loader.load()

  print(docs[0].page_content)
  ```

## CSVLoader :-

- CSVLoader is a document loader used to load CSV files into Langchain Document objects one per row, by default.

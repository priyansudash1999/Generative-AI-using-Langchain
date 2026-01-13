# Text Splitting

- Text splitting is the process of breaking large chunks of text(like articles, PDFs, HTML Pages or books) into smaller, managebale pieces(chunks) that an LLM can handle effectively.

  ![chunks](./assets/chunk.png)

- **Overcoming model limitations**:-
  - Many Embedding models and language models have maximum input size constraints.
  - Splitting allows us to process documents that would otherwise exceed these limits.
- **Downstream tasks**:-
  - Text splitting improves nearly every LLM powered task.

| Task            | Why Splitting Helps                             |
| --------------- | ----------------------------------------------- |
| Embedding       | Short chunks yield more accurate vectors        |
| Semantic search | Search results point to focused info, not noise |
| Summarization   | Prevents halluciation and topic drift           |

- Optimizing computational resources :-
  - Working with smaller chunks of text can be more memroy efficient and allow for better parallelization of processing task
    ![splitter](./assets/text_spltter.png)

## 1. length-based text splitting :-

- This is simple way of splitting and very fast
  ![split](./assets/split.png)
- When we divide a paragraph into 5 different parts with 100 characters to everyone (may be last one has less characters) then we can found that some word can split. means from "read" one sentence has "re" and the next sentence starts from "ad", that will be a problematic part. so, it is not use many times

  ```python
  from langchain_text_splitters import CharacterTextSplitter
  from langchain_community.document_loaders import PyPDFLoader

  loader = PyPDFLoader('./files/genai_roadmap_google.pdf')

  docs_pypdf = loader.load()


  splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,  # chunk_overlap share contexts between chunk
    separator = ''
  )

  res = splitter.split_documents(docs_pypdf)

  print(res[0])
  ```

## 2. Text-Structured Based :-

- A text-structure-based text splitter splits text based on logical structure, not just character count or tokens.
- It recursively splits text using a list of separators, starting from the most meaningful (paragraphs) down to the least (characters).
-

```
"\n\n"  → paragraphs
"\n"    → lines
" "     → words
""      → characters (last fallback)
```

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter


splitter = RecursiveCharacterTextSplitter(
  chunk_size = 100,
  chunk_overlap = 0,
)

text = """
  Cricket is a popular outdoor sport played between two teams of eleven players each.
  It originated in England and is now widely played in countries like India, Australia, England, Pakistan, and South Africa.

"""

res = splitter.split_text(text)

print(res)
```

## 3. Document-structure Based :-

- A document-structure-based splitter divides text using the natural structure of a document (headers, sections, pages, paragraphs), not just size.
- When we have no letters means we have code files
- It is an extension of recursive text splitting.

- Separators:-

  - for .md files
    | Separator | Meaning |
    | ------------------- | --------------- |
    | `#` | Main heading |
    | `##` | Subheading |
    | `###` | Sub-subheading |
    | `---` | Section divider |
    | Blank line (`\n\n`) | Paragraph |
  - for html files
    | Tag | Purpose |
    | ------ | ---------- |
    | `<h1>` | Page title |
    | `<h2>` | Section |
    | `<h3>` | Subsection |
    | `<p>` | Paragraph |
    | `<li>` | List item |
  - for python files
    | Separator | Purpose |
    | -------------- | -------------------- |
    | `\nclass ` | Class definitions |
    | `\ndef ` | Function definitions |
    | `\nasync def ` | Async functions |

  ```python
  from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

  python_code = """
  class User:
      def login(self):
          print("Login")

      def logout(self):
          print("Logout")

  def helper_function():
      print("Helper")
  """
  splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 300,
    chunk_overlap=0
  )

  chunks = splitter.split_text(python_code)

  print(len(chunks))
  print(chunks)
  ```

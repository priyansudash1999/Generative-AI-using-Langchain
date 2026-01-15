# Retreivers in Langchain

## What is Retrievers ?

- One of the core component of RAG which fetches relevant documents from a data source in response to a user's query.
- There are multiple types of retrievers
  ![ret](./assets/ret.png)
- Data source can be a vector store or an API.
- Retriever needs user query as input and gives multiple document objects as output.

## Types of Retrievers :-

- We can divide retriever types into two categories

- There are a lot of retriever in langchain.
  - Wikipedia retriever
  - Vector Store Retriever (Most Common)
  - Similarity Retriever
  - Multi-Query Retriever
  - Contextual Compression Retriever

### Wikipedia retriever :-

- A wikipedia retriever is a retriever that queries the wikipedia API to fetch relevant content for a given query.
- ##### **How it works** ?
  - User give a query (e.g Virat Kohli).
  - The retriever sends a query to wikipedia API.
  - It retrievs the most relevant articles.
  - It returns them as Langchain `Document` objects.
    > Visit https://colab.research.google.com/drive/1ApZMyI7uAn1W-IwDVwh_ott--ojDJV-1#scrollTo=NUFVcL8_mOzp for code

### Vector Store Retriever :-

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

- A vector store retriever in Langchain is the most common type of retriever that lets us search and fetch documents from a vector store based on semantic similarity using vector embeddings.
- ##### **How it works** ? :-
  - We store our documents in a vector store (like FAISS, Chroma, Pinecone, etc).
  - Each document is converted into a dense vector using an embedding model.
  - When the user enters a query:
    - It is also turned into a vector.
    - The retriever compares the query vector with the stored vectors.
    - It retrieves the top-k most similar ones.
      > Visit https://colab.research.google.com/drive/1ApZMyI7uAn1W-IwDVwh_ott--ojDJV-1#scrollTo=HSL-mGy-mF_J

### Maximal Marginal Relevance (MMR) :-

> How can we pick results that are not only relevant to the query but also different from each other.

- MMR is an information retrieval algorithim designed to reduce redundancy in the retrieved results while maintaining high relevance to the query.
- #### Why MMR Retriever ?
  - In regular similiarity search, we may get documents that are:
    - All very similar to each other
    - Repeating the same info.
    - Lacking diverse perspctives
  - MMR Retriever avoids that by:
    - Picking the most relevant document first
    - Then picking the next relevant and least similar to already selected docs and so on..
  - This helps especially in RAG pipelines where:
    - You want your context window to contain diverse but still relevant information.
    - Especially useful when documents are semantically overlapping.
      > Visit https://colab.research.google.com/drive/1ApZMyI7uAn1W-IwDVwh_ott--ojDJV-1#scrollTo=HSL-mGy-mF_J

### Multi-query Retriever :

> Sometimes a single query might not capture all the ways information is phrased in our docs.

- #### Query:-
  > How can I stay healthy ?
  - Could mean
    - What should I eat ?
    - How often should I exercise ?
    - How can I manage stress ?

### Contextual Compression Retriever :-

- The Contextual Compression Retriever in Langchain is an advanced retriever that improves retrival quality by compressing documents after retrieval - keeping only the relevant content based on the query.

- #### Query :-
  - > What is Photosynthesis ?
    - **Retrieval documents**

      > The grand canyon is a famous natural site.

      > Photosyntesis is how plant convert light into energy.

      > Many tourists visit the canyon for its scenic beauty.

    - Problem :-
      - The retriever returns the whole content of the document.
      - Only one setence is relevant to the query.\
      - The rest is irrelevant.
    - ##### What Contextual Compression Retriever does ?
      - Returns only the relevant content.
      - > Photosyntesis is how plant convert light into energy.

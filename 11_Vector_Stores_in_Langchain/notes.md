# Vector stores in Langchain

- **Why** ? :-

  - A vector store enables semantic search over documents by storing embeddings, allowing LangChain to retrieve relevant context for accurate, grounded LLM responses.
  - Vector stores give LLMs long-term semantic memory.

- What ? :-

  - A vector store is a system designed to store and retrieve data represented as numerical vectors.

  - Key features :-
    - **Storage** :- Ensures that vectors and their associated metadata are retained, wheather in-memory for quick lookups or on-disk for durability and large-scale use.
    - **Similarity Search** :- Helps retrieve the vectors most similar to a query vector.
    - **Indexing** :- Provide a data structure or method that enables fast similarity searches on high-dimensional vectors (e.g:- approximaate nearest neighbour lookups).
    - **CRUD Operation** :- Manage the lifecycle of data-adding new vectors, reading them, updating existing entries, removing outdated vectors.
  - Use cases :-
    - Semantic search
    - RAG
    - Recommender systems
    - Image/Multimedia search

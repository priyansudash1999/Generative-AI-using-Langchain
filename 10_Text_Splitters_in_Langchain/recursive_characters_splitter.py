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
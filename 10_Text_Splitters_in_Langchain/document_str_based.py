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
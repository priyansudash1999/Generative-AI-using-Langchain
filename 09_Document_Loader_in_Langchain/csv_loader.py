from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path= './files/csv_file.csv')

docs = loader.load()

print(docs[1])


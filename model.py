import openai
import os
from API_KEY import API_KEY

from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain import OpenAI

# change your api key in API_KEY.py file.
os.environ["OPENAI_API_KEY"]=API_KEY
openai.api_key = os.environ["OPENAI_API_KEY"]

# OpenAI document embedding instantiate
embeddings = OpenAIEmbeddings()

# Set your detectory path here
# Loading documents from directory
loader = DirectoryLoader('documents', glob="**/*.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=2500, 
                                      chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Embedding the documents
docsearch = Chroma.from_documents(texts, embeddings)

# Langchain tools for QandA
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(), 
    chain_type="stuff", 
    retriever=docsearch.as_retriever())

# Function to generate answer from the documents.
def query(q):
    return qa.run(q)

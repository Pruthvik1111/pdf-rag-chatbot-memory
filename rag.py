from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.llms import Ollama

def load_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    return documents

def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    return chunks
def get_embeddings():

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    return embeddings
def create_vectorstore(chunks):

    embeddings = get_embeddings()

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    return db
def get_llm():

    llm = Ollama(
        model="phi"
    )

    return llm
def get_retriever(db):

    retriever = db.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever
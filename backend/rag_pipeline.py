# backend/rag_pipeline.py
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

def create_vector_store(file_path="data/sample_resume.txt"):
    """Loads text, splits it, and creates a FAISS index for retrieval."""
    with open(file_path, "r") as f:
        text = f.read()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = [Document(page_content=chunk) for chunk in splitter.split_text(text)]

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    return db

def retrieve_relevant(query, db):
    """Finds the most relevant text chunks based on user query."""
    docs = db.similarity_search(query, k=3)
    return [d.page_content for d in docs]

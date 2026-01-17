import chromadb
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

# Define the persistent directory
CHROMA_PATH = "./chroma_db"


def get_retriever():
    """
    Initializes and returns a ChromaDB retriever from a predefined set of documents.
    """
    # Sample documents for our knowledge base
    docs = [
        Document(
            page_content="VS Code is a lightweight but powerful source code editor from Microsoft.",
            metadata={"source": "doc1", "topic": "tools"},
        ),
        Document(
            page_content="A virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.",
            metadata={"source": "doc2", "topic": "python"},
        ),
        Document(
            page_content="RAG, or Retrieval-Augmented Generation, is a technique for enhancing the accuracy and reliability of large language models (LLMs) with facts fetched from external sources.",
            metadata={"source": "doc3", "topic": "ai"},
        ),
        Document(
            page_content="FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.",
            metadata={"source": "doc4", "topic": "tools"},
        ),
    ]

    # Initialize OpenAI embeddings
    embeddings = OpenAIEmbeddings()

    # Create a new ChromaDB persistent client
    # This will save the vector store to disk in the 'chroma_db' directory
    db_client = chromadb.PersistentClient(path=CHROMA_PATH)

    # Create or load the vector store
    vectorstore = Chroma.from_documents(
        documents=docs, embedding=embeddings, persist_directory=CHROMA_PATH
    )

    # Create and return a retriever
    # 'k=2' means it will retrieve the top 2 most relevant documents
    return vectorstore.as_retriever(search_kwargs={"k": 2})


if __name__ == "__main__":
    # A simple test to verify the retriever is working
    print("Initializing and testing the vector store...")
    retriever = get_retriever()
    test_query = "What is RAG?"
    results = retriever.invoke(test_query)
    print(f"Retrieved {len(results)} documents for query: '{test_query}'")
    for doc in results:
        print(f"- {doc.page_content}")
    print("\nVector store setup complete and verified.")

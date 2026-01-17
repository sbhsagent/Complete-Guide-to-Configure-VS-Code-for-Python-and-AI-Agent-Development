from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from src.vector_store import get_retriever


def get_rag_chain():
    """
    Creates and returns a RAG chain using the vector store retriever.
    """
    retriever = get_retriever()

    # RAG prompt template
    template = """You are an assistant for question-answering tasks. 
    Use the following pieces of retrieved context to answer the question. 
    If you don't know the answer, just say that you don't know. 
    Keep the answer concise.

    Context: {context} 

    Question: {question} 

    Answer:"""

    prompt = ChatPromptTemplate.from_template(template)

    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # Create the RAG chain using LangChain Expression Language (LCEL)
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain


if __name__ == "__main__":
    # A simple test to verify the chain is working
    print("Testing the RAG chain...")
    chain = get_rag_chain()
    response = chain.invoke("What is FastAPI?")
    print(response)

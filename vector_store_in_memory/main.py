import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub

if __name__ == "__main__":
    print("hi")
    pdf_path = "C:/LangChain_application/vector_store_in_memory/2210.03629v3.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    documnets = loader.load()
    text_spliter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")
    docs= text_spliter.split_documents(documents=documnets)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = FAISS.from_documents(docs,embeddings)
    vectorstore.save_local("faiss_index_react")

    new_vecotrsotre = FAISS.load_local(
        "faiss_index_react", embeddings, allow_dangerous_deserialization=True
    )

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    combine_docs_chain = create_stuff_documents_chain(
        ChatOpenAI(model="gpt-4o-mini"), retrieval_qa_chat_prompt
    )
    retrieval_chain = create_retrieval_chain(
        new_vecotrsotre.as_retriever(), combine_docs_chain
    )

    res = retrieval_chain.invoke({"input": "Give me the gist of ReAct in 3 sentences"})
    print(res["answer"])


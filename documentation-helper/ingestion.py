import os
from dotenv import load_dotenv

load_dotenv()

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


def ingest_doc():
    loader = ReadTheDocsLoader("C:/LangChain_application/documentation-helper/langchain-docs/api.python.langchain.com/en/latest", encoding="utf-8")

    raw_documnets = loader.load()
    print(f"loaded {len(raw_documnets)} documnets")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documnets = text_splitter.split_documents(raw_documnets)

    for doc in documnets:
        new_url = doc.metadata["source"]
        new_url = new_url.replace("langchain-docs", "https:/")
        doc.metadata.update({"source":new_url})
    
    print(f"Going to add {len(documnets)} to Pinecone")
    PineconeVectorStore.from_documents(
        documnets, embeddings, index_name=os.environ['INDEX_NAME']
    )

    print("****Loading to vectorstore done ***")




if __name__ == "__main__":
    ingest_doc()
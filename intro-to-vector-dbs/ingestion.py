import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()


if __name__ == "__main__":
    print("Ingesting..")
    loader = TextLoader("C:\LangChain_application\intro-to-vector-dbs\mediumblog1.txt.txt",encoding="utf-8")
    document = loader.load()

    print("splitting...")
    text_spliter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
    texts = text_spliter.split_documents(documents=document)
    print(f"created {len(texts)} chunks")

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"), model="text-embedding-3-small")

    print("ingesting..")
    PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ['INDEX_NAME'])
    print("finish")
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_community.document_loaders import WebBaseLoader
from pathlib import Path
import os, requests
from dotenv import load_dotenv
from list_urls import get_urls

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    google_api_key=os.getenv("GEMINI_API_KEY"),
    model="models/embedding-001"
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap = 200
)

def processing_docs():
    all_links = get_urls()

    i=0
    for link in all_links:
        i += 1
        print(f"Processing link: {i}")

        try:
            loader = WebBaseLoader(f"{link}")
            docs = loader.load()

            # add metadata to each doc (applying for each and every page)
            for doc in docs:
                doc.metadata["url"] = link
                doc.metadata["section"] = link.split("/")[-3]
                doc.metadata["sub_section"] = link.split("/")[-2]

            split_docs = text_splitter.split_documents(documents=docs)


            vector_store = QdrantVectorStore.from_documents(
                documents=split_docs,
                url="http://localhost:6333",
                collection_name="chai_docs",
                embedding=embedding_model
            )

            print("Indexing of Documents done ...")


        except Exception as e:
            print(f"Failed for {link} - {i}: {e}")


# Processing all the chaidocs
# processing_docs()



# Debugging

# url = "https://docs.chaicode.com/youtube/chai-aur-git/github/"

# text = url.split("/")

# print(f"section:{text[-3]}")
# print(f"sub-section:{text[-2]}")
# ['https:', '', 'docs.chaicode.com', 'youtube', 'chai-aur-c', 'hello-world', '']


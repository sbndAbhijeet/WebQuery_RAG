from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_qdrant import QdrantVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

embedding_model = GoogleGenerativeAIEmbeddings(
    google_api_key=os.getenv("GEMINI_API_KEY"),
    model="models/embedding-001"
)

vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    collection_name="chai_docs",
    url="http://localhost:6333",
)


def process_query(query: str):
    search_results = vector_store.similarity_search(query=query)

    context = "\n\n\n".join([
        f"Page Content: {result.page_content}\nSection: {result.metadata['section']}\nSub-section: {result.metadata['sub_section']}\nurl: {result.metadata['url']}" for result in search_results
    ])

    SYSTEM_PROMPT = f"""
        You are a helpful assistant that gives detailed, accurate answers based on the provided document context.

        If you find relevant information in the context, answer the question clearly and concisely.
        If not, say: "I couldn’t find the answer from chaidocs."
        

        Always mention the section,subsection and url(to navigate) where relevant information was found.

        Output Format in JSON:
        {{
            "Answer": "<Give your detailed answer>",
            "Code": "<if necessary from context>",
            "Section": "<Relevant section from context>",
            "Sub_section": "<Relevant sub-section from context>",
            "url": "<Relevant URL from context>"
        }}

    """

    USER_PROMPT = f"""
        Use the following context to answer the question.
            Context: {context}
            Question: {query}
    """

    messages = [
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': USER_PROMPT}
    ]
    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        messages=messages,
        response_format={'type': 'json_object'},
    )

    result = response.choices[0].message.content

    return result
    


app = FastAPI()

#allow extension access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel): 
    question: str

@app.post("/query")
async def ask(query: Query):
    response = process_query(query.question)
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("chat:app", host="127.0.0.1", port=8000, reload=True)


# {"detail":[{"type":"missing","loc":["body","question"],"msg":"Field required","input":{"query":"how to use tailwind in
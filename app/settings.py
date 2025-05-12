from llama_index.core import Settings
from langchain_google_genai import ChatGoogleGenerativeAI
from llama_index.llms.langchain import LangChainLLM
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from llama_index.embeddings.langchain import LangchainEmbedding

def init_settings():
    Settings.llm = LangChainLLM(ChatGoogleGenerativeAI(model="gemini-2.0-flash"))
    Settings.embed_model = LangchainEmbedding(GoogleGenerativeAIEmbeddings(model="models/text-embedding-004"))

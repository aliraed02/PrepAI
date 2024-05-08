import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI




load_dotenv()
KEY = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-pro")

from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings





def indexing(path):
    loader = PyPDFLoader(path)
    pages = loader.load()


    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )


    docs = text_splitter.split_documents(pages)
    faiss_index = Chroma.from_documents(docs, GoogleGenerativeAIEmbeddings(model='models/embedding-001'))
    return faiss_index.as_retriever(search_type="similarity", search_kwargs={"k": 25})
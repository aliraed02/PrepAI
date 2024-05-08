from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings



def generate(selected_material, SUBJECT):

    material_options = ["English", "التربية الاسلامية", "تاريخ الاردن"]
    if selected_material == material_options[0]:
        PATH = r"D:\Python\Gen AI\Zinc\pdf docs\english.pdf"
    elif selected_material == material_options[1]:
        PATH = r"D:\Python\Gen AI\Zinc\pdf docs\islamic.pdf"
    else:
        PATH = r"D:\Python\Gen AI\Zinc\pdf docs\history.pdf"




    loader = PyPDFLoader(PATH)
    pages = loader.load()


    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=600,
        chunk_overlap=200,
        length_function=len,
    )


    docs = text_splitter.split_documents(pages)
    faiss_index = FAISS.from_documents(docs, GoogleGenerativeAIEmbeddings(model='models/embedding-001'))
    DOCS = faiss_index.similarity_search(SUBJECT, 25)
    return DOCS

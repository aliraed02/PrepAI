import sys
import streamlit as st
from QA_rag import indexing
from QA_chains import QuestionAnsweringSystemEN, QuestionAnsweringSystemAR



sys.path.append('..')
############################################################################


st.set_page_config(page_title= "Ask PrepAI", page_icon = "🔍", layout='wide')

page_bg_img = """
<style>
    [data-testid="stAppViewContainer"]{
        background: linear-gradient(to top, #dfe9f3 0%, white 100%)
        }
        .text-style{
        color: #3a9188;
        }
        p{
        font-size:28px;
        }

    </style>
    """
    # st.markdown("The next word is :red[red]")
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(f"<h1 class='text-style'>Ask PrepAI🔍</h1>", unsafe_allow_html=True)






def main():

    material_options = ["English", "التربية الاسلامية", "تاريخ الاردن"]
    selected_material = st.sidebar.selectbox("Select your material", material_options)
    question = st.sidebar.text_input("Enter a question to search for:")
    if st.sidebar.button("Ask!"):
        with st.spinner('Loading...'):
            if material_options[0] == selected_material:
                retrieval = indexing(r'D:\Python\Gen AI\Zinc\pdf docs\english.pdf')
                qw = QuestionAnsweringSystemEN(retriever=retrieval, question=question)
                st.write(qw.answer_question())
            elif material_options[1] == selected_material:
                retrieval = indexing(r'D:\Python\Gen AI\Zinc\pdf docs\islamic.pdf')
                qw = QuestionAnsweringSystemAR(retriever=retrieval, question=question)
                st.write(qw.answer_question())
            else:
                retrieval = indexing(r'D:\Python\Gen AI\Zinc\pdf docs\history.pdf')
                qw = QuestionAnsweringSystemAR(retriever=retrieval, question=question)
                st.markdown(qw.answer_question())






if __name__ == '__main__':
    main()
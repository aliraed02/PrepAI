import sys
import streamlit as st
from rag import generate
from run_chain import run



sys.path.append('..')
###################################################################


st.set_page_config(page_title= "Generate Exam", page_icon= "🔍", layout='wide')
st.title("Generate Exam")


page_style = """
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
st.markdown(page_style, unsafe_allow_html=True)
st.markdown(f"<h1 class='text-style'>Generate Questions📚</h1>", unsafe_allow_html=True)





def click_button():
    st.session_state.clicked = True



def main():


    material_options = ["English", "التربية الاسلامية", "تاريخ الاردن"]
    tone_options = ['simple', 'medium', 'hard']
    selected_material = st.sidebar.selectbox("Select your material", material_options)
    subject = st.sidebar.text_input("Enter a subject to search for:")
    num_questions = st.sidebar.number_input("Number of questions to generate:", min_value=1, max_value=20, value=5)
    selected_tone = st.sidebar.selectbox("Select Tone", tone_options)
    
    
    
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False
    st.sidebar.button('Generate!', on_click=click_button)
    if st.session_state.clicked:
        with st.spinner("Generate"):
            run(generate(selected_material, subject), num_questions, subject, selected_tone)
            

















    #SUBJECT = 'complementary medicin is a really solution'



if __name__ == "__main__":

    main()
































































    # data = {
    #     "1": {
    #         "mcq": "What is complementary medicine used for?",
    #         "option": {
    #             "a": "Curing all diseases",
    #             "b": "Treating certain medical conditions",
    #             "c": "Replacing conventional medicine",
    #             "d": "Preventing malaria"
    #         },
    #         "correct": "b"
    #     },
    #     "2": {
    #         "mcq": "What is NOT a condition that can be treated with complementary medicine?",
    #         "option": {
    #             "a": "Insomnia",
    #             "b": "Arthritis",
    #             "c": "Migraines",
    #             "d": "Malaria"
    #         },
    #         "correct": "d"
    #     },
    #     # ... Add remaining questions from your data ...
    #     "5": {
    #         "mcq": "According to the text, why are some doctors more open to complementary medicine now?",
    #         "option": {
    #             "a": "Because it has been proven to be more effective than conventional medicine",
    #             "b": "Because there is now more scientific evidence supporting its effectiveness",
    #             "c": "Because it is becoming more popular with patients",
    #             "d": "Because it is a cheaper option"
    #         },
    #         "correct": "b"
    #     }
    # }
    #generate_exam(questions)


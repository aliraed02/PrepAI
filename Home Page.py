import streamlit as st 


st.set_page_config(page_title= "Home Page", page_icon = "🏠", layout="wide")

# Design - Home page
page_bg_img = """
<style>
    [data-testid="stAppViewContainer"]{
    background: linear-gradient(to top, #dfe9f3 0%, white 100%)
    }
    .stMarkdown{
    color:#3a9188;
    }
    .colored-text {
    color:#EFAE4B;
        }
    .white-text{
    color: #3a9188;
    }
    h3{
    font-style: italic;
    }
    h3:hover{
    color: #3a9188;
    }
    .span-text{
    font-size: 22px;
    color:#3a9188;
    }
    .span-text:hover{
    font-size: 22px;
    color:#EFAE4B;
    }
    .box{
    font-size: 22px;
    color:#3a9188;
    box-shadow: rgba(0, 0, 0, 0.09) 0px 3px 12px;
    text-align: center;
    }

</style>
"""
# st.markdown("The next word is :red[red]")
st.markdown(page_bg_img, unsafe_allow_html=True)
# ----
st.markdown(f"<h1 class='white-text'>Welcome to PrepAI</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 class='colored-text'>Your ultimate destination for extensive exam preparation tailored just for you.</h3>", unsafe_allow_html=True)

st.markdown(f"<h2 class='white-text'>Features:</h2>", unsafe_allow_html=True)

st.markdown(f"<span class='span-text' > *Customized Practice Sessions📚*: Choose your textbook, subject, and number of questions. Click a button to generate MCQs for targeted practice sessions aligned with your study goals.</span>", unsafe_allow_html=True)
st.markdown(f"<span class='span-text' >*Ask Anything🔍*: Need help with a concept or have questions? Our platform lets you ask anything, and we'll give you clear answers.</span>", unsafe_allow_html=True)

st.markdown(f"<h2 class='white-text'>Our mission: </h2>", unsafe_allow_html=True)
st.markdown(f"<p class='box'>Making Tawjihi students fully prepared before their exams.</p>",unsafe_allow_html=True)
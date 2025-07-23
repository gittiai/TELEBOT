from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate , PromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
st.sidebar.image("https://i.pinimg.com/736x/ed/c7/15/edc71589ae31bf6e170926b883ada8c6.jpg", width=250)    
GROQ_API = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY =os.getenv("GEMINI_API_KEY")
llm1=ChatGroq(model="llama-3.1-8b-instant",temperature=0.3)
llm2=ChatGroq(model="llama-3.1-8b-instant",temperature=0.7)
llm3=ChatGroq(model="llama-3.1-8b-instant",temperature=0.98)
st.sidebar.markdown("## 📢 How to Use Telebot")
st.sidebar.markdown("""
1."Enter a Topic"

2."Choose a Tone (Motivational,Tips and more)"

3."Click "Generate Post" under each version "

4."Pick your favorite post — or try all three!"

5."Want to share it in another language? Use the "Translate to" dropdown to convert it to Hindi, Tamil, Telugu, and more.


""")

st.title("TELEBOT(Your Personal Telegram Post Generator)")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1740904136738-a23a60953ae2?q=80&w=1674&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] {
        background-image: url("https://images.unsplash.com/photo-1740904136738-a23a60953ae2?q=80&w=1674&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-repeat: no-repeat;
       
    }
    </style>
    """,
    unsafe_allow_html=True
)
if "history" not in st.session_state:
    st.session_state.history = []

user_input=st.text_input("Enter the Topic")

tone = st.radio("Select Tone", ["Motivational", "announcement style", "Relatable", "Tips"])
st.subheader("Pick your favorite:")

prompt=PromptTemplate(
 template="""
You are a professional Telegram Post writer with over 30 years of expirience in the field of JEE/NEET.

Write a Telegram post based on the user_input{text}-
**Post should Feel like Human Generated and not not ChatGPT tone**
> Keep length of post short within (70-80)words
> Keep the post in {tone} tone
> Do add 1–2 suggested CTAs (e.g., "drop a ❤️", "reply with your score") related to user_input 
> Do add 3–4 Hashtags related to user_input (e.g., #IITJEE,#NEET,#JEEAdvanced,#PaperPhodnaHai) 
> Do add 1 line space between post , CTAs and Hashtags
> Format should be first add post then CTAs and at last Hashtags

""",
 input_variables=["text","tone"]
)
prompt2=PromptTemplate(
  template="""
  Convert the Result{text} generated into the selected{language}
  """,
  input_variables=["text","language"]
 )

languages = ["Hindi", "Telugu", "Marathi", "English", "Tamil", "Gujarati", "Urdu", "Kannada", "Odia", "Malayalam", "Punjabi"]

col1, col2, col3 = st.columns(3)

with col1:
 st.subheader("Post 1")
 chain1=prompt|llm1
 if st.button("Generate Post",key="generate_btn_1"):
   result1=chain1.invoke({"text":user_input,"tone":tone})
   st.session_state.gen_result1 = result1.content
   st.session_state.history.append({
    "user_input":user_input,
    "post_generated":result1.content
   })
  

 if "gen_result1" in st.session_state:
  st.markdown(st.session_state.gen_result1)
  lang1 = st.selectbox("Translate to", languages, key="lang_1")
  trans_chain1=prompt2|llm1
  if st.button("Generate",key="translate_btn_1"):
   result_trans1=trans_chain1.invoke({"text":st.session_state.gen_result1,"language":lang1})
   st.markdown(result_trans1.content)
   st.session_state.history.append({
    "user_input":user_input,
    "post_generated":result_trans1.content
   })
  


with col2:
 st.subheader("Post 2")
 chain2=prompt|llm2
 if st.button("Generate Post",key="generate_btn_2"):
   result2=chain2.invoke({"text":user_input,"tone":tone})
   st.session_state.gen_result2 = result2.content
   st.session_state.history.append({
    "user_input":user_input,
    "post_generated":result2.content
   })

 if "gen_result2" in st.session_state:
  st.markdown(st.session_state.gen_result2)
  lang2 = st.selectbox("Translate to", languages, key="lang_2")
  trans_chain2=prompt2|llm2
  if st.button("Generate",key="translate_btn_2"):
   result_trans2=trans_chain2.invoke({"text":st.session_state.gen_result2,"language":lang2})
   st.markdown(result_trans2.content)
   st.session_state.history.append({
    "user_input":user_input,
    "post_generated":result_trans2.content
   })

with col3:
 st.subheader("Post 3")
 chain3=prompt|llm3
 if st.button("Generate Post",key="generate_btn_3"):
   result3=chain2.invoke({"text":user_input,"tone":tone})
   st.session_state.gen_result3 = result3.content
   st.session_state.history.append({
    "user_input":user_input,
    "post_generated":result3.content
   })

 if "gen_result3" in st.session_state:
  st.markdown(st.session_state.gen_result3)
  lang3 = st.selectbox("Translate to", languages, key="lang_3")
  trans_chain3=prompt2|llm3
  if st.button("Generate",key="translate_btn_3"):
   result_trans3=trans_chain2.invoke({"text":st.session_state.gen_result3,"language":lang3})
   st.markdown(result_trans3.content)
   st.session_state.history.append({
    "user_input":user_input,
    "post_generated":result_trans3.content
   })

if st.session_state.history:
    st.markdown(" History")
    for i, item in enumerate((st.session_state.history)):
        with st.expander(f"Post{i+1} | Topic:{item['user_input']}"):
            st.markdown(item["post_generated"])

    if st.button("🧹 Clear History"):
        st.session_state.history.clear()
        st.success("History cleared.")



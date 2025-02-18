import os
import streamlit as st
from mistralai import Mistral
from dotenv import load_dotenv

#### Load API key
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

#### Initialize Mistral AI Client
client = Mistral(api_key=MISTRAL_API_KEY)

#### Streamlit UI
st.set_page_config(page_title="InfoMover AI", page_icon="🤖" , layout="wide")

#### Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

def clear_input():
    st.session_state['user_input'] = ""

#### Layout setup: Sidebar + Centered Chat Window
with st.sidebar:
    st.title("📌 InfoMoverAI")
    st.write("Your AI assistant")

    # Clear chat history button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []  # Reset chat history
        st.rerun()  # Refresh the UI to reflect the changes

left_spacer, chat_container, right_spacer = st.columns([1, 2, 1])

with chat_container:
    st.title("🤖 InfoMover AI")

    #### Display chat messages inside an empty placeholder
    chat_area = st.empty()
    with chat_area.container():  #### Ensures chat messages stay above input
        for message in st.session_state['messages']:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

#### ** Dynamic Input Box (Fixed at Bottom)**
input_placeholder = (
    "Hey there, I'm InfoMover AI... Ask me anything:"
    if not st.session_state.messages
    else "Send a message"
)
user_input = st.chat_input(input_placeholder)  # Dynamic placeholder

if user_input:
    #### Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    # clear_input()

    #### Generate AI response
    response = client.chat.complete(
        model="mistral-large-latest",
        messages=st.session_state.messages
    )
    bot_reply = response.choices[0].message.content
    #### Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.rerun()



### Started working on Custom AI model selection











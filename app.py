import streamlit as st
from dotenv import load_dotenv

from response import get_response

# Allerede gjort skrapingen
    ##text = scrape_all_pages("https://www.coax.no/")

## denne burde lastes opp til en database, og ikke lagres lokalt
VectorStoreFile = "COAX_web_content.pkl"

with st.sidebar:
    st.title("COAX AS Chatbot")
    st.markdown('''
    ## Chat med COAX AS
    Dette er en chatbot for COAX As. Den kan svare på alt en kunde måtte lure på om selskapet, deres produkter og andre opplysninger.    
    ''')
    #add_vertical_space(5)
    st.write("-----------------------------")
    st.write("@Preben Andersen")

def main():
    load_dotenv()

    st.title("COAX AS Chatbot")

    # Definer CSS for layout og knappstil
    layout_style = """
    <style>
        .chatbox {
            border: 2px solid #ccc;
            padding: 10px;
            overflow-y: scroll;
            height: 300px;
        }
        .stTextInput > div > div > input {
            border-radius: 5px 0 0 5px;
        }
        .stButton > button {
            border-radius: 0 5px 5px 0;
            height: 34px;  /* Juster høyden for å passe til tekstfeltet */
            margin-top: 25px; /* Finjustering av vertikal posisjon */
            margin-left: 20px; /* Finjustering av horisontal posisjon */
        }
    </style>
    """

    st.markdown(layout_style, unsafe_allow_html=True)

    if 'history' not in st.session_state:
        st.session_state.history = [("🤖 COAX AI:", "Velkommen! Still meg et spørsmål om COAX AS.")]

    if 'total_cost' not in st.session_state:
        st.session_state.total_cost = 0 


    if 'cost' not in st.session_state:
        st.session_state.cost = None
        st.session_state.tokens = None


    chat_content = ""
    for question, answer in st.session_state.history:
        chat_content += f"<div><b>{question}</b> {answer}</div><br>"


    st.markdown(f"<div class='chatbox'>{chat_content}</div>", unsafe_allow_html=True)

    # Tekstfelt og knapp side ved side
    col1, col2 = st.columns([5, 1])  # Juster forholdet etter behov
    with col1:
        user_input = st.text_input("Ask your question here:", key="question", label_visibility="hidden")
    with col2:
        if st.button("Send"):
            user_question = user_input
            response, callback_info = get_response(user_question, VectorStoreFile)

            st.session_state.history.append(("👤 You:", user_question))
            st.session_state.history.append(("🤖 COAX AI:", response))
            ## Generating ....

            current_cost_NOK = round(callback_info.total_cost * 10.81, 2)
            st.session_state.cost = f"Total kostnad: {current_cost_NOK} NOK"
            st.session_state.tokens = f"Antall tokens brukt: {callback_info.total_tokens}"
            st.session_state.total_cost += current_cost_NOK

            st.experimental_rerun()
    
    if st.session_state.cost and st.session_state.tokens and st.session_state.total_cost:
        st.write(st.session_state.cost)
        st.write(st.session_state.tokens)
        st.write("-----------------------------")
        st.write(f"Total kostnad for samtalen: {st.session_state.total_cost} NOK")

if __name__ == '__main__':
    main()

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
    ## Chat with COAX AS
    This is a demo chatbot that can answer questions about COAX AS.    
    ''')
    #add_vertical_space(5)
    st.write("-----------------------------")
    st.write("Made by Preben Andersen")



def main():

    load_dotenv()

    st.title("COAX AS Chatbot")
    st.text("This is a chatbot that can answer questions about COAX AS")
    st.text("Please ask a question about COAX AS")

    question = st.text_input("Q", placeholder="Message COAX AS...")
    ## chattbot interface

    if st.button("Ask"):
        response, callback_info = get_response(question, VectorStoreFile)

        st.text_area("A", response, height=100)

        total_cost_NOK = callback_info.total_cost * 10.81
        st.write("Total kostnad: "+str(total_cost_NOK)+" NOK")
        st.write("Antall tokens brukt: "+str(callback_info.total_tokens))
        

if __name__ == '__main__':
    main()
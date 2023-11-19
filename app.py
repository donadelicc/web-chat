import streamlit as st
from dotenv import load_dotenv

from web_scrape import fetch_website_content, get_internal_links, scrape_all_pages
from web_content import embedd_text
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
        response = get_response(question, VectorStoreFile)

        st.text_area("A", response, height=100)


if __name__ == '__main__':
    main()
import streamlit as st

def app():
    with open('styles/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.markdown('<link rel="preconnect" href="https://fonts.googleapis.com">',
                    unsafe_allow_html=True)
    st.title("Kpop Analysis")
    st.markdown('<h2>Welcome to our project!</h2>', unsafe_allow_html=True)

import streamlit as st
from CustomerDAO import CustomerDAO

# streamlit run main_streamlit.py
def main():
    st.set_page_config(layout="wide")

    st.write("""# Hello
             
## Titre de niveau 2

- list item 01
- list item 02
- list item 03

un texte en **gras**.
             """)
    title = st.text_input("Your name", "")

    if st.button('Say hello'):
        st.write("Hello", title)

    with st.spinner("Wait for it...", show_time=True):
        dao = CustomerDAO('customers_db.db')
        customers = dao.findAll()
    st.table(customers)

if __name__ == '__main__':
    main()
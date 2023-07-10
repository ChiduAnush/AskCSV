import streamlit as st


def main():
    st.set_page_config(page_title="AskCSV")
    st.header("Ask you CSV 😪")

    user_csv = st.file_uploader("upload your csv file below ", type="csv")

    if user_csv is not None:
        user_question = st.text_input("yo, ask me something from the csv")


if __name__ == "__main__":
    main()

import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv


def main():

    load_dotenv()

    st.set_page_config(page_title="AskCSV")
    st.header("Ask you CSV 😪")

    user_csv = st.file_uploader("upload your csv file below", type="csv")

    if user_csv is not None:
        user_question = st.text_input("yo, ask me something from the csv")

        if user_question is not None and user_question != "":
            st.write(f"your question was : {user_question}")

        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm, user_csv, verbose=True)


if __name__ == "__main__":
    main()

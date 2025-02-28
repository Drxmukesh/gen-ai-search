import streamlit as st
from data_collection import collect_data
from summarization import summarize_data
from analysis import analyze_data
from output_generation import generate_output

def main():
    st.title("AI Search Engine")
    st.write("Enter your search query below:")

    query = st.text_input("Search Query")

    if st.button("Search"):
        if query:
            st.write("Collecting data...")
            data = collect_data(query)
            st.write("Data collected. Summarizing...")
            summary = summarize_data(data)
            st.write("Data summarized. Analyzing...")
            analysis_results = analyze_data(summary)
            st.write("Analysis complete. Generating output...")
            output = generate_output(analysis_results)
            st.write("Output generated:")
            st.write(output)
        else:
            st.warning("Please enter a search query.")

if __name__ == "__main__":
    main()
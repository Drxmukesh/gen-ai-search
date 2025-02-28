def generate_output(analysis_results):
    """
    Generate formatted output based on the analysis results.
    
    Parameters:
    analysis_results (dict): A dictionary containing the results of the analysis.
    
    Returns:
    str: A formatted string for display in the Streamlit app.
    """
    output = "### Analysis Results\n\n"
    
    for key, value in analysis_results.items():
        output += f"**{key}:** {value}\n\n"
    
    return output

def display_output(output):
    """
    Display the generated output in a Streamlit-friendly format.
    
    Parameters:
    output (str): The formatted output string to be displayed.
    """
    import streamlit as st
    
    st.markdown(output)
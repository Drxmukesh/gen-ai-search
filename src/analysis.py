import pandas as pd
import numpy as np

def analyze_data(summary_data):
    """
    Analyzes the summarized data to extract insights.
    
    Parameters:
    summary_data (list): A list of summarized texts.
    
    Returns:
    dict: A dictionary containing analysis results.
    """
    # Example analysis: word count and average word length
    analysis_results = {
        'total_summaries': len(summary_data),
        'average_word_count': np.mean([len(summary.split()) for summary in summary_data]),
        'average_word_length': np.mean([np.mean([len(word) for word in summary.split()]) for summary in summary_data])
    }
    
    return analysis_results

def generate_insights(analysis_results):
    """
    Generates insights based on the analysis results.
    
    Parameters:
    analysis_results (dict): A dictionary containing analysis results.
    
    Returns:
    str: A formatted string of insights.
    """
    insights = (
        f"Total Summaries Analyzed: {analysis_results['total_summaries']}\n"
        f"Average Word Count per Summary: {analysis_results['average_word_count']:.2f}\n"
        f"Average Word Length: {analysis_results['average_word_length']:.2f}"
    )
    
    return insights
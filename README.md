# AI Search Engine

This project is a Streamlit web application that serves as an AI-powered search engine utilizing DuckDuckGo for data collection and Keras for data processing. The application allows users to input search queries, retrieves relevant information, summarizes the data, analyzes it, and generates a formatted output for display.

## Project Structure

```
ai-search-engine
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   ├── data_collection.py     # Functions for collecting data from DuckDuckGo
│   ├── summarization.py       # Functions for summarizing collected data using Keras
│   ├── analysis.py            # Functions for analyzing summarized data
│   └── output_generation.py    # Functions for generating final output for display
├── requirements.txt           # List of dependencies for the project
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   https://github.com/Drxmukesh/gen-ai-search.git
   cd gen-ai-search
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

## Usage Guidelines

- Enter your search query in the input field provided in the Streamlit interface.
- The application will collect data from DuckDuckGo based on your query.
- The collected data will be summarized and analyzed to extract insights.
- The final output will be displayed in a user-friendly format.

## Features

- AI-powered search using DuckDuckGo.
- Data summarization using Keras models.
- Analytical insights derived from the summarized data.
- Interactive web interface built with Streamlit.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

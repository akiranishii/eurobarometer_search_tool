
# Eurobarometer Data Explorer

Access the app using this link: https://akiranishii-eurobarometer-search-tool-main-itn0px.streamlit.app/

This Streamlit app allows users to explore the Eurobarometer data by filtering survey results based on keywords, years, and countries. The app provides an interactive interface for users to input their preferences and view the filtered results in real-time.

## App Features

1. **Keyword search:** Users can input a list of comma-separated keywords to search for in the survey texts. The app will display the results containing those keywords with surrounding context. If a page contains the same keyword multiple times, the app will create a separate row for each occurrence.

2. **Year range selection:** Users can select a range of years to filter the survey results by using a slider. This feature enables users to focus on specific time periods.

3. **Country selection:** Users can select one or multiple countries from a dropdown list to filter the survey results by the countries involved. This feature allows users to focus on specific geographical regions.

## How to Use

1. Enter your desired keywords in the "Enter keywords separated by commas" input box. The app will filter the survey results based on the presence of these keywords.

2. Use the "Select the range of survey years" slider to specify a range of years for the survey results.

3. Select the desired countries from the "Select countries" dropdown list.

4. The filtered results will be displayed as a table below the input controls.

## Limitations

- The current implementation assumes that the keywords are not overlapping in the survey texts. If they are, the extracted phrases might not be accurate.

- The app might return a larger number of rows in the resulting DataFrame since it creates a new row for each keyword occurrence.

## Future Improvements

1. Implement more sophisticated text similarity techniques, such as cosine similarity or Jaccard similarity based on word frequency vectors, to measure how similar two texts are.

2. Employ natural language processing (NLP) techniques to identify the context and semantic meaning of the questions, such as named entity recognition or sentiment analysis.

3. Leverage clustering algorithms to group similar questions together, which can help in identifying common themes or topics.

4. If dealing with multilingual data, use machine translation to convert all texts into a common language before applying the similarity analysis.$


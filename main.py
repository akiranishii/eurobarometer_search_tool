import pandas as pd
import streamlit as st 

df = pd.read_csv('merged_df.csv')


st.markdown(""" This is a Streamlit App """)

# Streamlit app code
st.title("Explore the Eurobarometer Data")

# User input for keywords
keywords_input = st.text_input("Enter keywords separated by commas:", "")
privacy_keywords = [keyword.strip().lower() for keyword in keywords_input.split(',')]

# User input for year range
min_year, max_year = st.slider("Select the range of survey years:", min(df['Year of survey']), max(df['Year of survey']), (min(df['Year of survey']), max(df['Year of survey'])))

# Create a list of unique countries in the DataFrame
all_countries = set()
for countries_str in df['Countries']:
    countries = [country.strip() for country in countries_str.split()]
    all_countries.update(countries)

# User input for countries
selected_countries = st.multiselect('Select countries:', sorted(list(all_countries)))

def wrap_keywords_in_bold(text, keywords):
    for keyword in keywords:
        text = text.replace(keyword, f'<b>{keyword}</b>')
    return text

# Function to filter the dataframe
def filter_dataframe(df, privacy_keywords):
    matching_rows = []
    matching_phrases = []

    for index, row in df.iterrows():
        if any(keyword in row['sentence'].lower() for keyword in privacy_keywords):
            matching_rows.append(row)
            words = row['sentence'].lower().split()
            index_keyword = [i for i, word in enumerate(words) if word in privacy_keywords]
            if index_keyword:
                keyword_index = index_keyword[0]
                start = max(0, keyword_index - 2)
                end = min(len(words), keyword_index + 3)
                if keyword_index - start < 2:
                    start = max(0, keyword_index - 1)
                if end - keyword_index < 2:
                    end = min(len(words), keyword_index + 2)
                phrase = ' '.join(words[start:end])
                # phrase = wrap_keywords_in_bold(phrase, privacy_keywords) # Wrap keywords in bold
            else:
                phrase = ''
            matching_phrases.append(phrase)

    new_df = pd.DataFrame(matching_rows)
    new_df['matching_phrase'] = matching_phrases
    # new_df['sentence'] = new_df['sentence'].apply(lambda x: wrap_keywords_in_bold(x, privacy_keywords)) # Wrap keywords in bold for 'sentence' column

    return new_df

# Filter dataframe based on user's keywords
if privacy_keywords:
    filtered_df = filter_dataframe(df, privacy_keywords)
    filtered_df = filtered_df[(filtered_df['Year of survey'] >= min_year) & (filtered_df['Year of survey'] <= max_year)]
    
    if privacy_keywords:
        filtered_df = filter_dataframe(filtered_df, privacy_keywords)

    if selected_countries:
        filtered_df = filtered_df[filtered_df['Countries'].apply(lambda x: any(country in x.split() for country in selected_countries))]
    
    st.write(filtered_df)

    # Convert the filtered DataFrame to an HTML table with bold keywords
    # html_table = filtered_df.to_html(escape=False, index=False)
    # st.markdown(html_table, unsafe_allow_html=True)




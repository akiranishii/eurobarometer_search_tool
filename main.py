import pandas as pd
import streamlit as st 

st.set_page_config(layout='wide')

df = pd.read_csv('merged_df_links.csv')
df['extracted_text'] = df['extracted_text'].astype(str)
first_column_name = df.columns[0]
df = df.drop(columns=[first_column_name])



st.markdown(""" Please send any feedback or feature requests to anishii dot umich dot edu """)

# Streamlit app code
st.title("Eurobarometer Data Exploration Tool")

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
selected_countries = st.multiselect('Select required countries:', sorted(list(all_countries)))

def wrap_keywords_in_bold(text_series, keywords):
    return text_series.apply(lambda text: ' '.join([f'<b>{word}</b>' if word.lower() in keywords else word for word in text.split()]))

def filter_dataframe(df, privacy_keywords):
    matching_rows = []

    for index, row in df.iterrows():
        words = row['extracted_text'].lower().split()
        indices_keyword = [i for i, word in enumerate(words) if word in privacy_keywords]

        if indices_keyword:  # Check if there are any keyword occurrences
            for keyword_index in indices_keyword:
                start = max(0, keyword_index - 2)
                end = min(len(words), keyword_index + 3)
                if keyword_index - start < 2:
                    start = max(0, keyword_index - 1)
                if end - keyword_index < 2:
                    end = min(len(words), keyword_index + 2)
                phrase = ' '.join(words[start:end])
                
                new_row = row.copy()
                new_row['matching_phrase'] = phrase
                matching_rows.append(new_row)

    new_df = pd.DataFrame(matching_rows)

    return new_df


# Filter dataframe based on user's keywords
if not privacy_keywords or privacy_keywords == [""]:
    filtered_df = df
else:
    filtered_df = filter_dataframe(df, privacy_keywords)

# Filter by year range
filtered_df = filtered_df[(filtered_df['Year of survey'] >= min_year) & (filtered_df['Year of survey'] <= max_year)]

# Filter by selected countries
if selected_countries:
    filtered_df = filtered_df[filtered_df['Countries'].apply(lambda x: any(country in x.split() for country in selected_countries))]

st.write(filtered_df)




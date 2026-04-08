import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv('/content/netflix_titles.csv')
df
df.head()
df.tail()
df.info()
df.shape
df.describe()
df.isnull().sum()
df = df.dropna()
print("Null values removed ✅")
top_countries = df['country'].value_counts().head(5)
print(top_countries)
top_genres = df['listed_in'].value_counts().head(5)
print(top_genres)
top_genres.plot(kind='pie')
plt.title("Top Genres")
plt.show()
top_years = df['release_year'].value_counts().head(5)
print(top_years)
question = input("Ask your question: ")
if "country" in question:
    result = df['country'].value_counts().head(5)
    print("\nTop Countries:\n", result)
    result.plot(kind='bar')
    plt.show()

elif "genre" in question:
    result = df['listed_in'].value_counts().head(5)
    print("\nTop Genres:\n", result)
    result.plot(kind='bar')
    plt.show()

elif "year" in question:
    result = df['release_year'].value_counts().head(5)
    print("\nTop Years:\n", result)
    result.plot(kind='bar')
    plt.show()

else:
    print("❌ Question not supported")
while True:
    question = input("Ask your question (type 'exit'): ").lower()

    if question == "exit":
        break

    elif "country" in question:
        print(df['country'].value_counts().head(5))

    elif "genre" in question:
        print(df['listed_in'].value_counts().head(5))

    elif "year" in question:
        print(df['release_year'].value_counts().head(5))

    elif "rating" in question:
        print(df['rating'].value_counts().head(5))

    elif "movie" in question:
        print(df['type'].value_counts())

    elif "recent" in question:
        print(df.sort_values(by='release_year', ascending=False).head(5))

    else:
        print("❌ Not supported")
if any(word in question for word in ["country", "nation", "place"]):
    print(df['country'].value_counts().head(5))

elif any(word in question for word in ["genre", "category", "type"]):
    print(df['listed_in'].value_counts().head(5))

elif any(word in question for word in ["year", "date", "released"]):
    print(df['release_year'].value_counts().head(5))
import sys
!{sys.executable} -m pip install streamlit
import streamlit as st
import streamlit as st
import pandas as pd
%%writefile app.py
import streamlit as st
import pandas as pd

st.title("AI Data Analyst 🤖")

question = st.text_input("Ask your question:")

# Placeholder for the logic to handle questions
if question:
    st.write(f"You asked: {question}")
    st.write("Sorry, I can only respond to a fixed set of questions now")
!streamlit run app.py




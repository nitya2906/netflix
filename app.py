import numpy as np
import pandas as pd



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

import streamlit as st
import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd

st.title("AI Data Analyst 🤖")

question = st.text_input("Ask your question:")

# Placeholder for the logic to handle questions
if question:
    st.write(f"You asked: {question}")
    st.write("Sorry, I can only respond to a fixed set of questions now")





import streamlit as st
import string
import nltk
from nltk.corpus import stopwords
from collections import Counter
import textstat

# Download required NLTK data
nltk.download('stopwords')

# Ensure stopwords are available
stop_words = set(stopwords.words('english'))

def text_analysis(text):
    text_no_punct = text.translate(str.maketrans('', '', string.punctuation))
    words = text_no_punct.split()
    
    word_count = len(words)
    char_count = len(text)
    most_common_words = Counter(words).most_common(5)
    readability_score = textstat.flesch_reading_ease(text)
    
    stop_words_removed = [word for word in words if word.lower() not in stop_words]
    filtered_word_count = len(stop_words_removed)
    
    return {
        "Word Count": word_count,
        "Character Count": char_count,
        "Most Common Words": most_common_words,
        "Readability Score": readability_score,
        "Filtered Word Count (No Stopwords)": filtered_word_count
    }

def main():
    st.set_page_config(page_title="Text Analyzer", page_icon="📝", layout="centered")
    st.title("Text Analyzer")
    st.write("Enter text below to analyze various metrics.")
    
    text_input = st.text_area("Enter your text here:")
    
    if st.button("Analyze Text"):
        if text_input.strip():
            results = text_analysis(text_input)
            st.subheader("Analysis Results")
            
            st.write(f"**Word Count:** {results['Word Count']}")
            st.write(f"**Character Count:** {results['Character Count']}")
            st.write(f"**Readability Score:** {results['Readability Score']:.2f}")
            st.write(f"**Filtered Word Count (No Stopwords):** {results['Filtered Word Count (No Stopwords)']}")
            
            st.subheader("Most Common Words")
            for word, count in results['Most Common Words']:
                st.write(f"{word}: {count} times")
        else:
            st.warning("Please enter text to analyze.")

if __name__ == "__main__":
    main()
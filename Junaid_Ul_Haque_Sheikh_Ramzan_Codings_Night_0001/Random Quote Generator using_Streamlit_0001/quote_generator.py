import streamlit as st
import random

# List of motivational quotes
quotes = [
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Sometimes later becomes never. Do it now.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don’t stop when you’re tired. Stop when you’re done."
]

# Streamlit app
def main():
    st.title("🌟 Random Quote Generator")
    st.write("Click the button below to get a motivational quote!")

    if st.button("Generate Quote"):
        quote = random.choice(quotes)
        st.success(quote)

if __name__ == "__main__":
    main()

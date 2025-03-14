import streamlit as st
import random
import datetime

# Growth mindset challenges
challenges = [
    "Write down 3 things you learned today.",
    "Try a new approach to a problem you recently faced.",
    "Seek feedback from someone and act on it.",
    "Identify a challenge you avoided and take a small step towards it.",
    "Reflect on a mistake and what you learned from it.",
    "Encourage someone else to embrace a growth mindset.",
    "Read or watch something that expands your knowledge."
]

# Motivational quotes
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Challenges are what make life interesting and overcoming them is what makes life meaningful.",
    "You miss 100% of the shots you don’t take.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Believe you can and you're halfway there."
]

# Get today's date
today = datetime.date.today()
random.seed(today.toordinal())  # Ensure daily consistency

# Select today's challenge and quote
daily_challenge = random.choice(challenges)
daily_quote = random.choice(quotes)

# Streamlit UI
st.title("🌱 Growth Mindset Challenge")
st.write("### Embrace challenges, learn, and grow every day!")

# Display daily challenge
st.subheader("📌 Today's Challenge")
st.write(daily_challenge)

# Display motivational quote
st.subheader("💡 Motivation for Today")
st.write(f"*{daily_quote}*")

# User progress tracking
st.subheader("📊 Your Progress")
completed = st.checkbox("I completed today's challenge!")
if completed:
    st.success("Great job! Keep pushing yourself every day! 🚀")

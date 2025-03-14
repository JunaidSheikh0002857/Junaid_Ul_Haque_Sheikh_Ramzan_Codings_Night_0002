import streamlit as st
import random

def main():
    st.title("Number Guessing Game")
    st.write("Guess a number between 1 and 100!")
    
    if 'random_number' not in st.session_state:
        st.session_state.random_number = random.randint(1, 100)
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    guess_button = st.button("Check Guess")
    
    if guess_button:
        st.session_state.attempts += 1
        if guess < st.session_state.random_number:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.random_number:
            st.warning("Too high! Try again.")
        else:
            st.success(f"Congratulations! You guessed it in {st.session_state.attempts} attempts.")
            st.balloons()
            st.session_state.random_number = random.randint(1, 100)
            st.session_state.attempts = 0
    
    st.write(f"Attempts: {st.session_state.attempts}")

if __name__ == "__main__":
    main()

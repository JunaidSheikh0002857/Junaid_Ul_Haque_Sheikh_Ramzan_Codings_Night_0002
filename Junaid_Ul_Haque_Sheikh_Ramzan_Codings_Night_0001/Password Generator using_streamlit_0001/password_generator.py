import streamlit as st
import random
import string

# Function to generate a random password
def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters  # Upper and lower case letters
    
    if use_digits:
        characters += string.digits  # Add digits (0-9)
    
    if use_special_chars:
        characters += string.punctuation  # Add special characters
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit UI
def main():
    st.title("🔐 Password Generator")
    
    # User inputs
    length = st.slider("Select password length:", min_value=6, max_value=30, value=12)
    use_digits = st.checkbox("Include numbers (0-9)")
    use_special_chars = st.checkbox("Include special characters (!@#$%^&*)")

    if st.button("Generate Password"):
        password = generate_password(length, use_digits, use_special_chars)
        st.success(f"Generated Password: **{password}**")

if __name__ == "__main__":
    main()

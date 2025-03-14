import streamlit as st

def main():
    st.title("Tip Calculator 💰")
    
    # Input for bill amount
    bill = st.number_input("Enter the total bill amount ($)", min_value=0.0, format="%.2f")
    
    # Tip percentage selection
    tip_percentage = st.slider("Select tip percentage:", 0, 50, 15)
    
    # Calculate tip and total bill
    tip_amount = (tip_percentage / 100) * bill
    total_bill = bill + tip_amount
    
    # Split bill among people
    people = st.number_input("Split among how many people?", min_value=1, value=1, step=1)
    
    if people > 0:
        per_person = total_bill / people
    else:
        per_person = 0

    # Display results
    st.subheader("Bill Summary:")
    st.write(f"**Tip Amount:** ${tip_amount:.2f}")
    st.write(f"**Total Bill (including tip):** ${total_bill:.2f}")
    st.write(f"**Each person should pay:** ${per_person:.2f}")

if __name__ == "__main__":
    main()
